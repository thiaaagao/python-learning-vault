---
tags: [python, fase-2, project]
phase: 2
topic: projeto-port-scanner
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
xp_earned: 0
---

# 🏆 Projeto — Port Scanner + Log Parser

⏱️ ~40 min | 🎯 Vale **50XP**

> Duas ferramentas em uma: scanner de portas e parser de logs de autenticação.

---

## Parte 1: Port Scanner

Scanner TCP básico usando `socket`:

```python
# Exemplo de uso:
# python scanner.py --host scanme.nmap.org --ports 20-1000
#
# Porta 22: ABERTA
# Porta 80: ABERTA
# Porta 443: FECHADA
```

### Requisitos:
- [ ] Usar argparse para host e range de portas
- [ ] Tentar conexão TCP em cada porta (timeout 1s)
- [ ] Mostrar portas ABERTA/FECHADA
- [ ] Salvar resultado em JSON (--output resultado.json)
- [ ] Tratar ConnectionError, timeout, interrupção (Ctrl+C)

---

## Parte 2: Log Parser

Parser de logs de autenticação:

```python
# Exemplo de uso:
# python log_parser.py --file auth.log --json saida.json
#
# Total de tentativas: 150
# Tentativas falhas: 23
# Tentativas de root: 5
# IPs suspeitos: 203.0.113.5, 198.51.100.2
```

### Requisitos:
- [ ] Ler arquivo de log (simule com um .txt)
- [ ] Extrair com regex: data, hora, usuário, IP, sucesso/falha
- [ ] Contar estatísticas (total, falhas, IPs únicos)
- [ ] Salvar em JSON
- [ ] Identificar IPs com mais de 3 falhas como "suspeitos"

---

## 🔐 Conexão Cyber

Port scanners são a base do **reconhecimento** em pentest. Log parsers são a base do **monitoramento defensivo**. Esta ferramenta combina ofensivo + defensivo.

---

## 📚 Recursos
- Módulo `socket`: `socket.connect_ex()`, `socket.gethostbyname()`
- Módulo `argparse`: argumentos CLI
- Módulo `re`: parsing de logs
- Módulo `json`: saída estruturada
