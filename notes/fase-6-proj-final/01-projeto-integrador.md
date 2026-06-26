---
tags:
- python
- fase-6
- final
phase: 6
topic: projeto-integrador
status: not-started
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# 🏆 Projeto Final — Ferramenta de Análise de Rede

⏱️ 4-6 semanas | 🎯 Vale **100XP**

> Integra tudo das Fases 1-5: fundamentos, scripts, OOP, APIs, dados.

---

## Especificação

Ferramenta CLI que combina:
- **Scanner de rede** (Fase 2) — TCP, range de IPs
- **API de threat intel** (Fase 4) — consulta a bases públicas
- **Análise de dados** (Fase 5) — pandas para relatórios
- **Arquitetura OOP** (Fase 3) — classes modulares
- **Testes** (Fase 3) — pytest coverage > 80%

### Comandos:
```bash
python netanalyzer.py scan 192.168.1.0/24 --output relatorio.json
python netanalyzer.py threat --ip 203.0.113.5
python netanalyzer.py report --input scans.json --format html
python netanalyzer.py monitor --interval 3600
```

### Estrutura:
```
netanalyzer/
├── scanner/          # Módulo de scanning
├── threat/           # Módulo de threat intel
├── report/           # Módulo de relatórios
├── monitor/          # Módulo de monitoramento
├── tests/            # Testes
├── main.py           # CLI entry point
├── requirements.txt
└── README.md
```

### Milestones

- [ ] **M1:** Scanner funcional com output JSON
- [ ] **M2:** Integração com 1 API de threat intel
- [ ] **M3:** Relatório em HTML com pandas + plotly
- [ ] **M4:** Monitoramento contínuo com schedule
- [ ] **M5:** Testes e packaging
