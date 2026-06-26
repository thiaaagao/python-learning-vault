---
tags: [python, fase-5, data-science]
phase: 5
topic: numpy-ml-basico
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# NumPy e Machine Learning Básico

⏱️ ~25 min | 🎯 Projeto: Dashboard de Threat Intel

## Ao final desta nota você será capaz de:
- [ ] Criar e manipular arrays NumPy
- [ ] Calcular estatísticas básicas com NumPy
- [ ] Treinar um classificador com scikit-learn
- [ ] Classificar tráfego de rede como normal ou suspeito

---

## Por que NumPy?

Pandas é construído **em cima** do NumPy. Arrays NumPy são a fundação de toda computação científica em Python.

```bash
pip install numpy scikit-learn pandas
```

```python
import numpy as np

# Array a partir de lista
dados = np.array([10, 20, 30, 40, 50])
print(dados.mean())   # 30.0
print(dados.std())    # 14.14
print(dados.max())    # 50
print(dados.shape)    # (5,)
```

---

## Operações Vetorizadas

Sem NumPy — loop lento:
```python
valores = [1, 2, 3, 4, 5]
quadrados = [x**2 for x in valores]  # ok, mas lento pra 1mi+ itens
```

Com NumPy — vetorizado (C por baixo):
```python
valores = np.array([1, 2, 3, 4, 5])
quadrados = valores ** 2  # [1, 4, 9, 16, 25]

# Filtros rápidos
acima_media = valores[valores > valores.mean()]
```

---

## Matrizes 2D

```python
# Matriz 3x3
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matriz.shape)     # (3, 3)
print(matriz[1, 2])     # 6 (linha 1, coluna 2)
print(matriz[:, 0])     # [1, 4, 7] (todas linhas, coluna 0)
print(matriz.mean(axis=0))  # média por coluna: [4, 5, 6]
```

**Uso em ML: `X` (features) é uma matriz 2D:**
```
# shape = (n_amostras, n_caracteristicas)
#         (linhas,      colunas)
```

---

## ML Básico — Classificação de Tráfego

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Dados simulados de tráfego de rede
# Features: [bytes_enviados, bytes_recebidos, num_conexoes, portas_diferentes]
X = np.array([
    [100,  200,  5, 2],    # normal
    [50,   80,   3, 1],    # normal
    [5000, 100,  50, 20],  # suspeito
    [20,   30,   2, 1],    # normal
    [8000, 50,   80, 30],  # suspeito
    [150,  300,  4, 2],    # normal
    [3000, 5000, 60, 15],  # suspeito
])

# Rótulos: 0 = normal, 1 = suspeito
y = np.array([0, 0, 1, 0, 1, 0, 1])

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Treinar modelo
modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

# Avaliar
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

# --- Prever tráfego novo ---
novo_trafego = np.array([[6000, 8000, 70, 25]])
previsao = modelo.predict(novo_trafego)
print("Suspeito!" if previsao[0] else "Normal")
```

---

## Pipeline Completo

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# Pipeline: normaliza dados + treina
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
print(f"Acurácia: {pipeline.score(X_test, y_test):.2f}")
```

---

## 🔐 Conexão Cyber

Sistemas de IDS (Intrusion Detection Systems) como Snort, Suricata e Zeek usam ML para classificar tráfego. Ferramentas como o Elastic SIEM têm modelos integrados de detecção de anomalias. Este exercício simula o núcleo de um sistema de detecção baseado em comportamento.

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um array NumPy com 100 números aleatórios e calcule média, mediana e desvio padrão
- [ ] 2. Adicione 3 features novas ao modelo (ex: horario, pais_origem, protocolo)
- [ ] 3. Treine o modelo com 20 amostras e veja a acurácia
- [ ] 4. Teste o modelo com um tráfego claramente anômalo (valores extremos)

---

## 📚 Recursos
- 📖 NumPy quickstart: https://numpy.org/doc/stable/user/quickstart.html
- 📖 scikit-learn: https://scikit-learn.org/stable/tutorial/basic/tutorial.html
- 🎥 Corey Schafer — NumPy: https://youtu.be/8Y0qQEh7dJg
- 🎥 Sentdex — ML com Python: https://youtu.be/ogfH2k1w7_I
