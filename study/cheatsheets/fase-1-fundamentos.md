---
tags: [python, cheatsheet, fase-1]
phase: 1
---

# Fase 1 — Fundamentos (Resumão)

## Tipos Básicos

```python
int     → 42
float   → 3.14
str     → "hello"
bool    → True / False
NoneType → None
```

Verifique com `type(var)`.

## Operadores

| Operador | Faz |
|----------|-----|
| `+ - * /` | Matemática básica |
| `//` | Divisão inteira |
| `%` | Módulo (resto) |
| `**` | Potência |
| `== != < > <= >=` | Comparação |
| `and or not` | Lógicos |

## Controle de Fluxo

```python
if condicao:
    ...
elif outra:
    ...
else:
    ...

for item in iteravel:
    ...

while condicao:
    ...
```

`range(inicio, fim, passo)` — gera sequência numérica.

## Estruturas de Dados

| Tipo | Mutável? | Sintaxe |
|------|----------|---------|
| Lista | ✅ | `[1, 2, 3]` |
| Tupla | ❌ | `(1, 2, 3)` |
| Dicionário | ✅ | `{"chave": "valor"}` |
| Set | ✅ | `{1, 2, 3}` |

### Listas

```python
lista.append(x)    # adiciona no final
lista.insert(i, x) # adiciona na posição i
lista.remove(x)    # remove primeira ocorrência
lista.pop(i)       # remove e retorna índice i
len(lista)         # tamanho
lista[i:j]         # slicing [inicio:fim:passo]
```

### Dicionários

```python
dict["chave"]       # acessa (KeyError se não existir)
dict.get("chave")   # acessa (None se não existir)
dict["nova"] = val  # adiciona/altera
del dict["chave"]   # remove
dict.keys()         # lista de chaves
dict.values()       # lista de valores
```

### Comprehensions

```python
[x * 2 for x in range(10)]          # lista
{x: x**2 for x in range(5)}         # dicionário
{x for x in lista if x % 2 == 0}    # set
```

## Funções

```python
def nome(param1, param2="padrão"):
    """Docstring explicando o que faz."""
    return resultado
```

- Sem `return` → retorna `None`
- `return a, b` → retorna tupla (unpacking: `x, y = func()`)
- `*args` → argumentos posicionais variáveis (tupla)
- `**kwargs` → argumentos nomeados variáveis (dict)

## Escopo (LEGB)

1. **L**ocal — dentro da função
2. **E**nclosing — função externa (closures)
3. **G**lobal — módulo
4. **B**uilt-in — funções nativas do Python

## Módulos e Importação

```python
import modulo
from modulo import funcao
import modulo as apelido
```

## Erros Comuns

```python
try:
    codigo_arriscado
except TipoDoErro as e:
    print(f"Erro: {e}")
```

## Projeto: Password Analyzer

- `string.ascii_letters`, `string.digits`, `string.punctuation`
- `random.choice()` e `random.shuffle()`
- `"".join(lista)` para juntar caracteres
