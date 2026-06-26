---
tags:
- python
- fase-2
- scripts
phase: 2
topic: arquivos-cli
status: not-started
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Arquivos e CLI

⏱️ ~20 min | 🎯 Projeto: Port Scanner + Log Parser

## Ao final desta nota você será capaz de:
- [ ] Ler e escrever arquivos (.txt, .csv, .json)
- [ ] Usar argparse para criar ferramentas CLI
- [ ] Trabalhar com diferentes formatos de arquivo

---

## Leitura de Arquivos

```python
# Modo seguro com context manager (with)
with open("dados.txt", "r") as f:
    conteudo = f.read()        # string inteira
    linhas = f.readlines()     # lista de linhas
```

Modos: `"r"` (leitura), `"w"` (escrita, sobrescreve), `"a"` (append), `"r+"` (leitura+escrita)

## Escrita de Arquivos

```python
with open("saida.txt", "w") as f:
    f.write("Linha 1\n")
    f.write("Linha 2\n")
```

---

## Trabalhando com CSV

```python
import csv

with open("logs.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["ip"], row["data"])
```

---

## Trabalhando com JSON

```python
import json

# Objeto Python
dados = {"ip": "192.168.1.1", "portas": [22, 80, 443]}

# Salvar como JSON
with open("scan.json", "w") as f:
    json.dump(dados, f, indent=2)

# Ler JSON
with open("scan.json", "r") as f:
    dados = json.load(f)
```

---

## Argumentos de Linha de Comando

```python
import argparse

parser = argparse.ArgumentParser(description="Port Scanner")
parser.add_argument("--host", required=True, help="Host alvo")
parser.add_argument("--ports", type=int, nargs="+", default=[80, 443])
parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()
print(f"Escaneando {args.host} nas portas {args.ports}")
```

Uso: `python scanner.py --host 192.168.1.1 --ports 22 80 443 --verbose`

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Leia um arquivo .txt e conte quantas linhas ele tem
- [ ] 2. Salve uma lista de IPs em um arquivo JSON
- [ ] 3. Crie um script CLI que aceita --nome e --idade e imprime uma saudação

---

## 📚 Recursos
- 📖 Automate the Boring Stuff (Files): https://automatetheboringstuff.com/2e/chapter9/
- 🎥 Corey Schafer - File Objects: https://youtu.be/Uh2ebFW8deM
