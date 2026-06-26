---
progress_percent: 0
status: not-started
updated: '2026-06-26'
---﻿---
tags: [python, fase-1, functions]
phase: 1
topic: funcoes-modulos
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Funções e Módulos

⏱️ ~20 min | 🎯 Projeto: Password Analyzer + Gerador

## Ao final desta nota você será capaz de:
- [ ] Definir funções com def
- [ ] Retornar valores com return
- [ ] Usar argumentos posicionais e nomeados
- [ ] Importar módulos da biblioteca padrão

---

## Definindo Funções

`python
def saudacao(nome):
    """Retorna uma saudação personalizada."""  # docstring
    return f"Olá, {nome}!"

mensagem = saudacao("Ana")
print(mensagem)  # Olá, Ana!
`

---

## Parâmetros Padrão

`python
def saudacao(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

print(saudacao("Ana"))           # Olá, Ana!
print(saudacao("Ana", "Oi"))     # Oi, Ana!
`

---

## Return vs Print

`python
def soma(a, b):
    return a + b   # devolve o valor para quem chamou

def mostra_soma(a, b):
    print(a + b)   # só mostra na tela

resultado = soma(3, 4)       # resultado = 7
resultado = mostra_soma(3, 4) # resultado = None!
`

**Regra:** Use 
eturn para processar dados, print para depuração.

---

## Módulos

`python
# Importar módulo inteiro
import math
print(math.sqrt(16))       # 4.0

# Importar função específica
from random import randint
print(randint(1, 10))      # número aleatório entre 1 e 10

# Importar com alias
import os as sistema
print(sistema.getcwd())    # diretório atual
`

---

## Módulos Úteis para Cyber Segurança

| Módulo | Uso |
|---|---|
| socket | Conexões de rede, port scanning |
| 
equests | Requisições HTTP |
| hashlib | Hashing (MD5, SHA256) |
| json | Parse de JSON (APIs) |
| 
e | Expressões regulares |
| subprocess | Executar comandos do sistema |
| ase64 | Codificação base64 |

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie uma função eh_par(n) que retorna True se o número for par
- [ ] 2. Crie uma função rea_circulo(raio) que usa math.pi para calcular área
- [ ] 3. Crie uma função gerar_senha(tamanho) que usa 
andom.choice() para gerar uma senha alfanumérica

---

## 📚 Recursos
- 🎥 Corey Schafer - Functions: https://youtu.be/9Os0o3wzS_I
- 🎥 Corey Schafer - Import: https://youtu.be/CqvZ3vGoGsQ
