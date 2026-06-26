---
tags: [python, fase-2, exceptions]
phase: 2
topic: excecoes
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Tratamento de Exceções

⏱️ ~15 min | 🎯 Projeto: Port Scanner + Log Parser

## Ao final desta nota você será capaz de:
- [ ] Usar try/except/else/finally
- [ ] Tratar exceções específicas
- [ ] Criar exceções personalizadas

---

## Try/Except

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Isso não é um número válido!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
```

---

## Else e Finally

```python
try:
    with open("dados.txt", "r") as f:
        conteudo = f.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
else:
    print(f"Arquivo lido com sucesso: {len(conteudo)} caracteres")
finally:
    print("Sempre executa, com ou sem erro")
```

---

## Levantar Exceções

```python
def verificar_senha(senha):
    if len(senha) < 8:
        raise ValueError("Senha muito curta. Mínimo 8 caracteres.")
    return True

try:
    verificar_senha("abc")
except ValueError as e:
    print(f"Erro: {e}")
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Faça um script que pede dois números e divide, tratando ValueError e ZeroDivisionError
- [ ] 2. Crie uma função que lê um arquivo JSON e trata FileNotFoundError + json.JSONDecodeError
