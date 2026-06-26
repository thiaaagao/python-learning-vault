---
tags: [python, fase-3, packaging]
phase: 3
topic: pacotes-venv
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Pacotes, venv e pip

⏱️ ~15 min | 🎯 Projeto: CLI Tool com OOP + Testes

## Ao final desta nota você será capaz de:
- [ ] Criar e ativar virtual environments
- [ ] Instalar pacotes com pip
- [ ] Organizar código em módulos e pacotes
- [ ] Congelar dependências com requirements.txt

---

## Virtual Environments

```powershell
# Criar ambiente
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\Activate.ps1

# Sair
deactivate
```

Sempre use venv por projeto — evita conflitos entre versões.

## pip

```powershell
pip install requests
pip install -r requirements.txt
pip list          # pacotes instalados
pip freeze > requirements.txt   # salvar dependências
```

---

## Organização em Pacotes

```
meu_projeto/
├── __init__.py       # marca como pacote
├── scanner/
│   ├── __init__.py
│   ├── tcp.py        # class TCPScanner
│   └── http.py       # class HTTPScanner
├── utils/
│   ├── __init__.py
│   ├── network.py
│   └── parse.py
├── main.py
└── requirements.txt
```

```python
# main.py
from scanner.tcp import TCPScanner
from utils.network import resolver_host

s = TCPScanner("example.com")
s.escanear(80)
```

---

## requirements.txt

```txt
requests>=2.31.0
pytest>=7.4.0
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um pacote com 2 módulos e um main.py que usa ambos
- [ ] 2. Crie um requirements.txt com requests e pytest
