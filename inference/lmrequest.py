import json
import re
from pathlib import Path

import requests

# =====================================================
# LM Studio
# =====================================================

URL = "http://localhost:1234/v1/chat/completions"

# =====================================================
# Prompt xKaliBrain
# =====================================================

SYSTEM_PROMPT = """
You are xKaliBrain, an AI agent specializing in attack surface analysis and cybersecurity.

Your task is to analyze raw technical reports (outputs from tools like nmap, dirb, gobuster, etc.) and classify the findings into specific macro categories.

Taxonomy of Vulnerabilities (Macro Vulnerabilities)

You must classify each finding EXCLUSIVELY into one of the 5 categories below:

1. VULN. MACRO 01 - Information Disclosure:
Unintentional exposure of sensitive information (server versions, languages, frameworks, HTTP headers, email addresses, metadata).

Example:
"Server: Apache"
"Email[admin@example.com]"
-> MACRO 01

2. VULN. MACRO 02 - Directory Traversal:
Unauthorized access to files or directories (administrative directories, .env configuration files, .php files, directory listings).

Example:
"http://example.com/admin - Status: 200"
"http://example.com/wp-config.php - Status: 200"
-> MACRO 02

3. VULN. MACRO 03 - Outdated Software:
Use of obsolete or End-of-Life software versions.

Example:
"nginx/1.18.0 (Ubuntu)"
"WordPress[6.2.6]"
"Aggressive OS guesses: Linux 3.2 - 3.16 (93%)"
-> MACRO 03

4. VULN. MACRO 04 - Infrastructure Disclosure:
Exposure of network architecture, DNS information or internal services.

Example:
"DNSSEC is not configured"
"22/tcp open ssh"
-> MACRO 04

5. VULN. MACRO 05 - Weak SSL/TLS Configuration:
Weak cryptographic protocols, insecure redirects, certificates or HTTPS/HSTS issues.

Example:
"Location: http://example.com"
"X-XSS-Protection[0]"
-> MACRO 05

OUTPUT INSTRUCTIONS

Return ONLY a valid JSON object.

Do not use Markdown.

Do not wrap the JSON with ```json.

Do not explain your answer.

Do not include reasoning.

The first character of your response must be {

The last character of your response must be }

Expected format:

{
    "findings_list": [
        {
            "finding": "...",
            "macro_id": "MACRO 0X",
            "justification": "..."
        }
    ]
}
"""

# =====================================================
# Função para extrair JSON
# =====================================================

def extract_json(answer: str):

    answer = answer.strip()

    # Remove blocos markdown
    if answer.startswith("```json"):
        answer = answer[len("```json"):]

    if answer.startswith("```"):
        answer = answer[3:]

    if answer.endswith("```"):
        answer = answer[:-3]

    answer = answer.strip()

    # Procura o primeiro objeto JSON
    match = re.search(r"\{.*\}", answer, re.DOTALL)

    if not match:
        raise ValueError("Nenhum objeto JSON encontrado na resposta do modelo.")

    return json.loads(match.group())


# =====================================================
# Diretórios
# =====================================================

REPORTS = Path("reports")
OUTPUTS = Path("outputs")

OUTPUTS.mkdir(exist_ok=True)

FILES = sorted(REPORTS.glob("*.txt"))

print(f"\n{len(FILES)} report(s) found.\n")

headers = {
    "Content-Type": "application/json"
}

# =====================================================
# Processamento
# =====================================================

for index, report_file in enumerate(FILES, start=1):

    print(f"[{index}/{len(FILES)}] Processing {report_file.name}")

    try:

        with open(report_file, "r", encoding="utf-8") as f:
            report = f.read()

        print(f"Characters: {len(report):,}")
        print(type(report))

        payload = {
            "model": "google/gemma-4-e2b",
            "temperature": 0,
            "max_tokens": 4096,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": report
                }
            ]
        }

        response = requests.post(
            URL,
            headers=headers,
            json=payload,
            timeout=600
        )

        if response.status_code != 200:
            print(f"HTTP {response.status_code}")
            print(response.text)
            print()
            continue

        answer = response.json()["choices"][0]["message"]["content"]

        print("\n========== RAW MODEL OUTPUT ==========\n")
        print(answer)
        print("\n======================================\n")

        parsed = extract_json(answer)

        output_file = OUTPUTS / f"{report_file.stem}.json"

        with open(output_file, "w", encoding="utf-8") as out:
            json.dump(
                parsed,
                out,
                indent=4,
                ensure_ascii=False
            )

        print("✓ Saved successfully\n")

    except json.JSONDecodeError as e:
        print("\nErro ao interpretar o JSON retornado pelo modelo.")
        print(e)
        print()

    except ValueError as e:
        print("\nErro ao localizar um JSON na resposta.")
        print(e)
        print()

    except Exception as e:
        print(f"\nErro inesperado:\n{e}\n")

print("Finished.")
