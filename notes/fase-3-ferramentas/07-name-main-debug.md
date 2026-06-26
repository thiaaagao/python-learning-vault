---
tags: [python, fase-3, debugging]
phase: 3
topic: name-main-debug
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Entry Points e Debugging

⏱️ ~15 min | 🎯 Projeto: CLI Tool com OOP + Testes

## Ao final desta nota você será capaz de:
- [ ] Usar `if __name__ == "__main__"` corretamente
- [ ] Depurar código com pdb
- [ ] Usar breakpoints estratégicos
- [ ] Inspecionar variáveis durante execução

---

## if __name__ == "__main__"

O padrão que separa **código reutilizável** de **código executável**:

```python
# scanner.py
import socket

def scan_porta(host, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, porta))
    sock.close()
    return result == 0

# Só executa se rodar este arquivo diretamente
if __name__ == "__main__":
    host = input("Host: ")
    porta = int(input("Porta: "))
    aberta = scan_porta(host, porta)
    print(f"Porta {porta}: {'ABERTA' if aberta else 'FECHADA'}")
```

Quando outro módulo importa `scanner.py`, o bloco `if` **não** executa. Só roda quando você chama `python scanner.py`.

---

## Por que isso importa

```python
# main.py — usa scanner como módulo
from scanner import scan_porta  # NÃO imprime nada, não pede input

print(scan_porta("example.com", 80))
```

Sem o `if __name__`, importar o módulo executaria o código de teste — causando efeitos colaterais inesperados.

---

## pdb — Python Debugger

```python
def processar_logs(caminho):
    with open(caminho) as f:
        linhas = f.readlines()

    import pdb; pdb.set_trace()  # <--- PAUSA AQUI

    for linha in linhas:
        print(linha.strip())
```

### Comandos pdb essenciais:

| Comando | Efeito |
|---|---|
| `n` (next) | Executa próxima linha |
| `s` (step) | Entra dentro de uma função |
| `c` (continue) | Continua até próximo breakpoint |
| `p var` (print) | Mostra valor de `var` |
| `l` (list) | Mostra código ao redor |
| `q` (quit) | Sai do debugger |
| `h` (help) | Lista comandos |

---

## breakpoint() — Python 3.7+

```python
def analisar_pacote(dados):
    total = sum(dados)
    media = total / len(dados) if dados else 0

    breakpoint()  # mesma coisa que pdb.set_trace()

    alertas = [d for d in dados if d > media * 3]
    return alertas

# Roda normalmente, pausa no breakpoint()
analisar_pacote([10, 12, 11, 13, 50, 12, 11])
```

**Dica:** `breakpoint()` é mais limpo e não precisa importar pdb.

---

## Debugging Estratégico

### Quando usar breakpoint:
1. **Antes de um erro** — quando você sabe onde algo quebra
2. **Dentro de condicionais** — pra verificar se entrou no if/else
3. **Em loops** — pra inspecionar iteração específica
4. **Valor inesperado** — quando uma variável não tem o valor esperado

```python
def validar_portas(portas):
    resultado = []
    for i, p in enumerate(portas):
        breakpoint()  # inspeciona p e i
        if not 1 <= p <= 65535:
            print(f"Porta inválida no índice {i}: {p}")
            continue
        resultado.append(p)
    return resultado
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Adicione `if __name__ == "__main__"` a um script existente da Fase 1 ou 2
- [ ] 2. Use breakpoint() dentro de um loop e inspecione variáveis com `p`
- [ ] 3. Debug um erro proposital (divisão por zero, lista vazia) com pdb

---

## 📚 Recursos
- 📖 pdb docs: https://docs.python.org/3/library/pdb.html
- 🎥 Real Python — Python Debugging: https://realpython.com/python-debugging-pdb/
