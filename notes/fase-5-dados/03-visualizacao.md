---
tags: [python, fase-5, visualization]
phase: 5
topic: visualizacao
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Visualização de Dados

⏱️ ~20 min | 🎯 Projeto: Dashboard de Threat Intel

## Ao final desta nota você será capaz de:
- [ ] Criar gráficos com matplotlib
- [ ] Criar gráficos interativos com plotly
- [ ] Visualizar distribuições de ataques
- [ ] Exportar gráficos para relatórios

---

## Matplotlib — Gráficos Estáticos

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("incidentes.csv")

# Gráfico de barras
contagem = df["severidade"].value_counts()
plt.bar(contagem.index, contagem.values)
plt.title("Incidentes por Severidade")
plt.xlabel("Severidade")
plt.ylabel("Quantidade")
plt.show()

# Salvar
plt.savefig("relatorio_severidade.png")
```

---

## Plotly — Gráficos Interativos

```python
import plotly.express as px
import pandas as pd

df = pd.read_csv("incidentes.csv")

# Gráfico de dispersão
fig = px.scatter(df, x="data", y="portas", color="pais",
                 title="Atividade por País")
fig.show()

# Salvar como HTML
fig.write_html("dashboard_atividade.html")

# Gráfico de linha temporal
df["data"] = pd.to_datetime(df["data"])
por_dia = df.groupby(df["data"].dt.date).size().reset_index(name="total")
fig = px.line(por_dia, x="data", y="total",
              title="Incidentes por Dia")
fig.show()
```

---

## Heatmap

```python
import plotly.express as px

# Tabela pivot: dia da semana x hora
df["hora"] = pd.to_datetime(df["timestamp"]).dt.hour
df["dia"] = pd.to_datetime(df["timestamp"]).dt.day_name()

pivot = df.pivot_table(index="dia", columns="hora",
                       aggfunc="size", fill_value=0)

fig = px.imshow(pivot, title="Atividade por Dia/Hora",
                labels=dict(x="Hora", y="Dia", color="Eventos"))
fig.show()
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um gráfico de barras com matplotlib mostrando incidentes por tipo
- [ ] 2. Crie um gráfico de linhas plotly mostrando tendência ao longo do tempo
- [ ] 3. Salve o gráfico como HTML e abra no navegador

---

## 📚 Recursos
- 📖 Plotly docs: https://plotly.com/python/
- 🎥 Corey Schafer - Matplotlib: https://youtu.be/UO98lJQ3QGI
