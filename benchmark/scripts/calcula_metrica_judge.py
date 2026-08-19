import json
from scripts import  utils
import os

modelo_gpt = "openai_gpt-oss-120b"
modelo_gemma = "gemma_3_27b"

model = modelo_gpt

def calcula_metricas_pred(modelo_preditor, output_print = True, pasta_avaliacoes = "judge_evaluations", pasta_results = "metric_results", const = False):
    """
    Calcula a métrica de Precision, Recall e F1-Score com base no JSON gerado pela avaliação do Judge 'llm_avaliador.py'.

    :param modelo_preditor: LLM candidato que será calculado as métricas.
    :param output_print: Indicador para printar ou não os resultados.
    :param pasta_avaliacoes: Pasta que terá as avaliações textuais do Judge
    :param const: Avaliação será realizada nas predições dos modelos gemma3-27b ou gpt-oss-120b, que possuem predições avaliadas manualmente.
    :return:
    """
    resultados_avaliados_json, df_avaliado = utils.organiza_dataset_analisado_judge(path_json =f'{pasta_avaliacoes}/{"CONST_" if const else ""}automatic_evaluations_{modelo_preditor.replace("/", "_")}.json')
    resultados_interpretados_json, df_interpretado = utils.organiza_dataset_interpretado(path_json ='dataset/interpreted_dataset.json')

    QNT_PREDICOES = 0
    QNT_TOTAL_DATASET_OURO = 0
    QNT_TP = 0
    QNT_FP = 0
    QNT_FN = 0



    for target_json in resultados_avaliados_json:
        target = target_json["target"]
        try:
            dicionario_correspondente = resultados_interpretados_json[target + "_inter.txt"]
        except:
            dicionario_correspondente = resultados_interpretados_json[target]


        indices_encontrados = set()
        for avaliacao in target_json["avaliacoes"]:
            QNT_PREDICOES += 1
            if avaliacao["rotulacao"] == "CORRETO": QNT_TP += 1
            else: QNT_FP += 1

            indices_encontrados.update( avaliacao["ids_correspondentes"] )

        indices_encontrados = sorted(indices_encontrados) # Índices encontrados pelo Judge.
        try:
            indices_originais = sorted(map(lambda x: int(x["ID"]), dicionario_correspondente)) # Índices verdadeiros, com base no dataset ouro.
        except:
            indices_originais = sorted(map(lambda x: int(x["id"]), dicionario_correspondente)) # Índices verdadeiros, com base no dataset ouro.


        QNT_TOTAL_DATASET_OURO += len(indices_originais)
        QNT_FN += len(indices_originais) - len(indices_encontrados)

    if QNT_PREDICOES > 0:
        precision = QNT_TP / QNT_PREDICOES
    else:
        precision = 1

    recall = 1 - (QNT_FN / QNT_TOTAL_DATASET_OURO)
    if precision + recall == 0: f1 = 0
    else: f1 = 2 * (precision * recall) / (precision + recall)

    if output_print:
        print(f"Métricas do AVALIADOR (LLM JUDGE) para o modelo {modelo_preditor}")
        print("Precisão = Do total das vulnerabilidades preditas pelo LLM, quantas são verdadeiras positivas?")
        print("Recall = Do total de vulnerabilidades no dataset ouro, quantas o LLM conseguiu captar?")
        print("Falsos Positivos = Vulnerabilidade que o LLM encontrou mas o avaliador considerou como inválido")
        print("Falsos Negativos = Vulnerabilidade do dataset ouro (interpretado) que não foi encontrado pelo LLM")

        print()
        print("Total dataset ouro:", QNT_TOTAL_DATASET_OURO)
        print("Total preditos:", QNT_PREDICOES)
        print("Corretos:", QNT_TP)
        print("Incorretos (FP):", QNT_FP)
        print("Não encontrados (FN):", QNT_FN)
        print("Precisão:", precision)
        print("Recall:", recall )
        print("F1:", f1)



    metrics_results = {"dataset_size": QNT_TOTAL_DATASET_OURO,
                       "predictions_size": QNT_PREDICOES,
                       "TP": QNT_TP,
                       "FP": QNT_FP,
                       "FN": QNT_FN,
                       "precision": precision,
                       "recall": recall,
                       "f1": f1
                       }

    os.makedirs(pasta_results, exist_ok=True)
    with open(f"{pasta_results}/prediction_metrics___preditor_{modelo_preditor.replace("/","_")}.json", 'w', encoding='utf-8') as json_file:
        json.dump(metrics_results, json_file, indent=4, ensure_ascii=False)

    return metrics_results

