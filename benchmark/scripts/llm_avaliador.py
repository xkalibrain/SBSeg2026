import json
from scripts import utils
from prompts.prompts import SYSTEM_PROMPT_AVALIADOR, SYSTEM_PROMPT_CORRIGE_JSON
from tqdm import tqdm
import os

def executa_judge(modelo_preditor, COLS_PREDICAO = ["finding", "justification"], COLS_INTERPRETADO = ["ID","Evidência"],
                  pasta_resultados = "judge_evaluations", original_predictions = False, pasta_predicoes = "models_predictions",
                  modelo_judge = "gemma-3-27b-it", dataset_anonimizado = False,
                  system_promt_judge = SYSTEM_PROMPT_AVALIADOR
                  ):
    """
    Código que executa o modelo avaliador (Judge) nas predições das LLMs geradas pelo arquivo 'executa_predicao_LLMs.py'

    :param modelo_preditor: Nome do LLM que realizou a predição dos relatórios brutos
    :param COLS_PREDICAO: Colunas (atributos) da predição que serão usadas para a avaliação do Judge
    :param COLS_INTERPRETADO: Colunas (atributos) do relatório interpretado que serão usadas para a avaliação do Judge
    :param pasta_resultados: Pasta onde os resultados serão guardados
    :param original_predictions: Se verdadeiro, recebe as predições originais do gemma3 e do gpt-oss-120b (Ambos foram rotulados manualmente, são usados para a calibração do Judge)
    :param modelo_judge: Nome do LLM que realizará a avaliação
    :param system_promt_judge: Prompt que será usado na avaliação
    :return: Lista com as predições avaliadas pelo Judge
    """
    if original_predictions: predictions_path = f"original_predictions/CONST_results_{modelo_preditor.replace("/","_")}.json"
    else: predictions_path = f'{pasta_predicoes}/results_{modelo_preditor.replace("/","_")}.json'
    resultados_llm_json, df_predicoes = utils.organiza_predicoes(path_json = predictions_path) # Organiza o arquivo das predições para ser usado como dict python ou dataframe
    resultados_interpretados_json, df_interpretado = utils.organiza_dataset_interpretado(path_json =f'dataset/{"anonymized_" if dataset_anonimizado else ""}interpreted_dataset.json') # Organiza o arquivo do dataset interpretado para ser usado como dict python ou dataframe

    print(df_predicoes.columns)
    print(df_interpretado.columns)

    lista_final_avaliacoes = []

    targets = list(df_interpretado.target.drop_duplicates())


    idx = 0
    open("debug.log", "w", encoding="utf-8").close()
    for i, TARGET_INVESTIGADO in enumerate(targets, start=1): # Loop para as predições de cada target
        print(f"[{i}/{len(targets)}] Target:", TARGET_INVESTIGADO)
        lista_target_avaliacoes = []


        df_predicoes_filtrado = df_predicoes[df_predicoes.target.str.contains(TARGET_INVESTIGADO)] # Filtra apenas as predições do target do loop
        for _, series in tqdm(df_predicoes_filtrado.iterrows(), total=len(df_predicoes_filtrado), desc=f"Processando vulnerabilidades", leave=False):
            if TARGET_INVESTIGADO not in series.target: continue
            dict_final_avaliacao = dict()

            # Metadados
            dict_final_avaliacao["evaluation_metadata"] = {"modelo_preditor": modelo_preditor,
                                                           "modelo_judge": modelo_judge,
                                                           "prompt": SYSTEM_PROMPT_AVALIADOR,
                                                           "cols_predicao": COLS_PREDICAO,
                                                           "cols_interpretado": COLS_INTERPRETADO
                                                           }


            target_predicao = series.target
            df_interpretado_filtrado = df_interpretado[ df_interpretado.target == target_predicao ] # Filtra os dados interpretados para usar apenas o target do loop

            string_predicao = utils.retorna_string_unica_vulnerabilidade(series, cols=COLS_PREDICAO)
            string_df = utils.retorna_string_multiplas_vulnerabilidades(df_interpretado_filtrado, cols = COLS_INTERPRETADO)

            user_prompt = f"""[PREDIÇÃO] (vulnerabilidade_predita)\n{string_predicao}\n\n[DATASET OURO] (vulnerabilidades_interpretadas)\n{string_df}"""


            response = utils.chat_completion(
                messages=[{"role": "system", "content": system_promt_judge},
                          {"role": "user", "content": user_prompt}
                          ],
                model=modelo_judge,
                temperature = 0.0
            )
            output = response.choices[0].message.content # Resultado da avaliação do JUDGE

            with open("debug.log", "a", encoding="utf-8") as f:
                f.write(string_predicao + "\n")
                f.write(output + "\n\n\n")

            for key, value in series.to_dict().items(): dict_final_avaliacao[key] = value

            ###
            ### VERIFICAÇÕES DE FORMATO CORRETO DO AVALIADOR
            ###

            try:
                rotulacao_dict = eval(utils.extract_dictionary(output, search_for="veredito"))
                veredito = rotulacao_dict["veredito"]
                correct_format = True
            except:
                correct_format = False

            try:
                ids_dict = eval(utils.extract_dictionary(output, search_for="ids_ouro_correspondentes"))
                ids = ids_dict["ids_ouro_correspondentes"]
                correct_format = True
            except:
                correct_format = False

            ### Caso tenha formato incorreto em algum dos atributos do JSON, tentar corrigir
            if not correct_format:
                new_response = utils.chat_completion(
                    messages=[{"role": "system", "content": SYSTEM_PROMPT_CORRIGE_JSON},
                              {"role": "user", "content": output}
                              ],
                    model=modelo_judge,
                    temperature = 0.0
                )
                output = new_response.choices[0].message.content

                with open("debug.log", "a", encoding="utf-8") as f:
                    f.write("##### CORREÇÃO! #####" + "\n")
                    f.write(string_predicao + "\n")
                    f.write(output + "\n\n\n")

                rotulacao_dict = eval(utils.extract_dictionary(output, search_for="veredito"))
                veredito = rotulacao_dict["veredito"]

                try:
                    ids_dict = eval(utils.extract_dictionary(output, search_for="ids_ouro_correspondentes"))
                    ids = ids_dict["ids_ouro_correspondentes"]
                except:
                    ids = []




            dict_final_avaliacao["resposne"] = output
            dict_final_avaliacao["rotulacao"] = veredito
            dict_final_avaliacao["ids_correspondentes"] = ids

            lista_target_avaliacoes.append(dict_final_avaliacao)




        # Adiciona na lista de avaliações e salva automaticamente na pasta resultados
        lista_final_avaliacoes.append({"target": TARGET_INVESTIGADO, "avaliacoes": lista_target_avaliacoes})

        os.makedirs(pasta_resultados, exist_ok=True)
        with open(f"{pasta_resultados}/automatic_evaluations_{modelo_preditor.replace("/","_")}.json", 'w', encoding='utf-8') as json_file:
            json.dump(lista_final_avaliacoes, json_file, indent=4, ensure_ascii=False)

    return lista_final_avaliacoes