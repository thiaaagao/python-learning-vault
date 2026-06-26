---
progress_percent: 0
status: not-started
updated: '2026-06-26'
---﻿---
tags: [python, fase-1, project]
phase: 1
topic: projeto-password-analyzer
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
xp_earned: 0
---

# 🏆 Projeto — Password Analyzer + Gerador

⏱️ ~30 min | 🎯 Vale **50XP**

> Aplique tudo que aprendeu: variáveis, condicionais, loops, funções, módulos.

---

## Especificação

Crie um programa que:

### 1. Analisador de Senhas
Recebe uma senha do usuário e avalia sua força:

`python
# Exemplo de execução:
# Digite uma senha: abc123
# Força: FRACA
# Critérios atendidos: 2/5
# Comprimento: 6 caracteres
# Contém número: Sim
# Contém maiúscula: Não
# Contém minúscula: Sim
# Contém especial: Não
`

### 2. Gerador de Senhas
Gera senhas aleatórias com parâmetros escolhidos:

`python
# Exemplo:
# Comprimento: 16
# Incluir maiúsculas? (s/n): s
# Incluir números? (s/n): s
# Incluir símbolos? (s/n): s
# Senha gerada: X7#mQ2@pR5*v
`

### Requisitos

- [ ] Função nalisar_senha(senha) que retorna um dicionário com resultado
- [ ] Função gerar_senha(tamanho, maiusculas, numeros, simbolos) que retorna string
- [ ] Função main() que orquestra o programa
- [ ] Menu com opções: 1-Analisar, 2-Gerar, 3-Sair
- [ ] Tratamento básico de erros (try/except para input)
- [ ] Loop até o usuário escolher sair

---

## 🔐 Conexão com Cyber Segurança

Analisadores de senha são a base de:
- **Password spraying detection** (logs de tentativas)
- **Auditoria de políticas** (verificar se senhas atendem requisitos)
- **Ferramentas de hardening** (como cracklib no Linux)

---

## 📚 Recursos
- Módulo string: string.ascii_letters, string.digits, string.punctuation
- Módulo 
andom: 
andom.choice(), 
andom.shuffle()
- join(): "".join(lista) para juntar caracteres
