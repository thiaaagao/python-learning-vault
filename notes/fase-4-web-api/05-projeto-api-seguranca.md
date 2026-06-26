---
tags: [python, fase-4, project]
phase: 4
topic: projeto-api-seguranca
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
xp_earned: 0
---

# 🏆 Projeto — API de Segurança

⏱️ ~45 min | 🎯 Vale **50XP**

> API REST para consulta de segurança de hosts, com histórico em SQLite.

---

## Especificação

Crie uma API FastAPI com os seguintes endpoints:

### Endpoints

| Método | Rota | Descrição |
|---|---|---|
| GET | `/api/health` | Status da API |
| POST | `/api/scan` | Escanea um host (aceita: host, portas) |
| GET | `/api/scans/` | Lista histórico de scans |
| GET | `/api/scans/{id}` | Detalhes de um scan |
| DELETE | `/api/scans/{id}` | Remove um scan |

### Requisitos

- [ ] Modelo `Scan` com SQLAlchemy + SQLite
- [ ] Endpoint POST `/api/scan` — recebe JSON, executa scan, salva no banco
- [ ] Endpoint GET `/api/scans/?host=X` — filtra por host opcional
- [ ] Tratamento de erros com HTTPException
- [ ] Validação com Pydantic (ScanRequest, ScanResponse)
- [ ] Rota async para suportar scans concorrentes
- [ ] Documentação automática em `/docs`

---

## 🔐 Conexão Cyber

APIs de segurança são o padrão da indústria: Shodan, VirusTotal, Censys, AbuseIPDB. Esta API simula o comportamento desses serviços, preparando você para integrar com ferramentas reais de threat intel.

---

## 📚 Recursos
- FastAPI + SQLite: https://fastapi.tiangolo.com/tutorial/sql-databases/
- Pydantic: https://docs.pydantic.dev/
