import utils
import pandas as pd
import json
import os

ordem_severidades = ['Crítica', 'Alta', 'Média', 'Baixa', 'Informativa']
ordem_macros = ['Infrastructure Disclosure', 'Outdated Softwares',
       'Directory Traversal', 'Information Disclosure',
       'Weak SSL/TLS Configuration']

lista_modelos = ['deepseek-r1-distill-llama-70b', 'deepseek-r1-distill-llama-8b', 'deepseek-r1-distill-qwen-14b',
                       'deepseek-r1-distill-qwen-32b', 'deepseek-r1-distill-qwen-7b', 'gemma-3-12b-it', 'gemma-3-1b-it',
                       'gemma-3-27b-it', 'gemma-3-4b-it', 'google_gemma-4-26b-a4b', 'google_gemma-4-e2b',
                       'llama-3.2-3b-instruct', 'llama-3.3-70b-instruct', 'llama-4-scout-17b-16e-instruct', 'meta-llama-3.1-8b-instruct',
                       'phi-4-mini-instruct', 'phi-4', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-14b',
                       'qwen3-30b-a3b', 'qwen3-32b', 'qwen3-4b', 'qwen3-8b', 'qwen_qwen3.6-27b', 'qwen_qwen3.6-35b-a3b']

modelo_campeao = 'google_gemma-4-e2b'


lista_resultados = []
for modelo_preditor in lista_modelos:
    pasta_resultados = "judge_evaluations"
    const = False

    resultados_avaliados_json, df_avaliado = utils.organiza_dataset_analisado_judge(path_json =f'{pasta_resultados}/{"CONST_" if const else ""}automatic_evaluations_{modelo_preditor}.json')
    resultados_interpretados_json, df_interpretado = utils.organiza_dataset_interpretado(path_json ='xKaliBurr_Datasets/interpreted_dataset.json')

    cvss_list = []
    severidades_list = []
    vulnerabilidades_list = []

    if modelo_preditor == modelo_campeao: modelo_campeao_list = []

    for target_json in resultados_avaliados_json:
        target = target_json["target"]
        dicionario_correspondente = resultados_interpretados_json[target + "_inter.txt"]
        indices_encontrados = set()
        qnt_TP = 0
        for avaliacao in target_json["avaliacoes"]:
            if avaliacao["rotulacao"] == "CORRETO":
                indices_encontrados.update(avaliacao["ids_correspondentes"])
                qnt_TP += 1

        indices_encontrados = sorted(indices_encontrados)

        qnt_total_vuln = len(dicionario_correspondente)
        vuln_encontradas = list(filter(lambda x: int(x["ID"]) in indices_encontrados, dicionario_correspondente))

        cvss_list.extend( list(map(lambda x: float(x["CVSS_Score"]), vuln_encontradas)) )
        severidades_list.extend( list(map(lambda x: x["Severidade"].split(".")[0], vuln_encontradas)) )
        vulnerabilidades_list.extend( list(map(lambda x: x["Vulnerabilidade_Macro"], vuln_encontradas)) )

        if modelo_preditor == modelo_campeao:
            modelo_campeao_target_dict = {"target": target,
                                          "qnt_vuln_verdadeiras": qnt_total_vuln,
                                          "qnt_vuln_preditas": len(vuln_encontradas),
                                          "tempo_inferencia": target_json["inference_time"],
                                          "recall": qnt_TP / qnt_total_vuln,
                                          "precision": min(1, qnt_TP / len(vuln_encontradas)),
                                          "qnt_VP": qnt_TP,
                                          "distribuicao_macros": pd.Series(list(map(lambda x: x["Vulnerabilidade_Macro"],vuln_encontradas))).value_counts().to_dict(),
                                          "IDs_encontrados": list(map(lambda x: int(x["ID"]), vuln_encontradas)),
                                          "lista_cvss": list(map(lambda x: float(x["CVSS_Score"]), vuln_encontradas)),
                                          "lista_severidades": list(map(lambda x: x["Severidade"].split(".")[0], vuln_encontradas)),
                                          "lista_macros": list(map(lambda x: x["Vulnerabilidade_Macro"], vuln_encontradas)),

                                          }
            modelo_campeao_list.append(modelo_campeao_target_dict)

    if modelo_preditor == modelo_campeao:
        os.makedirs("modelo_campeao/", exist_ok=True)
        with open(f"modelo_campeao/{modelo_campeao}_infos_tabela_overleaf.json", 'w', encoding='utf-8') as json_file:
            json.dump(modelo_campeao_list, json_file, indent=4, ensure_ascii=False)

    media_cvss = sum(cvss_list) / len(cvss_list)
    series_severidades = pd.Series(severidades_list).value_counts().reindex(ordem_severidades).fillna(0)
    series_vulnerabilidades = pd.Series(vulnerabilidades_list).value_counts().reindex(ordem_macros).fillna(0)

    lista_resultados.append([modelo_preditor, media_cvss,  *list(series_severidades), *list(series_vulnerabilidades) ])

df_final = pd.DataFrame(lista_resultados,
                    columns = ["modelo", "media_cvss", "sev_critica", "sev_alta", "sev_media", "sev_baixa", "sev_informativa", "macro_infrastructure_disclosure", "macro_outdated_softwares", "macro_directory_transversal", "macro_information_disclosure", "macro_weak_ssl_tls_configuration"])

dict_macros = {"macro_information_disclosure":"macro_1",
               "macro_directory_transversal":"macro_2",
               "macro_outdated_softwares":"macro_3",
               "macro_infrastructure_disclosure":"macro_4",
               "macro_weak_ssl_tls_configuration":"macro_5"}

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 200)


df_final_mesmo = df_final.rename(columns = dict_macros).iloc[:,:].sort_values(by = ["sev_critica", "media_cvss"], ascending = False).copy()
df_final_mesmo.to_csv("resultados_adicionais_benchmark.csv")