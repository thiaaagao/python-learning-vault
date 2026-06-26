---
tags: [python, fase-4, deploy]
phase: 4
topic: deploy-render
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Deploy no Render (Grátis)

⏱️ ~20 min | 🎯 Projeto: REST API de Segurança

## Ao final desta nota você será capaz de:
- [ ] Preparar um app Flask/FastAPI para produção
- [ ] Fazer deploy no Render (plano grátis)
- [ ] Configurar variáveis de ambiente
- [ ] Manter o app online 24/7

---

## Pré-requisitos

```powershell
# 1. Crie conta no Render: https://render.com
# 2. Conecte seu GitHub
# 3. Tenha o projeto versionado no GitHub
```

---

## 1. Preparar o App para Produção

### Estrutura necessária:
```
seu-projeto/
├── app.py              # ou main.py (FastAPI)
├── requirements.txt
├── .env                # variáveis locais (NÃO commitar)
└── .gitignore
```

### requirements.txt:

```
flask>=3.0
gunicorn>=21.2
python-dotenv>=1.0
```

Para FastAPI:
```
fastapi>=0.100
uvicorn>=0.23
gunicorn>=21.2
```

### .gitignore:

```
venv/
.env
__pycache__/
*.pyc
.DS_Store
```

---

## 2. Ponto de Entrada

### Flask:
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "ok"}

# NÃO usar app.run() — o Render usa gunicorn
```

### FastAPI:
```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"status": "ok"}
```

---

## 3. Deploy no Render

1. **Dashboard Render → New + → Web Service**
2. Conecte seu repositório GitHub
3. Configuração:

| Campo | Flask | FastAPI |
|---|---|---|
| Runtime | Python 3 | Python 3 |
| Build Command | `pip install -r requirements.txt` | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` | `gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app` |
| Plan | Free | Free |

4. **Advanced → Add Environment Variable**:
   - `SECRET_KEY` = (valor aleatório seguro)
   - `FLASK_ENV` = production
   - `DATABASE_URL` = (se usar banco)

5. **Deploy** → Render builda e sobe automaticamente

---

## 4. Variáveis de Ambiente

```python
# app.py — NUNCA coloque secrets no código
import os
from dotenv import load_dotenv

load_dotenv()  # carrega .env local

SECRET_KEY = os.getenv("SECRET_KEY", "fallback-dev")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///dev.db")
API_KEY_SHODAN = os.getenv("API_KEY_SHODAN")
```

```bash
# .env (local, não vai pro git)
SECRET_KEY=minha-chave-segura-aqui
API_KEY_SHODAN=abc123def456
```

No Render, essas variáveis são configuradas no dashboard (não precisa de .env).

---

## 5. Banco de Dados em Produção

SQLite **não funciona** no Render (dados são apagados a cada deploy).

### Opções grátis:
- **Render PostgreSQL** — 1GB grátis
- **Supabase** (PostgreSQL) — 500MB grátis
- **SQLite** → só para dev local

```python
# Use variável de ambiente para trocar o banco
import os

if os.getenv("RENDER"):
    DATABASE_URL = os.getenv("DATABASE_URL")  # PostgreSQL
else:
    DATABASE_URL = "sqlite:///dev.db"  # local
```

---

## 6. Manutenção

```powershell
# Logs no Render: Dashboard → seu-app → Logs
# Re-deploy: git push → Render rebuilda automático
# Sleep: plano grátis dorme após 15 min inativo
# Wake-up: primeira requisição após sleep leva ~30s
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Prepare requirements.txt e .gitignore para deploy
- [ ] 2. Faça deploy de um app Flask "Hello World" no Render
- [ ] 3. Configure uma variável de ambiente SECRET_KEY no Render
- [ ] 4. Acesse sua URL pública: `https://seu-app.onrender.com`

---

## 📚 Recursos
- 📖 Render docs: https://render.com/docs/deploy-flask
- 📖 FastAPI Deploy: https://fastapi.tiangolo.com/deployment/
- 🎥 Deploy Flask no Render: https://youtu.be/3a1_-ZQjWRw
