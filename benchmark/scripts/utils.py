from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import pandas as pd
import re

load_dotenv()
client = OpenAI(base_url=os.getenv("MACHINE_URL"), api_key="lm-studio") # Execução via lm-studio. Alterar a base_url para: 'http://127.0.0.1:1234/v1'.


def chat_completion(**args):
    response = client.chat.completions.create(
        **args
    )
    return response

def remove_reasoning(text, tag_inicial = r"<\|channel>", tag_final = r"<channel\|>"):
    pattern = fr"{tag_inicial}.*?{tag_final}"
    return re.sub(pattern, "", text, flags=re.DOTALL)

def extract_json_from_llm_response(response):
    if not isinstance(response, str):
        return None, False

    text = remove_reasoning(response.strip()).strip()

    # Remove blocos markdown ```json ... ``` ou ``` ... ```
    codeblock_pattern = r"```(?:json)?\s*([\s\S]*?)\s*```"
    match = re.search(codeblock_pattern, text, re.IGNORECASE)

    if match:
        text = match.group(1).strip()

    # Caso ainda tenha texto extra antes/depois do JSON
    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:
        text = text[start:end + 1]

    # Tenta converter para dict
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data, True
        else:
            return data, True
    except json.JSONDecodeError:
        return text, False

def limpa_target(x):
    return x.replace("_report.txt", "").replace("_inter.txt", "").replace("http://", "")

def organiza_predicoes(path_json):
    """
    Recupera o arquivo JSON gerado pelo LLM e transforma em Dict e DataFrame
    """
    with open(path_json, 'r', encoding="utf-8") as file:
        resultados_gemma_json = json.load(file)

    df_gemma = pd.DataFrame()
    for target_json in resultados_gemma_json:
        findings_list = target_json["results"]["findings_list"]
        df_findings = pd.DataFrame(findings_list)
        df_findings["target"] = limpa_target(target_json["target"])
        df_gemma = pd.concat([df_gemma, df_findings])

    return resultados_gemma_json, df_gemma

def organiza_dataset_interpretado(path_json):
    """
    Recupera o dataset ouro (vulnerabilidades esperadas dos targets usados) em formato JSON e transforma em Dict e DataFrame
    """
    with open(path_json, 'r', encoding="utf-8") as file:
        resultados_interpretados_json = json.load(file)

    df_interpretado = pd.DataFrame()
    for key in resultados_interpretados_json.keys():
        findings_list = resultados_interpretados_json[key]
        df_findings = pd.DataFrame(findings_list)
        df_findings["target"] = limpa_target(key)
        df_interpretado = pd.concat([df_interpretado, df_findings])

    return resultados_interpretados_json, df_interpretado


def organiza_dataset_analisado_judge(path_json, explode_ids=False):
    with open(path_json, 'r', encoding="utf-8") as file:
        resultados_avaliacao_json = json.load(file)

    df_avaliado = pd.DataFrame()
    for target_json in resultados_avaliacao_json:
        findings_list = target_json["avaliacoes"]
        df_findings = pd.DataFrame(findings_list)
        df_findings["target"] = limpa_target(target_json["target"])
        df_avaliado = pd.concat([df_avaliado, df_findings])

    if explode_ids:
        df_avaliado['ids_correspondentes'] = df_avaliado['ids_correspondentes'].apply(
            lambda x: [-1] if len(x) == 0 else x
        )
        df_avaliado = df_avaliado.explode('ids_correspondentes')

    return resultados_avaliacao_json, df_avaliado


def organiza_dataset_analisado_manualmente(path_json, explode_ids=False):
    with open(path_json, 'r', encoding="utf-8") as file:
        resultados_avaliacao_manual_json = json.load(file)

    df_avaliado_manualmente = pd.DataFrame()
    for target_json in resultados_avaliacao_manual_json:
        findings_list = target_json["results"]["findings_list"]
        df_findings = pd.DataFrame(findings_list)
        df_findings["target"] = limpa_target(target_json["target"]).replace("_report.txt", "")
        df_findings["ids_correspondentes"] = list(map(lambda x: x["avaliacao"]["id"], findings_list))
        df_avaliado_manualmente = pd.concat([df_avaliado_manualmente, df_findings])

    if explode_ids:
        df_avaliado_manualmente['ids_correspondentes'] = df_avaliado_manualmente['ids_correspondentes'].apply(
            lambda x: [-1] if len(x) == 0 else x
        )
        df_avaliado_manualmente = df_avaliado_manualmente.explode('ids_correspondentes')

    return resultados_avaliacao_manual_json, df_avaliado_manualmente

def retorna_string_unica_vulnerabilidade(series, cols):
    string_predicao = "\n".join([f"{key}: {value}" for key, value in series.to_dict().items() if
                                 key in cols ])
    return string_predicao

def retorna_string_multiplas_vulnerabilidades(df, cols):
    string_df = ""
    for i in range(df.shape[0]):
        string_df += "\n".join([f"{key}: {value}" for key, value in df[cols].iloc[i].to_dict().items()])
        string_df += "\n------------------------------------------------\n"
    return string_df

def extract_dictionary(text, search_for="valid_message"):
    dicts = []
    stack = 0
    start = None

    for i, ch in enumerate(text):
        if ch == '{':
            if stack == 0:
                start = i
            stack += 1
        elif ch == '}':
            stack -= 1
            if stack == 0 and start is not None:
                dicts.append(text[start:i+1])
                start = None

    if not dicts:
        return "{}"

    for d in dicts:
        if search_for in d:
            return d

    return dicts[0]