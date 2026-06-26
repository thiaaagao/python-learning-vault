---
tags: [python, fase-1, data-structures]
phase: 1
topic: estruturas-dados
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Estruturas de Dados

⏱️ ~25 min | 🎯 Projeto: Password Analyzer + Gerador

## Ao final desta nota você será capaz de:
- [ ] Usar listas, tuplas, dicionários e sets
- [ ] Fatiar (slicing) sequências
- [ ] Usar list comprehensions
- [ ] Escolher a estrutura certa para cada caso

---

## Listas []

Sequência **mutável** e ordenada:

`python
numeros = [1, 2, 3, 4, 5]
numeros.append(6)         # adiciona no final
numeros.insert(0, 0)      # adiciona no índice 0
numeros.remove(3)          # remove o valor 3
ultimo = numeros.pop()     # remove e retorna o último
print(numeros[0])          # primeiro elemento
print(numeros[-1])         # último elemento
print(len(numeros))        # tamanho
`

---

## Slicing

`python
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[2:5])     # [2, 3, 4]    (índices 2 até 4)
print(lista[:4])      # [0, 1, 2, 3] (do início até 3)
print(lista[6:])      # [6, 7, 8, 9] (do 6 até o fim)
print(lista[::2])     # [0, 2, 4, 6, 8] (passo 2)
print(lista[::-1])    # [9, 8, ..., 0] (invertido)
`

---

## Tuplas ()

**Imutável** — não pode alterar depois de criada:

`python
coord = (10, 20)
x, y = coord                   # unpacking
print(x)                       # 10

# coord[0] = 30 — ERRO! tupla não suporta atribuição
`

Use tuplas quando os dados não devem mudar (coordenadas, configurações).

---

## Dicionários {}

Pares chave-valor:

`python
aluno = {
    "nome": "Maria",
    "idade": 22,
    "curso": "Segurança"
}

print(aluno["nome"])           # Maria
aluno["idade"] = 23            # atualiza
aluno["email"] = "m@email.com" # adiciona

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
`

🔐 **Conexão Cyber:** Dicionários são ideais para representar pacotes de rede, headers HTTP, configurações de ferramentas de segurança.

---

## Sets {}

Coleção **não ordenada** e **sem duplicatas**:

`python
ips = {"192.168.1.1", "10.0.0.1", "192.168.1.1"}
print(ips)          # {"192.168.1.1", "10.0.0.1"} — sem duplicatas!

# Útil para remover IPs duplicados de logs
`

---

## List Comprehension

Sintaxe concisa para criar listas:

`python
# Forma tradicional:
quadrados = []
for n in range(10):
    quadrados.append(n ** 2)

# Comprehension:
quadrados = [n ** 2 for n in range(10)]

# Com condição:
pares = [n for n in range(20) if n % 2 == 0]
`

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie uma lista de 10 números e imprima apenas os pares
- [ ] 2. Dada uma lista de nomes, crie um dicionário nome → tamanho do nome
- [ ] 3. Use slicing para inverter uma string (ex: "python" → "nohtyp")

---

## 📚 Recursos
- 🎥 Corey Schafer - Lists/Tuples: https://youtu.be/W8KRzm-HUcc
- 🎥 Corey Schafer - Dictionaries: https://youtu.be/daefaLgNkw0
