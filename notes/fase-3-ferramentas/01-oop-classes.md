---
tags:
- python
- fase-3
- oop
phase: 3
topic: oop-classes
status: not-started
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Orientação a Objetos

⏱️ ~25 min | 🎯 Projeto: CLI Tool com OOP + Testes

## Ao final desta nota você será capaz de:
- [ ] Definir classes com __init__
- [ ] Criar métodos de instância
- [ ] Usar herança para reutilizar código
- [ ] Entender @property para getters/setters

---

## Classes e Objetos

```python
class Scanner:
    def __init__(self, host, timeout=1):
        self.host = host
        self.timeout = timeout
        self.portas_abertas = []

    def escanear(self, porta):
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(self.timeout)
        resultado = sock.connect_ex((self.host, porta))
        sock.close()
        if resultado == 0:
            self.portas_abertas.append(porta)
            return True
        return False

    def relatorio(self):
        return {
            "host": self.host,
            "portas_abertas": self.portas_abertas
        }

# Uso
s = Scanner("scanme.nmap.org")
s.escanear(22)
s.escanear(80)
print(s.relatorio())
```

---

## Herança

```python
class ScannerHTTP(Scanner):
    """Especialização: detecta servidor web"""
    def __init__(self, host):
        super().__init__(host)

    def detectar_servidor(self):
        if 80 in self.portas_abertas:
            import requests
            r = requests.get(f"http://{self.host}")
            return r.headers.get("Server")
        return None

s = ScannerHTTP("example.com")
s.escanear(80)
print(s.detectar_servidor())  # "Apache/2.4.41" ou similar
```

---

## @property

```python
class Conexao:
    def __init__(self, host, porta):
        self._host = host
        self._porta = porta

    @property
    def url(self):
        return f"http://{self._host}:{self._porta}"

    @property
    def porta(self):
        return self._porta

    @porta.setter
    def porta(self, valor):
        if not 1 <= valor <= 65535:
            raise ValueError("Porta inválida")
        self._porta = valor

c = Conexao("localhost", 8080)
print(c.url)       # http://localhost:8080 (getter)
c.porta = 9090     # setter com validação
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie uma classe `LogEntry` com atributos timestamp, ip, usuario, sucesso
- [ ] 2. Adicione método `to_dict()` que retorna um dicionário
- [ ] 3. Crie uma subclasse `FailedLogEntry` que automaticamente marca sucesso=False e adiciona um contador de tentativas

---

## 📚 Recursos
- 🎥 Corey Schafer - OOP Playlist: https://youtu.be/ZDa-Z5JzLYM
- 🎥 ArjanCodes - OOP Principles: https://youtu.be/pGz0ChXwMNU
