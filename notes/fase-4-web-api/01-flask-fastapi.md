---
tags: [python, fase-4, web]
phase: 4
topic: flask-fastapi
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Flask e FastAPI

⏱️ ~25 min | 🎯 Projeto: REST API de Segurança

## Ao final desta nota você será capaz de:
- [ ] Criar um servidor web com Flask
- [ ] Criar uma API REST com FastAPI
- [ ] Definir rotas e métodos HTTP
- [ ] Documentar endpoints automaticamente

---

## Flask — Micro Framework

```python
# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/api/scan", methods=["POST"])
def scan():
    dados = request.json
    host = dados.get("host")
    porta = dados.get("porta")
    # lógica de scan...
    return jsonify({"host": host, "porta": porta, "aberta": True}), 201

if __name__ == "__main__":
    app.run(debug=True)
```

---

## FastAPI — Moderno e Automático

```python
# main.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Security API")

class ScanRequest(BaseModel):
    host: str
    portas: list[int] = [80, 443]

class ScanResult(BaseModel):
    host: str
    portas_abertas: list[int]
    scan_time: float

@app.post("/scan", response_model=ScanResult)
async def scan(request: ScanRequest):
    # lógica...
    return ScanResult(host=request.host, portas_abertas=[80], scan_time=1.5)

# Documentação automática em /docs
```

---

## Comparação

| Característica | Flask | FastAPI |
|---|---|---|
| Simplicidade | ✅ Mínimo | ⚠️ Mais conceitos |
| Performance | ❌ Síncrono | ✅ Assíncrono nativo |
| Documentação | ❌ Manual | ✅ Automática (Swagger) |
| Validação | ❌ Manual | ✅ Pydantic |
| Indicação | Protótipos, microserviços | APIs de produção |

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um endpoint GET /ping que retorna {"pong": true}
- [ ] 2. Crie um endpoint POST /alerta que recebe JSON e salva em um arquivo
- [ ] 3. Teste no navegador ou curl: `curl http://localhost:5000/ping`

---

## 📚 Recursos
- 📖 FastAPI docs: https://fastapi.tiangolo.com/tutorial/
- 🎥 Corey Schafer - Flask: https://youtu.be/MwZwr5Tvyxo
