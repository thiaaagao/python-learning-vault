---
tags: [python, fase-3, testing]
phase: 3
topic: testes-pytest
status: not-started
priority: high
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Testes com Pytest

⏱️ ~20 min | 🎯 Projeto: CLI Tool com OOP + Testes

## Ao final desta nota você será capaz de:
- [ ] Escrever testes com pytest
- [ ] Usar assert para verificar resultados
- [ ] Organizar testes em arquivos separados
- [ ] Usar fixtures para dados compartilhados

---

## Primeiro Teste

```python
# test_scanner.py
from scanner import TCPScanner

def test_porta_valida():
    s = TCPScanner("localhost")
    assert s.porta_valida(80) == True
    assert s.porta_valida(0) == False
    assert s.porta_valida(70000) == False
```

```powershell
pytest test_scanner.py -v
```

---

## Fixtures

```python
import pytest

@pytest.fixture
def scanner():
    return TCPScanner("scanme.nmap.org")

def test_host_valido(scanner):
    assert scanner.host == "scanme.nmap.org"
```

---

## Testando Exceções

```python
import pytest

def test_porta_invalida():
    from scanner import TCPScanner
    s = TCPScanner("localhost")

    with pytest.raises(ValueError):
        s.escanear(-1)

    with pytest.raises(TypeError):
        s.escanear("abc")
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Escreva testes para a classe `LogEntry` da fase anterior
- [ ] 2. Escreva testes para o gerador de senhas (Fase 1)
- [ ] 3. Execute com `pytest -v` e veja todos passarem

---

## 📚 Recursos
- 📖 Pytest docs: https://docs.pytest.org/
- 🎥 Corey Schafer - Pytest: https://youtu.be/YbpKMIUjvK8
