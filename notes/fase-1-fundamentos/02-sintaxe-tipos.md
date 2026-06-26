---
tags: [python, fase-1, sintaxe]
phase: 1
topic: sintaxe-tipos
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Sintaxe e Tipos Básicos

⏱️ ~20 min | 🎯 Projeto: Password Analyzer + Gerador

## Ao final desta nota você será capaz de:
- [ ] Declarar variáveis com tipos int, float, str, bool
- [ ] Usar f-strings para formatar saída
- [ ] Converter entre tipos
- [ ] Identificar o tipo de qualquer valor com type()

---

## Variáveis

Python é **dinamicamente tipado** — você não declara o tipo, ele é inferido:

`python
nome = "Ana"          # str
idade = 25            # int
altura = 1.65         # float
estudante = True      # bool

print(type(idade))    # <class 'int'>
`

---

## Tipos Básicos

| Tipo | Exemplo | Uso |
|---|---|---|
| int | 42, -3, 1_000_000 | Números inteiros |
| loat | 3.14, -0.5, 1e6 | Números decimais |
| str | "hello", 'python' | Texto |
| ool | True, False | Lógico |
| NoneType | None | Ausência de valor |

---

## F-Strings (Python 3.6+)

`python
nome = "João"
idade = 30
print(f"Meu nome é {nome} e tenho {idade} anos")
# Meu nome é João e tenho 30 anos

print(f"Em 5 anos terei {idade + 5} anos")
# Em 5 anos terei 35 anos
`

---

## Conversão de Tipos

`python
idade_str = "25"
idade_int = int(idade_str)     # "25" → 25
preco = float("19.99")         # "19.99" → 19.99
valor = str(42)                # 42 → "42"
`

⚠️ **Armadilha:** int("abc") dá erro! Sempre trate entradas de usuário.

---

## Entrada do Usuário

`python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))  # input sempre retorna str!
`

---

## Comentários

`python
# Isso é um comentário de linha

"""
Isso é um comentário
de múltiplas linhas
(docstring)
"""
`

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie variáveis com seu nome, idade, altura. Imprima com f-string
- [ ] 2. Peça dois números ao usuário e mostre a soma
- [ ] 3. Mostre o tipo de cada variável usando type()

---

## 📚 Recursos
- 🎥 Corey Schafer - Variables: https://youtu.be/cQT33yu9pY8
- 📖 FreeCodeCamp - Variables: https://www.freecodecamp.org/learn/scientific-computing-with-python/
