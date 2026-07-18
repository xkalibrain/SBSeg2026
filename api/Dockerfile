FROM kalilinux/kali-rolling

WORKDIR /exekaliburr/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt -q update -y && apt -q upgrade -y
RUN apt -q install -y ca-certificates
RUN apt -q install -y python3 python3-pip python3-venv
RUN apt -q install -y figlet \
    host \
    nmap \
    dirb \
    whois \
    whatweb \
    dnsrecon \
    curl \
    dnsmap \
    gobuster

COPY requirements.txt .
RUN python3 -m venv venv
RUN venv/bin/pip3 install -r requirements.txt

COPY . .

CMD ["venv/bin/python3", "api.py"]
