---
tags: [python, fase-5, project]
phase: 5
topic: projeto-threat-dashboard
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
xp_earned: 0
---

# 🏆 Projeto — Dashboard de Threat Intel

⏱️ ~45 min | 🎯 Vale **50XP**

> Dashboard interativo de análise de ameaças usando pandas + plotly.

---

## Especificação

### Coleta de Dados
Crie um script que coleta dados simulados de ameaças (ou usa dados reais de fontes públicas como CVE feeds).

### Processamento com Pandas
- [ ] Carregar dados em DataFrame
- [ ] Limpar e normalizar (datas, remover duplicatas)
- [ ] Agrupar por severidade, país, tipo de ataque
- [ ] Identificar top 10 IPs mais ativos
- [ ] Estatísticas temporais (ataques por hora/dia/mês)

### Visualização com Plotly
- [ ] Gráfico de barras: incidentes por severidade
- [ ] Linha temporal: incidentes ao longo do tempo
- [ ] Heatmap: atividade por dia da semana x hora
- [ ] Scatter: portas abertas vs tempo de resposta
- [ ] Mapa (opcional): geolocalização dos IPs

### Entregáveis
- [ ] Script `coletar_dados.py` (scraping ou CSV simulado)
- [ ] Script `gerar_dashboard.py` (pandas + plotly → HTML)
- [ ] Dashboard interativo em `dashboard_threat.html`
- [ ] README.md do projeto

---

## 🔐 Conexão Cyber

Dashboards de threat intel são ferramentas essenciais de SOC (Security Operations Center). Ferramentas como Splunk, Elastic SIEM e Microsoft Sentinel usam exatamente os mesmos conceitos: coleta → processamento → visualização.

---

## 📚 Recursos
- Plotly: https://plotly.com/python/
- Pandas: https://pandas.pydata.org/
- CVE feed: https://cve.mitre.org/data/downloads/
