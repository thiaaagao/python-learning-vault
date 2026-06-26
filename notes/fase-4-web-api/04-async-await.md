---
tags:
- python
- fase-4
- async
phase: 4
topic: async-await
status: not-started
priority: medium
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Async/Await e Concorrência

⏱️ ~20 min | 🎯 Projeto: REST API de Segurança

## Ao final desta nota você será capaz de:
- [ ] Entender o conceito de async/await
- [ ] Usar asyncio para tarefas concorrentes
- [ ] Fazer requisições HTTP assíncronas com aiohttp
- [ ] Escanear múltiplos hosts em paralelo

---

## async/await

```python
import asyncio

async def escanear_host(host):
    print(f"Escaneando {host}...")
    await asyncio.sleep(1)  # simula scan
    print(f"{host} concluído")
    return f"{host}: portas [22, 80]"

async def main():
    resultado = await escanear_host("192.168.1.1")
    print(resultado)

asyncio.run(main())
```

---

## Múltiplas Tarefas

```python
import asyncio

async def escanear_host(host):
    await asyncio.sleep(1)
    return f"{host}: OK"

async def main():
    hosts = ["192.168.1.1", "10.0.0.1", "203.0.113.5"]

    # Executa em PARALELO
    tarefas = [escanear_host(h) for h in hosts]
    resultados = await asyncio.gather(*tarefas)

    for r in resultados:
        print(r)

# Tempo total: ~1s (não 3s!)
asyncio.run(main())
```

---

## aiohttp — HTTP Assíncrono

```python
import asyncio
import aiohttp

async def consultar_api(session, host):
    url = f"https://api.exemplo.com/scan/{host}"
    async with session.get(url) as response:
        return await response.json()

async def main():
    hosts = ["192.168.1.1", "10.0.0.1"]
    async with aiohttp.ClientSession() as session:
        tarefas = [consultar_api(session, h) for h in hosts]
        resultados = await asyncio.gather(*tarefas)
        print(resultados)

asyncio.run(main())
```

---

## 🔐 Caso de Uso: Scan em Massa

```python
import asyncio
import socket

async def check_port(host, port):
    loop = asyncio.get_event_loop()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    try:
        await loop.sock_connect(sock, (host, port))
        sock.close()
        return port, True
    except:
        sock.close()
        return port, False

async def scan_host(host, ports):
    tasks = [check_port(host, p) for p in ports]
    results = await asyncio.gather(*tasks)
    abertas = [p for p, status in results if status]
    return host, abertas

# Escaneia 1000 portas em segundos!
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie uma função async que espera 2 segundos e retorna "pronto"
- [ ] 2. Execute 5 tarefas em paralelo com asyncio.gather()
- [ ] 3. Use aiohttp para fazer 3 requisições GET concorrentes

---

## 📚 Recursos
- 📖 Real Python - Async IO: https://realpython.com/async-io-python/
- 📖 aiohttp docs: https://docs.aiohttp.org/
