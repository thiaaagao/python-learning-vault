---
tags: [python, fase-1, controle]
phase: 1
topic: controle-fluxo
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Controle de Fluxo

⏱️ ~20 min | 🎯 Projeto: Password Analyzer + Gerador

## Ao final desta nota você será capaz de:
- [ ] Usar if/elif/else para decisões
- [ ] Usar for e while loops
- [ ] Usar range() para sequências numéricas
- [ ] Combinar condições com and/or/not

---

## Condicionais — if/elif/else

`python
idade = 18

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")
# Adulto
`

---

## Operadores de Comparação

`python
==  # igual
!=  # diferente
<   # menor
>   # maior
<=  # menor ou igual
>=  # maior ou igual
`

---

## Operadores Lógicos

`python
and  # True se ambos True
or   # True se pelo menos um True
not  # inverte True/False
`

`python
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir")
# Pode dirigir
`

---

## Loop For

`python
# Iterando sobre uma lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# Usando range()
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8, 2):  # 2, 4, 6 (início, fim, passo)
    print(i)
`

---

## Loop While

`python
contador = 0
while contador < 5:
    print(contador)
    contador += 1     # IMPORTANTE: incrementar!
# 0 1 2 3 4
`

---

## Break e Continue

`python
for i in range(10):
    if i == 3:
        continue    # pula o 3
    if i == 7:
        break       # para no 7
    print(i)
# 0 1 2 4 5 6
`

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Peça um número e diga se é par ou ímpar
- [ ] 2. Imprima os números de 1 a 20, mas substitua múltiplos de 3 por "Fizz" e de 5 por "Buzz"
- [ ] 3. Crie um loop que soma números até o usuário digitar 0

---

## 📚 Recursos
- 🎥 Corey Schafer - If/Else: https://youtu.be/DZwmZ8Usvnk
- 🎥 Corey Schafer - For Loops: https://youtu.be/6iF8Xb7Z3wQ
