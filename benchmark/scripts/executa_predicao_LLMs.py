from scripts import utils
import os
import json
import time

from prompts.prompts import SYTEM_PROMPT_CORRIGE_JSON_PREDICAO

system_prompt = """### ROLE
You are xKaliBrain, an AI agent specializing in attack surface analysis and cybersecurity. 
Your task is to analyze raw technical reports (outputs from tools like nmap, dirb, gobuster, etc.) and classify the findings into specific macro categories.

Taxonomy of Vulnerabilities (Macro Vulnerabilities)
You must classify each finding EXCLUSIVELY into one of the 5 categories below:

1. VULN. MACRO 01 - Information Disclosure: Unintentional exposure of sensitive information (server versions, languages, frameworks, HTTP headers, email addresses, metadata).
   - Example: "Server: Apache" or "Email[exemplo@com.br]" -> MACRO 01.

2. VULN. MACRO 02 - Directory Traversal: Unauthorized access to files or directories (administrative directories, .env configuration files, .php files, directory listings).
   - Example: "http://www.exemplo.com.br/admin - Status: 200" or "http://www.exemplo.com.br/wp-config.php - Status: 200" -> MACRO 02.

3. VULN. MACRO 03 - Outdated Software: Use of components with obsolete or EOL (End of Life) versions.
   - Example: "nginx/1.18.0 (Ubuntu)" ou "WordPress[6.2.6]" or "Aggressive OS guesses: Linux 3.2 - 3.16 (93%)" -> MACRO 03.

4. VULN. MACRO 04 - Infrastructure Disclosure: Exposure of details of the network architecture, DNS, or internal services.
   - Example: "DNSSEC is not configured for www.exemplo.com.br" or "22/tcp open ssh" -> MACRO 04.

5. VULN. MACRO 05 - Weak SSL/TLS Configuration: Flaws in cryptographic protocols, insecure redirection, certificates, or absence of HTTPS/HSTS.
   - Example: "Location: http://www.exemplo.com/redirecionamento/inseguro" or "X-XSS-Protection[0]" -> MACRO 05.

### OUTPUT INSTRUCTIONS
For each finding identified in the raw report, respond in the following JSON format:
```
{ 
"findings_list": [
    {
    "finding": "[Short name of the finding]",
    "macro_id": "MACRO 0X",
    "justification": "[Brief explanation based on the macro definition]"
    }
                 ]
}
"""

def inferencia_llms(remaining_models, pasta_resultados = "models_predictions", pasta_relatorios = "reports"):
    """
    Função que executa uma lista de LLMs para realizar a predição com base nos relatórios brutos.
    As predições são a lista de achados para todos os targets analisados.
    """

    contents = os.listdir(f"{pasta_relatorios}/")

    for model in remaining_models: # Loop para rodar os modelos diferentes
        final_results = []
        print(f"##### EXECUTANDO MODELO {model.upper()} #####")
        n_files = len(contents)
        for i, file_name in enumerate(contents): # Loop para analisar os targets investigados
            if "_inter" in file_name: # Ignora os arquivos interpretados
                continue
            print(f"[{i}/{n_files}] {file_name}")

            with open(f"{pasta_relatorios}/{file_name}", "r") as f:
                relatorio = f.read() # Lê o relatório bruto

            start_time = time.time()
            try: # Predição od modelo para o relatório bruto
                response = utils.chat_completion(
                    messages = [{"role":"system", "content":system_prompt},
                                {"role":"user", "content": relatorio}
                                ],
                    model = model,
                    temperature=0.0
                )
            except Exception as e: # Caso dê erro em algum target, é printado no terminal
                print("!!!!! Erro no target", file_name)
                print("   ", e)
                print("INTERROMPENDO MODELO", model)
                break

            end_time = time.time()

            # Tempo de inferência do modelo
            inference_time = end_time - start_time

            # Coleta as informações de quantidade de tokens usado pelo modelo
            if hasattr(response, "usage") and response.usage is not None:
                prompt_tokens = response.usage.prompt_tokens
                completion_tokens = response.usage.completion_tokens
                total_tokens = response.usage.total_tokens
            else:
                prompt_tokens = None
                completion_tokens = None
                total_tokens = None

            output = response.choices[0].message.content
            model_output, correct_format = utils.extract_json_from_llm_response(output)

            if not correct_format:
                new_response = utils.chat_completion(
                    messages=[{"role": "system", "content": SYTEM_PROMPT_CORRIGE_JSON_PREDICAO},
                              {"role": "user", "content": output}
                              ],
                    model=model,
                    temperature=0.0
                )
                output = new_response.choices[0].message.content
                model_output, correct_format = utils.extract_json_from_llm_response(output)


            # Dicionário final com todas as informações da predição em um target (website) específico. Contém os resultados, quantidade de tokens e tempo de inferência
            final_dict = {
                "target": file_name,
                "results": model_output,
                "correct_format": correct_format,
                "inference_time": inference_time,
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": total_tokens
            }

            final_results.append(final_dict)

            os.makedirs(pasta_resultados, exist_ok=True)
            with open(f"{pasta_resultados}/results_{model.replace("/","_")}.json", 'w', encoding='utf-8') as json_file:
                json.dump(final_results, json_file, indent=4, ensure_ascii=False)
        print("\n")

        time.sleep(30)