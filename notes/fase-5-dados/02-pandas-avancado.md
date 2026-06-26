---
tags: [python, fase-5, data]
phase: 5
topic: pandas-avancado
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Pandas — Avançado

⏱️ ~20 min | 🎯 Projeto: Dashboard de Threat Intel

## Ao final desta nota você será capaz de:
- [ ] Agrupar dados com groupby
- [ ] Combinar DataFrames com merge
- [ ] Trabalhar com datas e séries temporais
- [ ] Criar pivot tables

---

## GroupBy

```python
import pandas as pd

df = pd.read_csv("incidentes.csv")

# Agrupar por país e contar
print(df.groupby("pais").size())

# Agrupar e calcular média
print(df.groupby("severidade")["portas"].mean())

# Múltiplas agregações
print(df.groupby("pais").agg({
    "portas": ["mean", "max"],
    "ip": "count"
}))
```

---

## Merge / Join

```python
# Dois DataFrames
ips = pd.DataFrame({
    "ip": ["192.168.1.1", "10.0.0.1"],
    "hostname": ["router", "server"]
})
geo = pd.DataFrame({
    "ip": ["192.168.1.1", "203.0.113.5"],
    "pais": ["BR", "US"]
})

# Inner join — só IPs que existem em ambos
resultado = pd.merge(ips, geo, on="ip", how="inner")
print(resultado)

# Left join — todos os IPs de ips
resultado = pd.merge(ips, geo, on="ip", how="left")
```

---

## Datas

```python
# Converter coluna para datetime
df["data"] = pd.to_datetime(df["ultimo_scan"])

# Filtrar por período
ultima_semana = df[df["data"] > "2024-01-01"]

# Extrair componentes
df["ano"] = df["data"].dt.year
df["mes"] = df["data"].dt.month
df["dia_semana"] = df["data"].dt.day_name()

# Reamostragem temporal
por_dia = df.resample("D", on="data").size()
```

---

## 🔐 Aplicação: Análise Temporal de Ataques

```python
# Agrupar tentativas de login por hora
df["hora"] = pd.to_datetime(df["timestamp"]).dt.hour
ataques_por_hora = df.groupby("hora").size()

# Identificar horários de pico de ataque
print(ataques_por_hora.sort_values(ascending=False).head(3))
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Agrupe logs por severidade e conte quantos em cada grupo
- [ ] 2. Faça merge de uma tabela de IPs com uma tabela de geolocalização
- [ ] 3. Filtre incidentes dos últimos 7 dias

---

## 📚 Recursos
- 🎥 Corey Schafer - GroupBy: https://youtu.be/qy0fDqoJxQ4
- 📖 Pandas Merge: https://pandas.pydata.org/docs/user_guide/merging.html
