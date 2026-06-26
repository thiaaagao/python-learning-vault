"""Sync progress based on checkbox completion across all notes."""
import re
import yaml
from pathlib import Path
from datetime import date

VAULT = Path(__file__).parent.parent
PHASES_DIRS = {
    1: "fase-1-fundamentos", 2: "fase-2-scripts", 3: "fase-3-ferramentas",
    4: "fase-4-web-api", 5: "fase-5-dados", 6: "fase-6-proj-final",
}

def parse_frontmatter(content):
    if not content.startswith("---"):
        return {}, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content
    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2]
    return fm, body

def count_checkboxes(text):
    unchecked = len(re.findall(r'- \[ \]', text))
    checked = len(re.findall(r'- \[x\]', text))
    return checked, unchecked

def checkboxes_in_body(body):
    return count_checkboxes(body)

# Load progress data
progress_path = VAULT / "data" / "progress.md"
raw = progress_path.read_text(encoding="utf-8")
data = yaml.safe_load(raw.split("---", 2)[1] if raw.startswith("---") else raw)
p = data["progress"]

today = date.today().isoformat()

for phase_num in range(1, 7):
    phase_dir = VAULT / "notes" / PHASES_DIRS[phase_num]
    if not phase_dir.exists():
        continue

    notes = sorted(phase_dir.glob("*.md"))
    if not notes:
        p["phase_status"][f"phase_{phase_num}"]["progress_percent"] = 0
        p["phase_status"][f"phase_{phase_num}"]["status"] = "not-started"
        continue

    phase_checked = 0
    phase_total = 0

    for note_path in notes:
        content = note_path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(content)

        checked, unchecked = checkboxes_in_body(body)
        total = checked + unchecked
        note_progress = round((checked / total) * 100) if total > 0 else 0

        fm["progress_percent"] = note_progress
        if note_progress == 0:
            fm["status"] = "not-started"
        elif note_progress == 100:
            fm["status"] = "completed"
        else:
            fm["status"] = "studying"
        fm["updated"] = today

        new_fm = yaml.dump(fm, default_flow_style=False, sort_keys=False, allow_unicode=True).strip()
        new_content = f"---\n{new_fm}\n---{body}"
        note_path.write_text(new_content, encoding="utf-8")

        phase_checked += checked
        phase_total += total

    phase_percent = round((phase_checked / phase_total) * 100) if phase_total > 0 else 0
    phase_status = "completed" if phase_percent == 100 else "not-started" if phase_percent == 0 else "studying"

    p["phase_status"][f"phase_{phase_num}"]["progress_percent"] = phase_percent
    p["phase_status"][f"phase_{phase_num}"]["status"] = phase_status

# Global stats
completed_phases = sum(1 for i in range(1, 7) if p["phase_status"][f"phase_{i}"]["status"] == "completed")
active_phases = sum(1 for i in range(1, 7) if p["phase_status"][f"phase_{i}"]["status"] == "studying")

p["phases_completed"] = completed_phases
p["phases_in_progress"] = active_phases

for i in range(1, 7):
    if p["phase_status"][f"phase_{i}"]["status"] != "completed":
        p["current_phase"] = i
        break
else:
    p["current_phase"] = 6

with open(progress_path, "w", encoding="utf-8") as f:
    f.write("---\n")
    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
    f.write("---\n")

total_notes = sum(1 for _ in Path(VAULT / "notes").rglob("*.md") if _.parent != VAULT / "notes" / "labs")
total_boxes = sum(len(re.findall(r'- \[ \]', _.read_text(encoding="utf-8"))) + len(re.findall(r'- \[x\]', _.read_text(encoding="utf-8"))) for _ in Path(VAULT / "notes").rglob("*.md") if _.parent != VAULT / "notes" / "labs")
total_checked = sum(len(re.findall(r'- \[x\]', _.read_text(encoding="utf-8"))) for _ in Path(VAULT / "notes").rglob("*.md") if _.parent != VAULT / "notes" / "labs")

print(f"Progresso: {completed_phases}/6 fases completas")
print(f"Checkboxes: {total_checked}/{total_boxes} ({round(total_checked/total_boxes*100) if total_boxes else 0}%)")
