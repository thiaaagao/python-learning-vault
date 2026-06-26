---
tags:
- python
- fase-1
- setup
phase: 1
topic: introducao
status: completed
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 100
---

# Introdução ao Python

⏱️ ~20 min | 🎯 Projeto: Password Analyzer + Gerador

## Ao final desta nota você será capaz de:
- [x] Instalar Python no seu sistema
- [x] Executar código Python no terminal
- [x] Usar o interpretador interativo (REPL)
- [x] Escrever seu primeiro script .py

---

## Instalação

### Verificar se já tem Python:
`powershell
python --version
`

Se aparecer Python 3.x.x — já está instalado.

### Download (se necessário):
Baixe de https://www.python.org/downloads/

**Importante:** Marque "Add Python to PATH" durante a instalação.

---

## Primeiro Script

Crie um arquivo ola.py:

`python
# ola.py
print("Olá, Python Journey!")
`

Execute:
`powershell
python ola.py
`

Saída esperada:
`
Olá, Python Journey!
`

---

## REPL — Modo Interativo

Digite python no terminal para entrar no REPL:

`python
>>> print("teste")
teste
>>> 2 + 2
4
>>> exit()
`

Útil para testar comandos rápidos sem criar arquivo.

---

## Hello, Hacker — Primeiro Exercício

`python
# hacker.py
nome = input("Digite seu nome: ")
print(f"Bem-vindo, {nome}. Seu treinamento Python começa agora.")
`

Execute e digite seu nome.

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [x] 1. Crie um script que pergunta sua idade e imprime "Você tem X anos"
- [x] 2. No REPL, calcule 15 * 37 e 2 ** 10 (potência)
- [x] 3. Crie um script que imprime seu nome 10 vezes (sem loop ainda — só 10 prints)

---

## 📚 Recursos
- 🎥 Corey Schafer: https://youtu.be/YYXdXT2l-Gg (Python Setup)
- 🎥 Curso em Vídeo Mundo 1 Aula 1: https://youtu.be/S9uPNwGsTEM
