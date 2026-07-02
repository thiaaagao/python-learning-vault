---
tags: [python, study, methodology]
created: 2026-06-26
---

# Sistema de Estudo

> Metodologia baseada no que funcionou para certificações AWS adaptada para Python:
> **teoria direta ao ponto → flashcards (SM-2) → simulados → análise de erro → revisão programada**

## Workflow Recomendado

### Diário (~30 min)

| Etapa | O que fazer | Comando |
|-------|-------------|---------|
| 1 | Revisar flashcards pendentes | `python scripts/study.py quiz` |
| 2 | Ler/estudar uma nota do vault | Abrir `notes/fase-N/` |
| 3 | Marcar checkboxes e rodar progresso | `python scripts/update_progress.py` |

### Semanal (~1h)

| Etapa | O que fazer | Comando |
|-------|-------------|---------|
| 1 | Revisar pontos fracos | `python scripts/study.py weaknesses` |
| 2 | Rodar simulado da fase atual | `python scripts/study.py test N` |
| 3 | Analisar erros (vão pro weaknesses) | Automático |
| 4 | Atualizar revisão programada | `python scripts/study.py update` |

### A cada novo tópico

| Etapa | O que fazer |
|-------|-------------|
| 1 | Estudar a nota no vault |
| 2 | Fazer os mini-exercícios |
| 3 | Adicionar flashcards sobre o tópico em `data/flashcards.md` |
| 4 | Rodar `python scripts/update_progress.py` |

## Ferramentas

| Recurso | Localização |
|---------|-------------|
| Flashcards com spaced repetition | `data/flashcards.md` |
| Simulados por fase | `data/tests/fase-*.yaml` |
| Caderno de pontos fracos | `study/weaknesses.md` |
| Revisão programada | `study/review-schedule.md` (gerado) |
| Resumões (cheatsheets) | `study/cheatsheets/` |
| Log de sessão de estudo | `study/session.md` |

## Progresso no Método

- [ ] Flashcards configurados e revisados
- [ ] Primeiro simulado feito
- [ ] Pontos fracos registrados
- [ ] Revisão programada ativa
- [ ] Cheatsheets criados
