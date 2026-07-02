"""Study system: flashcards (SM-2), tests, weaknesses, results."""
import argparse
import yaml
import random
import sys
from pathlib import Path
from datetime import date, timedelta
from collections import defaultdict

VAULT = Path(__file__).parent.parent
TODAY = date.today()

def to_date(val):
    if isinstance(val, date):
        return val
    return date.fromisoformat(str(val))

def load_yaml(path):
    raw = path.read_text(encoding="utf-8")
    if raw.startswith("---"):
        raw = raw.split("---", 2)[1]
    return yaml.safe_load(raw)

def save_yaml(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        f.write("---\n")

def save_md(path, content):
    path.write_text(content, encoding="utf-8")

# ─── FLASHCARDS (SM-2) ──────────────────────────────────────────────

def cmd_review():
    cards = load_yaml(VAULT / "data" / "flashcards.md")
    due = [c for c in cards["flashcards"] if to_date(c["next_review"]) <= TODAY]
    if not due:
        print("Nenhum flashcard pendente. Bela disciplina!")
        return
    print(f"Flashcards para revisar hoje: {len(due)}")
    for c in due:
        print(f"  [{c['status']}] (Fase {c['phase']}) {c['question']}")
    print("Rode 'python scripts/study.py quiz' para revisar.")

def cmd_quiz():
    cards = load_yaml(VAULT / "data" / "flashcards.md")
    due = [c for c in cards["flashcards"] if to_date(c["next_review"]) <= TODAY]
    if not due:
        due = random.sample(cards["flashcards"], min(5, len(cards["flashcards"])))
        print(f"(Nenhum pendente - revisando {len(due)} aleatorios)\n")
    random.shuffle(due)

    for card in due:
        print("")
        print("=" * 50)
        print(f"Fase {card['phase']} | {card['topic']} | {card['difficulty']}")
        print("=" * 50)
        print(f"\nPergunta: {card['question']}")
        input("[Enter] para ver a resposta...")
        print(f"\nResposta: {card['answer']}")

        grade = None
        while grade not in ("0", "1", "2", "3", "4", "5"):
            grade = input("Avalie (0=esqueci, 3=dificil mas lembrei, 5=facil): ").strip()
        grade = int(grade)

        if grade < 3:
            card["ease"] = max(1.3, card["ease"] - 0.2)
            card["interval"] = 1
            card["status"] = "learning"
        else:
            card["ease"] = min(3.0, card["ease"] + 0.1 * (grade - 3))
            if card["interval"] == 0:
                card["interval"] = 1
            elif card["interval"] == 1:
                card["interval"] = 3
            else:
                card["interval"] = round(card["interval"] * card["ease"])
            if grade >= 4 and card["status"] != "mastered":
                card["status"] = "learning"
            if card["interval"] >= 30:
                card["status"] = "mastered"

        card["next_review"] = (TODAY + timedelta(days=card["interval"])).isoformat()
        card["reviews"] += 1
        print(f"  -> Proxima revisao: {card['next_review']} (intervalo: {card['interval']}d, ease: {card['ease']:.1f})")

    save_yaml(VAULT / "data" / "flashcards.md", cards)
    print(f"\n[OK] {len(due)} flashcards revisados.")

# ─── TESTS ──────────────────────────────────────────────────────────

def cmd_test(phase=None):
    phases = [f"fase-{p}.yaml" for p in ([phase] if phase else range(1, 7))]
    all_questions = []

    for fname in phases:
        fpath = VAULT / "data" / "tests" / fname
        if fpath.exists():
            data = load_yaml(fpath)
            for q in data.get("questions", []):
                q["source_phase"] = fname.replace("fase-", "").replace(".yaml", "")
                all_questions.append(q)

    if not all_questions:
        print("Nenhuma questao encontrada.")
        return

    n = min(10, len(all_questions))
    selected = random.sample(all_questions, n)
    correct = 0

    print(f"Simulado ({n} questoes)")
    print("=" * 50)

    for i, q in enumerate(selected, 1):
        print(f"\n{i}. [Fase {q['source_phase']}] {q['domain']}")
        print(f"   {q['question']}")
        options = q["options"]
        letters = sorted(options.keys())
        for l in letters:
            print(f"   {l}) {options[l]}")

        answer = input("\n   Sua resposta: ").strip().lower()
        if answer == q["answer"]:
            print("   [OK] Correto!")
            correct += 1
        else:
            print(f"   [X] Errado. Resposta: {q['answer']}")
            print(f"   Explicacao: {q['explanation']}")
            log_weakness(TODAY, q["domain"], q["question"][:60], q["id"])

    pct = round(correct / n * 100)
    grade = "A" if pct >= 90 else "B" if pct >= 80 else "C" if pct >= 70 else "D" if pct >= 60 else "F"
    print(f"\n{'='*50}")
    print(f"Resultado: {correct}/{n} ({pct}%) - Nota: {grade}")
    print("=" * 50)

    results = load_yaml(VAULT / "data" / "tests" / "results.yaml")
    results.setdefault("results", []).append({
        "date": str(TODAY),
        "phase": phase or "all",
        "correct": correct,
        "total": n,
        "percent": pct,
        "grade": grade,
    })
    save_yaml(VAULT / "data" / "tests" / "results.yaml", results)
    print("Resultado salvo! Rode 'study.py results' para historico.")

def log_weakness(date, domain, error, question_id):
    wpath = VAULT / "study" / "weaknesses.md"
    entry = f"| {date} | {domain} | {error} | {question_id} | [ ] |\n"
    if wpath.exists():
        content = wpath.read_text(encoding="utf-8")
        if question_id not in content:
            content += entry
            wpath.write_text(content, encoding="utf-8")
    else:
        header = "# Caderno de Pontos Fracos\n\n| Data | Dominio | Erro | Questao | Revisado |\n|------|---------|------|---------|----------|\n"
        wpath.write_text(header + entry, encoding="utf-8")

# ─── RESULTS ─────────────────────────────────────────────────────────

def cmd_results():
    data = load_yaml(VAULT / "data" / "tests" / "results.yaml")
    results = data.get("results", [])
    if not results:
        print("Nenhum resultado ainda. Rode 'python scripts/study.py test' primeiro.")
        return

    print("Historico de Simulados\n")
    print(f"{'Data':<12} {'Fase':<8} {'Acertos':<8} {'%':<6} {'Nota':<4}")
    print("-" * 40)
    for r in results:
        print(f"{r['date']:<12} {r['phase']:<8} {r['correct']}/{r['total']:<5} {r['percent']}%  {r['grade']:>4}")

    wpath = VAULT / "study" / "weaknesses.md"
    if wpath.exists():
        weak_text = wpath.read_text(encoding="utf-8")
        domains_with_issues = set()
        for line in weak_text.split("\n"):
            if "[ ]" in line and "|" in line:
                parts = line.split("|")
                if len(parts) >= 3:
                    domains_with_issues.add(parts[2].strip())
        if domains_with_issues:
            print("\nDominios com pontos fracos pendentes:")
            for d in sorted(domains_with_issues):
                print(f"  [!] {d}")

# ─── WEAKNESSES ──────────────────────────────────────────────────────

def cmd_weaknesses():
    wpath = VAULT / "study" / "weaknesses.md"
    if not wpath.exists():
        print("Nenhum ponto fraco registrado ainda.")
        return

    content = wpath.read_text(encoding="utf-8")
    lines = content.strip().split("\n")
    weak_lines = [l for l in lines if l.startswith("|") and "[ ]" in l]

    if not weak_lines:
        print("Nenhum ponto fraco pendente. :)")
        return

    print(f"\nPontos fracos registrados: {len(weak_lines)}")
    print(f"\n{lines[2]}")
    print(lines[3])
    for l in weak_lines:
        print(l)

    mark = input("\nDeseja marcar algum como revisado? (id da questao ou Enter p/ sair): ").strip()
    if mark:
        new_lines = []
        for l in lines:
            if mark in l and "[ ]" in l:
                l = l.replace("[ ]", "[X]")
            new_lines.append(l)
        wpath.write_text("\n".join(new_lines), encoding="utf-8")
        print("Atualizado!")

# ─── UPDATE ──────────────────────────────────────────────────────────

def cmd_update():
    wpath = VAULT / "study" / "review-schedule.md"
    due = []
    cards_list = []
    try:
        cards = load_yaml(VAULT / "data" / "flashcards.md")
        cards_list = cards.get("flashcards", [])
        due = [c for c in cards_list if to_date(c["next_review"]) <= TODAY]
    except:
        pass

    weak_count = 0
    weak_path = VAULT / "study" / "weaknesses.md"
    if weak_path.exists():
        weak_count = sum(1 for l in weak_path.read_text(encoding="utf-8").split("\n") if "[ ]" in l)

    content = f"""# Revisao Programada

_Atualizado em: {TODAY}_

## Hoje
- **Flashcards pendentes:** {len(due)}
- **Pontos fracos:** {weak_count}

## Proximos Dias
"""
    for d in range(1, 8):
        nd = TODAY + timedelta(days=d)
        day_due = [c for c in cards_list if to_date(c["next_review"]) <= nd]
        content += f"- {nd}: {len(day_due)} flashcards\n"

    content += """
## Dominios para Revisar
"""
    reviewed_topics = set()
    for c in cards_list:
        if to_date(c["next_review"]) <= TODAY + timedelta(days=7):
            if c["topic"] not in reviewed_topics:
                content += f"- {c['topic']} (flashcards pendentes)\n"
                reviewed_topics.add(c["topic"])

    reviewed_domains = set()
    for d_phase in range(1, 7):
        fpath = VAULT / "data" / "tests" / f"fase-{d_phase}.yaml"
        if fpath.exists():
            tdata = load_yaml(fpath)
            for q in tdata.get("questions", []):
                w_path = VAULT / "study" / "weaknesses.md"
                if w_path.exists() and q["domain"] in w_path.read_text(encoding="utf-8") and "[ ]" in w_path.read_text(encoding="utf-8"):
                    if q["domain"] not in reviewed_domains:
                        content += f"- [!] {q['domain']} (ponto fraco)\n"
                        reviewed_domains.add(q["domain"])

    save_md(wpath, content)
    print(f"Revisao atualizada em study/review-schedule.md")

# ─── CLI ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Python Journey - Sistema de Estudo")
    parser.add_argument("command", nargs="?", default="review",
                        choices=["review", "quiz", "test", "results", "weaknesses", "update"],
                        help="Comando a executar")
    parser.add_argument("phase", nargs="?", type=int, choices=range(1, 7),
                        help="Fase para simulado (1-6)")

    args = parser.parse_args()

    if args.command == "review":
        cmd_review()
    elif args.command == "quiz":
        cmd_quiz()
    elif args.command == "test":
        cmd_test(args.phase)
    elif args.command == "results":
        cmd_results()
    elif args.command == "weaknesses":
        cmd_weaknesses()
    elif args.command == "update":
        cmd_update()

if __name__ == "__main__":
    main()
