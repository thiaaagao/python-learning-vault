---
tags:
- python
- fase-4
- web
phase: 4
topic: auth-forms-templates
status: not-started
priority: high
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# Templates, Formulários e Autenticação

⏱️ ~25 min | 🎯 Projeto: REST API de Segurança

## Ao final desta nota você será capaz de:
- [ ] Renderizar templates HTML com Jinja2
- [ ] Criar formulários com validação (WTForms)
- [ ] Implementar login com sessão
- [ ] Proteger rotas com autenticação

---

## Jinja2 Templates (Flask)

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", titulo="Security Dashboard")

@app.route("/host/<nome>")
def host_info(nome):
    return render_template("host.html", host=nome, portas=[22, 80, 443])
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html>
<head><title>{{ titulo }}</title></head>
<body>
    <h1>Bem-vindo ao {{ titulo }}</h1>
    <a href="/login">Login</a>
</body>
</html>
```

```html
<!-- templates/host.html -->
<h1>Host: {{ host }}</h1>
<ul>
{% for porta in portas %}
    <li>Porta {{ porta }}</li>
{% endfor %}
</ul>
```

---

## Formulários com WTForms

```bash
pip install flask-wtf
```

```python
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ScanForm(FlaskForm):
    host = StringField("Host", validators=[DataRequired()])
    porta = IntegerField("Porta", validators=[
        DataRequired(), NumberRange(1, 65535)
    ])
    submit = SubmitField("Escanear")
```

```python
@app.route("/scan", methods=["GET", "POST"])
def scan_page():
    form = ScanForm()
    if form.validate_on_submit():
        host = form.host.data
        porta = form.porta.data
        return f"Escaneando {host}:{porta}..."
    return render_template("scan.html", form=form)
```

```html
<!-- templates/scan.html -->
<form method="POST">
    {{ form.hidden_tag() }}
    <p>{{ form.host.label }} {{ form.host() }}</p>
    <p>{{ form.porta.label }} {{ form.porta() }}</p>
    <p>{{ form.submit() }}</p>
</form>
```

---

## Autenticação com Sessão

```python
from flask import Flask, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "troque-isso-por-uma-chave-segura"  # use os.urandom(24)

USUARIOS = {"admin": "senha123", "analista": "senha456"}

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if USUARIOS.get(usuario) == senha:
            session["user"] = usuario
            flash("Login bem-sucedido!")
            return redirect(url_for("dashboard"))
        flash("Usuário ou senha inválidos")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))
```

---

## Protegendo Rotas

```python
from functools import wraps

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            flash("Faça login primeiro")
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return wrapper

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", usuario=session["user"])
```

---

## Projeto Mini: Security Dashboard com Login

Combine tudo em um app:
- [ ] Página de login com WTForms
- [ ] Dashboard protegido que mostra histórico de scans
- [ ] Formulário para iniciar novo scan
- [ ] Botão de logout
- [ ] Templates com Jinja2 (herança de layout)

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um template base `layout.html` com nav bar e bloque de conteúdo
- [ ] 2. Crie um formulário de scan com validação de host e porta
- [ ] 3. Implemente login com sessão e rota protegida
- [ ] 4. Use flash messages para feedback de login

---

## 📚 Recursos
- 📖 Flask docs — Templates: https://flask.palletsprojects.com/patterns/templates/
- 📖 Flask-WTF: https://flask-wtf.readthedocs.io/
- 📖 Jinja2 docs: https://jinja.palletsprojects.com/
