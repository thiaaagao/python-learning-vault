# Python Journey Vault

Vault gamificado de aprendizado Python full stack com foco em Cyber Security.

Estrutura em 6 fases, sistema de XP/level, flashcards, dashboard interativo e projetos práticos. Design pensado para TDAH/autismo com blocos pequenos, checkboxes visíveis e progresso claro.

## Fases

| Fase | Tópico | Projeto | XP |
|------|--------|---------|----|
| 1 | Fundamentos | Password analyzer + gerador | 70 |
| 2 | Scripts & Automação | Port scanner + log parser | 70 |
| 3 | Ferramentas | CLI tool com OOP + testes | 70 |
| 4 | Web & API | REST API de segurança | 70 |
| 5 | Dados | Dashboard de threat intel | 70 |
| 6 | Projeto Final | Ferramenta completa | 100 |

## Como usar

1. Abra este vault no **Obsidian** (ou qualquer leitor de Markdown)
2. Ative os plugins: **Dataview**, **Linter**, **Yaml Manager**, **Force note view mode**
3. Comece pela **Fase 1**: `notes/fase-1-fundamentos/01-introducao-setup.md`
4. Acompanhe seu progresso pelo `dashboard.md`
5. Rode `python scripts/update_progress.py` para sincronizar o progresso automático

## Estrutura do vault

```
├── INDEX.md                # Índice geral com links rápidos
├── dashboard.md            # Dashboard interativo (Dataview)
├── data/                   # YAMLs de progresso, XP, flashcards
│   ├── progress.yaml
│   ├── xp.yaml
│   ├── flashcards.yaml
│   └── resources.yaml
├── notes/                  # Conteúdo das 6 fases
│   ├── fase-1-fundamentos/
│   ├── fase-2-scripts/
│   ├── fase-3-ferramentas/
│   ├── fase-4-web-api/
│   ├── fase-5-dados/
│   ├── fase-6-proj-final/
│   └── labs/
├── projects/               # Seus projetos práticos
├── scripts/                # Automação do vault
│   ├── update_progress.py
│   └── validate_vault.py
├── templates/              # Templates para novas notas
└── .obsidian/              # Configurações + plugins
```

## Sistema de Progresso

- Cada nota tem **frontmatter YAML** com status (`not-started` → `studying` → `completed`)
- **Mini-exercícios** com checkboxes valem 10 XP cada
- **Projetos** valem 50 XP
- A cada 100 XP você sobe de nível
- **Badges** são conquistadas ao completar fases

## Flashcards

Os flashcards ficam em `data/flashcards.yaml`. Alterne o status entre `unknown` → `learning` → `mastered` conforme sua familiaridade.

## Recursos incluídos

Links curados organizados por fase: vídeos (Corey Schafer, Tech With Tim, NetworkChuck, ArjanCodes), cursos (FreeCodeCamp, Curso em Vídeo), livros (Automate the Boring Stuff), e documentação oficial.

## Licença

MIT
