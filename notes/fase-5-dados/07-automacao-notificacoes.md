---
tags:
- python
- fase-5
- automation
phase: 5
topic: automacao-notificacoes
status: not-started
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Automação e Notificações

⏱️ ~25 min | 🎯 Projeto: Dashboard de Threat Intel

## Ao final desta nota você será capaz de:
- [ ] Enviar emails com Python (smtplib)
- [ ] Enviar notificações para Slack via webhook
- [ ] Automatar scraping com schedule + Selenium
- [ ] Criar um price tracker com alerta por email

---

## Email com smtplib

```python
import smtplib
from email.message import EmailMessage

def enviar_email(destino, assunto, corpo):
    msg = EmailMessage()
    msg.set_content(corpo)
    msg["Subject"] = assunto
    msg["From"] = "seu-email@gmail.com"
    msg["To"] = destino

    # Gmail: use "App Password" (senha de app)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("seu-email@gmail.com", "senha-de-app")
        smtp.send_message(msg)

enviar_email(
    "analista@empresa.com",
    "🚨 Alerta de Segurança",
    "Porta 22 exposta detectada no host 192.168.1.1"
)
```

**Gmail App Password:** Ative 2FA → Settings → Security → App Passwords.

---

## Slack — Webhook

1. Crie um webhook: https://api.slack.com/messaging/webhooks
2. Escolha um canal → Copie a URL

```python
import requests

def alerta_slack(mensagem):
    webhook_url = "https://hooks.slack.com/services/SEU/WEBHOOK/AQUI"
    payload = {"text": mensagem}
    requests.post(webhook_url, json=payload)

alerta_slack("🚨 Novo scan detectou 3 portas abertas em 10.0.0.5")
```

---

## SMS com Twilio (grátis)

```bash
pip install twilio
```

```python
from twilio.rest import Client

# Cadastre em https://www.twilio.com/try-twilio
account_sid = "SEU_SID"
auth_token = "SEU_TOKEN"

def alerta_sms(mensagem, para="+5511999999999"):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=mensagem,
        from_="+14155555555",  # número Twilio
        to=para
    )

alerta_sms("Alerta: tráfego anômalo detectado!")
```

---

## Price Tracker com Selenium + Email

```python
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

ALVO_PRECO = 500.00
PRODUTO_URL = "https://www.amazon.com.br/produto-x"
DESTINO_EMAIL = "seu-email@gmail.com"

def verificar_preco():
    driver = webdriver.Chrome()
    driver.get(PRODUTO_URL)

    try:
        preco_texto = driver.find_element(By.CLASS_NAME, "a-price-whole").text
        preco = float(preco_texto.replace(".", "").replace(",", "."))

        if preco <= ALVO_PRECO:
            enviar_email(
                DESTINO_EMAIL,
                "🔥 Preço Baixou!",
                f"{PRODUTO_URL}\nPreço atual: R${preco:.2f}"
            )
            print(f"Alerta enviado! Preço: R${preco:.2f}")
        else:
            print(f"Preço atual: R${preco:.2f} (acima de R${ALVO_PRECO:.2f})")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        driver.quit()

# Verificar a cada 6 horas
schedule.every(6).hours.do(verificar_preco)

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## Schedule — Agendamento

```python
import schedule

def scan_diario():
    print("Executando scan agendado...")

schedule.every(10).minutes.do(scan_diario)
schedule.every().hour.do(scan_diario)
schedule.every().day.at("08:00").do(scan_diario)
schedule.every().monday.do(scan_diario)

while True:
    schedule.run_pending()
    time.sleep(1)
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Envie um email de teste para si mesmo com smtplib
- [ ] 2. Crie um webhook do Slack e envie uma mensagem de alerta
- [ ] 3. Crie um price tracker que monitora 1 produto e envia email quando o preço cair
- [ ] 4. Agende seu script de scraping para rodar 2x ao dia

---

## 📚 Recursos
- 📖 smtplib docs: https://docs.python.org/3/library/smtplib.html
- 📖 Twilio Python: https://www.twilio.com/docs/libraries/python
- 📖 schedule docs: https://schedule.readthedocs.io/
