---
tags: [python, fase-3, functions]
phase: 3
topic: args-kwargs-lambda
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# *args, **kwargs e Lambda

⏱️ ~20 min | 🎯 Projeto: CLI Tool com OOP + Testes

## Ao final desta nota você será capaz de:
- [ ] Usar *args para argumentos posicionais variáveis
- [ ] Usar **kwargs para argumentos nomeados variáveis
- [ ] Criar funções anônimas com lambda
- [ ] Usar map() e filter() com lambda

---

## *args — Argumentos Posicionais Variáveis

```python
def somar(*args):
    """Soma qualquer quantidade de números"""
    total = 0
    for n in args:
        total += n
    return total

print(somar(1, 2))           # 3
print(somar(1, 2, 3, 4, 5)) # 15
print(somar())               # 0
```

**Desempacotamento:**
```python
numeros = [1, 2, 3, 4, 5]
print(somar(*numeros))  # * "espalha" a lista nos argumentos
```

---

## **kwargs — Argumentos Nomeados Variáveis

```python
def configurar(**kwargs):
    """Aceita qualquer parâmetro nomeado"""
    for chave, valor in kwargs.items():
        print(f"{chave} = {valor}")

configurar(host="localhost", porta=8080, ssl=True)
# host = localhost
# porta = 8080
# ssl = True
```

**Uso prático — passar config para funções:**
```python
def scan_host(host, **kwargs):
    timeout = kwargs.get("timeout", 1)
    portas = kwargs.get("portas", [80, 443])
    verbose = kwargs.get("verbose", False)
    # lógica do scan...

# Chamada limpa:
scan_host("example.com", timeout=2, portas=[22, 80, 443], verbose=True)
```

---

## Combinando *args e **kwargs

```python
def logger(func):
    """Decorator que loga qualquer função"""
    def wrapper(*args, **kwargs):
        print(f"Chamando {func.__name__} com args={args} kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def scan(host, porta, timeout=1):
    print(f"Escaneando {host}:{porta}...")

scan("localhost", 80, timeout=2)
# Chamando scan com args=('localhost', 80) kwargs={'timeout': 2}
# Escaneando localhost:80...
```

---

## Lambda — Funções Anônimas

```python
# Função normal
def dobro(x):
    return x * 2

# Equivalente lambda
dobro = lambda x: x * 2

print(dobro(5))  # 10
```

Lambda é uma função de **uma linha** sem nome. Útil para operações curtas.

---

## map() — Aplicar Função a uma Lista

```python
portas = [22, 80, 443, 8080]

# Com lambda (mais comum)
dobradas = list(map(lambda p: p * 2, portas))
print(dobradas)  # [44, 160, 886, 16160]

# Equivalente com list comprehension:
dobradas = [p * 2 for p in portas]
```

**map() com função nomeada:**
```python
def porta_para_nome(p):
    servicos = {22: "SSH", 80: "HTTP", 443: "HTTPS", 8080: "HTTP-Alt"}
    return servicos.get(p, "Desconhecida")

nomes = list(map(porta_para_nome, [22, 80, 443, 9999]))
print(nomes)  # ['SSH', 'HTTP', 'HTTPS', 'Desconhecida']
```

---

## filter() — Filtrar uma Lista

```python
portas = [22, 80, 443, 8080, 135, 445, 3389]

# Filtrar portas conhecidas (top 100)
portas_comuns = list(filter(lambda p: p in [22, 80, 443, 8080], portas))
print(portas_comuns)  # [22, 80, 443, 8080]
```

**Uso prático — filtrar logs:**
```python
logs = [
    "192.168.1.1 - OK",
    "10.0.0.5 - FAILED",
    "192.168.1.1 - FAILED",
    "10.0.0.5 - OK",
]

falhas = list(filter(lambda linha: "FAILED" in linha, logs))
print(falhas)
# ['10.0.0.5 - FAILED', '192.168.1.1 - FAILED']
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie uma função `media(*args)` que calcula a média de números
- [ ] 2. Use **kwargs em uma função `criar_alerta` que aceita titulo, descricao, severidade, e exibe formatado
- [ ] 3. Use map() + lambda para converter uma lista de portas string para int
- [ ] 4. Use filter() + lambda para extrair ips únicos de uma lista de logs

---

## 📚 Recursos
- 📖 *args e **kwargs: https://realpython.com/python-kwargs-and-args/
- 🎥 Corey Schafer — Lambda: https://youtu.be/25ovCm9jKfA
