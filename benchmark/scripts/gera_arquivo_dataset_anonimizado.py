import os
import json


def coletar_anonymized_interpreted_dataset(
    pasta_entrada="dataset_padronizado",
    pasta_saida="dataset",
    nome_saida="anonymized_interpreted_dataset.json",
):
    """
    Lê todos os arquivos JSON da pasta `dataset_padronizado` cujo nome contém
    a substring '_inter' e cria um único dicionário no formato:

    {
        "arquivo1_inter.json": {...},
        "arquivo2_inter.json": {...},
        ...
    }

    O resultado é salvo em:
        dataset/anonymized_interpreted_dataset.json

    Retorna:
        dict: dicionário consolidado.
    """

    os.makedirs(pasta_saida, exist_ok=True)

    dataset_final = {}

    for arquivo in os.listdir(pasta_entrada):
        if "_inter" not in arquivo or not arquivo.endswith(".json"):
            continue

        caminho_arquivo = os.path.join(pasta_entrada, arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as f:
            dataset_final[arquivo] = json.load(f)

    caminho_saida = os.path.join(pasta_saida, nome_saida)

    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(dataset_final, f, ensure_ascii=False, indent=4)

    return dataset_final

coletar_anonymized_interpreted_dataset(
    pasta_entrada="dataset_padronizado",
    pasta_saida="dataset",
    nome_saida="anonymized_interpreted_dataset.json",
)