---
tags: [python, fase-5, scraping]
phase: 5
topic: scraping-avancado
status: not-started
priority: medium
created: 2026-06-24
updated: 2026-06-24
started:
completed:
---

# Web Scraping Avançado

⏱️ ~20 min | 🎯 Projeto: Dashboard de Threat Intel

## Ao final desta nota você será capaz de:
- [ ] Extrair dados de páginas HTML com BeautifulSoup
- [ ] Navegar por páginas dinâmicas com Selenium
- [ ] Automatizar scraping com schedule
- [ ] Respeitar robots.txt e boas práticas

---

## BeautifulSoup

```python
import requests
from bs4 import BeautifulSoup

url = "https://example.com/cves"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Encontrar todas as tabelas
tabelas = soup.find_all("table")

# Extrair linhas
for tabela in tabelas:
    for linha in tabela.find_all("tr"):
        colunas = linha.find_all("td")
        if colunas:
            cve_id = colunas[0].text.strip()
            descricao = colunas[1].text.strip()
            print(f"{cve_id}: {descricao}")
```

---

## Selenium — Páginas Dinâmicas

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Iniciar navegador
driver = webdriver.Chrome()
driver.get("https://example.com/dashboard")

# Esperar carregar e extrair
elemento = driver.find_element(By.CLASS_NAME, "alerta")
print(elemento.text)

# Fechar
driver.quit()
```

---

## Automação com Schedule

```python
import schedule
import time
import requests

def coletar_threat_intel():
    """Coleta dados de fontes públicas a cada hora"""
    fontes = [
        "https://example.com/feeds/alerts.json",
        "https://example.com/feeds/cves.json"
    ]
    for fonte in fontes:
        try:
            r = requests.get(fonte, timeout=10)
            with open(f"data/{fonte.split('/')[-1]}", "w") as f:
                f.write(r.text)
            print(f"Coletado: {fonte}")
        except Exception as e:
            print(f"Erro: {e}")

# Agenda a cada hora
schedule.every(1).hours.do(coletar_threat_intel)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Use BeautifulSoup para extrair todos os links de uma página
- [ ] 2. Crie um scraping que coleta dados e salva em CSV
- [ ] 3. Agende a coleta para rodar a cada 30 minutos

---

## 📚 Recursos
- 📖 BeautifulSoup docs: https://www.crummy.com/software/BeautifulSoup/
- 📖 Selenium docs: https://selenium-python.readthedocs.io/
