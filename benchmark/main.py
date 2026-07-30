from scripts.executa_predicao_LLMs import inferencia_llms
from scripts.llm_avaliador import executa_judge
from scripts.calcula_metrica_judge import calcula_metricas_pred
from prompts.prompts_judge import SYSTEM_PROMPT_AVALIADOR_CAND2

### Modelos do Benchmark
# lista_modelos = ['deepseek-r1-distill-llama-70b', 'deepseek-r1-distill-llama-8b', 'deepseek-r1-distill-qwen-14b',
#                        'deepseek-r1-distill-qwen-32b', 'deepseek-r1-distill-qwen-7b', 'gemma-3-12b-it', 'gemma-3-1b-it',
#                        'gemma-3-27b-it', 'gemma-3-4b-it', 'google_gemma-4-26b-a4b', 'google_gemma-4-e2b',
#                        'llama-3.2-3b-instruct', 'llama-3.3-70b-instruct', 'llama-4-scout-17b-16e-instruct', 'meta-llama-3.1-8b-instruct',
#                        'phi-4-mini-instruct', 'phi-4', 'qwen3-0.6b', 'qwen3-1.7b', 'qwen3-14b',
#                        'qwen3-30b-a3b', 'qwen3-32b', 'qwen3-4b', 'qwen3-8b', 'qwen_qwen3.6-27b', 'qwen_qwen3.6-35b-a3b']

lista_modelos = ["google/gemma-4-e2b"] # Teste mínimo
ONLY_INFERENCE = False
modelo_judge = "gpt-oss-120b"

for inference_model in lista_modelos:
    inferencia_llms(remaining_models = [inference_model])
    if ONLY_INFERENCE: continue
    executa_judge(modelo_preditor = inference_model,
                  modelo_judge = modelo_judge,
                  system_promt_judge = SYSTEM_PROMPT_AVALIADOR_CAND2) # Recomendado o modelo "gpt-oss-120b" como Judge, dado o prompt utilizado
    calcula_metricas_pred(modelo_preditor=inference_model, output_print=True)