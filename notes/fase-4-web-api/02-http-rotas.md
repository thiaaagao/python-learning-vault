---
tags: [python, fase-4, http]
phase: 4
topic: http-rotas
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# HTTP, Rotas e Métodos

⏱️ ~15 min | 🎯 Projeto: REST API de Segurança

## Ao final desta nota você será capaz de:
- [ ] Entender os métodos HTTP (GET, POST, PUT, DELETE)
- [ ] Criar rotas com parâmetros de path e query
- [ ] Trabalhar com status codes
- [ ] Validar entrada com Pydantic

---

## Métodos HTTP

| Método | Ação | Exemplo |
|---|---|---|
| GET | Obter recurso | `GET /api/scans` |
| POST | Criar recurso | `POST /api/scan` |
| PUT | Atualizar recurso | `PUT /api/scans/123` |
| DELETE | Remover recurso | `DELETE /api/scans/123` |

---

## Parâmetros de Rota

```python
from fastapi import FastAPI

app = FastAPI()

# Path parameter
@app.get("/api/hosts/{host_id}")
async def get_host(host_id: int):
    return {"host_id": host_id}

# Query parameters
@app.get("/api/hosts/")
async def list_hosts(limit: int = 10, offset: int = 0):
    return {"limit": limit, "offset": offset}

# /api/hosts/?limit=5&offset=10
```

---

## Status Codes

```python
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

@app.post("/api/scan", status_code=status.HTTP_201_CREATED)
async def create_scan():
    # Criou com sucesso → 201
    return {"id": 1}

@app.get("/api/scans/{scan_id}")
async def get_scan(scan_id: int):
    if scan_id != 1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Scan não encontrado"
        )
    return {"id": scan_id, "status": "completo"}
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie rota GET /api/status que retorna uptime e versão da API
- [ ] 2. Crie rota GET /api/scan/{scan_id} com validação e erro 404 se não existir

---

## 📚 Recursos
- 📖 FastAPI Path Params: https://fastapi.tiangolo.com/tutorial/path-params/
- 📖 HTTP Status Codes: https://httpstatuses.io/
