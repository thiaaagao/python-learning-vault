---
tags:
- python
- fase-5
- data
phase: 5
topic: pandas-basico
status: not-started
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Pandas — Básico

⏱️ ~25 min | 🎯 Projeto: Dashboard de Threat Intel

## Ao final desta nota você será capaz de:
- [ ] Criar DataFrames a partir de CSV, JSON, dicts
- [ ] Filtrar, selecionar e ordenar dados
- [ ] Calcular estatísticas básicas
- [ ] Salvar resultados processados

---

## DataFrame

```python
import pandas as pd

# De um dicionário
dados = {
    "ip": ["192.168.1.1", "10.0.0.1", "203.0.113.5"],
    "portas": [3, 5, 12],
    "pais": ["BR", "US", "CN"],
    "ultimo_scan": ["2024-01-10", "2024-01-09", "2024-01-08"]
}
df = pd.DataFrame(dados)
print(df)
```

---

## Leitura de Arquivos

```python
# CSV
df = pd.read_csv("scans.csv")

# JSON
df = pd.read_json("scans.json")

# Excel
df = pd.read_excel("relatorio.xlsx")
```

---

## Seleção e Filtros

```python
# Colunas
print(df["ip"])            # uma coluna
print(df[["ip", "pais"]])  # múltiplas colunas

# Linhas por índice
print(df.iloc[0])          # primeira linha

# Filtro condicional
suspeitos = df[df["portas"] > 5]
print(suspeitos)

# Múltiplas condições
filtro = df[(df["portas"] > 5) & (df["pais"] == "CN")]
```

---

## Estatísticas Rápidas

```python
print(df.describe())        # estatísticas das colunas numéricas
print(df["pais"].value_counts())  # contagem por país
print(df["portas"].mean())  # média de portas
print(df["portas"].max())   # maior número de portas
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Carregue um CSV com dados de logs e mostre as 5 primeiras linhas
- [ ] 2. Filtre apenas entradas com severidade "alta" e salve em um novo CSV
- [ ] 3. Calcule a média e o máximo de uma coluna numérica

---

## 📚 Recursos
- 🎥 Corey Schafer - Pandas: https://youtu.be/ZyhVh-qRZPA
- 📖 Pandas docs: https://pandas.pydata.org/docs/
