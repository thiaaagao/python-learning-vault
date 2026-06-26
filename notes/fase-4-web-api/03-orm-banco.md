---
tags:
- python
- fase-4
- database
phase: 4
topic: orm-banco
status: not-started
priority: medium
created: 2026-06-24
updated: '2026-06-26'
started: null
completed: null
progress_percent: 0
---

# ORM e Banco de Dados

⏱️ ~20 min | 🎯 Projeto: REST API de Segurança

## Ao final desta nota você será capaz de:
- [ ] Conectar SQLite com Python
- [ ] Definir modelos com SQLAlchemy
- [ ] Executar queries: insert, select, update, delete
- [ ] Usar ORM com FastAPI

---

## SQLite + SQLAlchemy

```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

engine = create_engine("sqlite:///scans.db")
Base = declarative_base()

class Scan(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True)
    host = Column(String, nullable=False)
    portas_abertas = Column(String)  # JSON string
    scan_time = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
```

---

## Operações Básicas

```python
# Criar sessão
session = Session()

# INSERT
novo_scan = Scan(host="192.168.1.1", portas_abertas="[22,80]")
session.add(novo_scan)
session.commit()

# SELECT todos
scans = session.query(Scan).all()

# SELECT com filtro
alvos = session.query(Scan).filter(Scan.host.like("192.168.%")).all()

# UPDATE
scan = session.query(Scan).first()
scan.host = "10.0.0.1"
session.commit()

# DELETE
session.query(Scan).filter(Scan.host == "10.0.0.1").delete()
session.commit()
```

---

## ORM + FastAPI

```python
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/scans/")
async def listar_scans(db: Session = Depends(get_db)):
    scans = db.query(Scan).all()
    return [{"id": s.id, "host": s.host} for s in scans]
```

---

## ⚡ Mini-Exercícios
> Marque ao concluir. Cada um vale 10XP!

- [ ] 1. Crie um modelo `Alerta` com campos: id, titulo, severidade, timestamp
- [ ] 2. Insira 3 alertas no banco e liste todos
- [ ] 3. Filtre alertas por severidade "alta"

---

## 📚 Recursos
- 📖 SQLAlchemy ORM Guide: https://docs.sqlalchemy.org/en/20/orm/
- 📖 FastAPI + SQLAlchemy: https://fastapi.tiangolo.com/tutorial/sql-databases/
