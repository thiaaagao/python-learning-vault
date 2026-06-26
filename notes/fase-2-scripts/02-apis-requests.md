---
tags: [python, fase-2, apis]
phase: 2
topic: apis-requests
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# APIs com Requests

⏱️ ~20 min | 🎯 Projeto: Port Scanner + Log Parser

## Ao final desta nota você será capaz de:
- [ ] Fazer requisições GET e POST
- [ ] Processar respostas JSON
- [ ] Usar APIs públicas de segurança (Shodan, VirusTotal)
- [ ] Tratar erros de rede

---

## Introdução ao requests

```python
import requests

# GET simples
response = requests.get("https://api.github.com")
print(response.status_code)   # 200
print(response.json())         # dict com a resposta
```

---

## Requisições

```python
# GET com parâmetros
params = {"q": "python", "page": 1}
r = requests.get("https://api.github.com/search/repositories", params=params)

# POST com dados
dados = {"username": "admin", "password": "123456"}
r = requests.post("https://exemplo.com/login", json=dados)

# Headers personalizados
headers = {"Authorization": "Bearer token123", "User-Agent": "PythonJourney"}
r = requests.get("https://api.exemplo.com/dados", headers=headers)
```

---

## Tratamento de Erros

```python
try:
    r = requests.get("https://site-inexistente.xyz", timeout=5)
    r.raise_for_status()  # levanta exceção se status >= 400
    print(r.json())
except requests.exceptions.ConnectionError:
    print("Não foi possível conectar")
except requests.exceptions.Timeout:
    print("Timeout — servidor demorou demais")
except requests.exceptions.HTTPError as e:
    print(f"Erro HTTP: {e}")
```

---

## 🔐 API de Segurança: Shodan

Shodan indexa dispositivos conectados à internet.

```python
import requests

API_KEY = "sua_chave_aqui"  # cadastre em https://www.shodan.io
r = requests.get(f"https://api.shodan.io/shodan/host/search?key={API_KEY}&query=apache")
print(r.json())
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Faça GET em https://api.github.com/users/seu-nome e mostre nome e repositórios
- [ ] 2. Consulte a API pública do ViaCEP (https://viacep.com.br/) e busque um CEP
- [ ] 3. Adicione tratamento de timeout e ConnectionError

---

## 📚 Recursos
- 📖 Requests docs: https://requests.readthedocs.io/
- 🎥 Corey Schafer - Requests: https://youtu.be/tb8gHvYlCFs
