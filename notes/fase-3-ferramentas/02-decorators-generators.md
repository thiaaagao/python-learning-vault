---
tags: [python, fase-3, advanced]
phase: 3
topic: decorators-generators
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Decorators e Generators

⏱️ ~20 min | 🎯 Projeto: CLI Tool com OOP + Testes

## Ao final desta nota você será capaz de:
- [ ] Criar e usar decorators
- [ ] Usar generators com yield
- [ ] Aplicar decorators para logging, timing, auth

---

## Decorators

Funções que modificam outras funções:

```python
import time

def timer(func):
    """Mede o tempo de execução de uma função"""
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        duracao = time.time() - inicio
        print(f"{func.__name__} levou {duracao:.2f}s")
        return resultado
    return wrapper

@timer
def escanear_portas(host, portas):
    for p in portas:
        time.sleep(0.1)  # simula scan
    return len(portas)

escanear_portas("localhost", [22, 80, 443])
# escanear_portas levou 0.31s
```

---

## Decorator com Argumentos

```python
def repetir(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repetir(3)
def alerta():
    print("🚨 ALERTA DE SEGURANÇA!")

alerta()
# 🚨 ALERTA DE SEGURANÇA!
# 🚨 ALERTA DE SEGURANÇA!
# 🚨 ALERTA DE SEGURANÇA!
```

---

## Generators

```python
def ler_log_em_partes(caminho):
    """Lê arquivo linha por linha sem carregar tudo na memória"""
    with open(caminho, "r") as f:
        for linha in f:
            yield linha.strip()

# Uso — processa milhões de linhas sem estourar RAM
for linha in ler_log_em_partes("access.log"):
    if "FAILED" in linha:
        print(linha)
```

---

## Generator Expressions

```python
# List comprehension (carrega tudo na RAM)
quadrados = [x**2 for x in range(1000000)]

# Generator expression (preguiçoso, um por vez)
quadrados_gen = (x**2 for x in range(1000000))

# Ambos funcionam igual no loop, mas o generator usa menos memória
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um decorator `@log_chamada` que imprime "Chamando função X com argumentos Y"
- [ ] 2. Crie um generator `ips_unicos(logs)` que itera sobre logs e yield IPs sem repetir
