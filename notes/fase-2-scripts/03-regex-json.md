---
tags:
- python
- fase-2
- regex
phase: 2
topic: regex-json
status: not-started
priority: medium
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Expressões Regulares e JSON

⏱️ ~20 min | 🎯 Projeto: Port Scanner + Log Parser

## Ao final desta nota você será capaz de:
- [ ] Usar regex para buscar padrões em texto
- [ ] Extrair IPs, emails, URLs de logs
- [ ] Combinar regex + JSON para análise de dados

---

## Introdução ao re

```python
import re

texto = "Meu IP é 192.168.1.1 e o DNS é 8.8.8.8"

# Encontrar todos os IPs
ips = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", texto)
print(ips)  # ['192.168.1.1', '8.8.8.8']
```

---

## Padrões Comuns em Segurança

```python
# IP
r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Email
r"[\w.-]+@[\w.-]+\.\w+"

# URL
r"https?://[^\s]+"

# Data ISO
r"\d{4}-\d{2}-\d{2}"

# MAC Address
r"([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}"
```

---

## Grouping e Extração

```python
log = "2024-01-15 10:30:45 FAILED LOGIN from 203.0.113.5 user=admin"
pattern = r"(\d{4}-\d{2}-\d{2}) .* from (\d+\.\d+\.\d+\.\d+) user=(\w+)"

match = re.search(pattern, log)
if match:
    data, ip, usuario = match.groups()
    print(f"Data: {data}, IP: {ip}, Usuário: {usuario}")
```

---

## JSON + Regex = Análise de Logs

```python
import re, json

# Simular parsing de log de SSH
log_entry = "2024-01-15 10:30:45 sshd[1234]: Failed password for root from 203.0.113.5 port 22 ssh2"

pattern = r"(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) .* Failed password for (\w+) from ([\d.]+)"

match = re.search(pattern, log_entry)
if match:
    data, hora, usuario, ip = match.groups()
    evento = {
        "data": data,
        "hora": hora,
        "tipo": "failed_login",
        "usuario": usuario,
        "ip": ip,
        "severidade": "alta"
    }
    print(json.dumps(evento, indent=2))
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Extraia todos os IPs de um arquivo de log (simulado em string)
- [ ] 2. Valide se uma string é um email válido usando regex
- [ ] 3. Transforme um log em JSON estruturado

---

## 📚 Recursos
- 🎥 Corey Schafer - Regex: https://youtu.be/sa-TUpSx1JA
- 🔧 Testador de regex online: https://regex101.com/
