import json
import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(base_url=os.getenv("MACHINE_URL"), api_key="lm-studio")

model_sizes = {
    'deepseek-r1-distill-llama-70b': 70,
    'deepseek-r1-distill-llama-8b': 8,
    'deepseek-r1-distill-qwen-1.5b': 1.5,
    'deepseek-r1-distill-qwen-14b': 14,
    'deepseek-r1-distill-qwen-32b': 32,
    'deepseek-r1-distill-qwen-7b': 7,
    'gemma-3-12b-it': 12,
    'gemma-3-1b-it': 1,
    'gemma-3-4b-it': 4,
    'gemma-3-27b-it': 27,
    'google_gemma-4-26b-a4b': 26,
    'google_gemma-4-e2b': 5.1,
    'google_gemma-4-e4b': 8,
    'google_gemma-4-E2B': 5.1,
    'google_gemma-4-E4B': 8,
    'gpt-oss-20b': 20,
    'llama-3.2-1b-instruct': 1,
    'llama-3.2-3b-instruct': 3,
    'llama-3.3-70b-instruct': 70,
    'llama-4-scout-17b-16e-instruct': 109,
    'meta-llama-3.1-8b-instruct': 8,
    'openai_gpt-oss-120b': 120,
    'phi-4-mini-instruct': 3.8,
    'phi-4': 14,
    'qwen3-0.6b': 0.6,
    'qwen3-1.7b': 1.7,
    'qwen3-14b': 14,
    'qwen3-30b-a3b': 30,
    'qwen3-32b': 32,
    'qwen3-4b': 4,
    'qwen3-8b': 8,
    'qwen_qwen3.6-27b': 27,
    'qwen_qwen3.6-35b-a3b': 35
}


arquivos = os.listdir("metric_results/")
final_results = []
for arquivo in arquivos:
    if arquivo == "resultados_antigos": continue
    model_name = arquivo.split("_preditor_")[1].split(".json")[0]

    with open(f"metric_results/{arquivo}", "r", encoding = "utf-8") as file:
        results = json.load(file)

    results["model_name"] = model_name
    results["model_size"] = model_sizes[model_name]
    final_results.append(results)

df_results = pd.DataFrame(final_results)
df_results_metrics = df_results[["model_name", "model_size", "f1", "recall", "precision"]]
print(df_results_metrics.sort_values(by = "f1", ascending = False))

print(list(df_results_metrics.model_name))

df_results_metrics.sort_values(by = "f1", ascending = False).to_csv("resultados_benchmark.csv")
