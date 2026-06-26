"""Sync progress.yaml from actual vault state."""
import yaml
from pathlib import Path

VAULT = Path(__file__).parent.parent

# Load current progress from markdown frontmatter
progress_path = VAULT / "data" / "progress.md"
raw = progress_path.read_text(encoding="utf-8")
data = yaml.safe_load(raw.split("---", 2)[1] if raw.startswith("---") else raw)

p = data["progress"]

# Calculate phase progress from note frontmatter
for i in range(1, 7):
    phase_dir = VAULT / f"notes/fase-{i}"
    if not phase_dir.exists():
        continue

    notes = list(phase_dir.glob("*.md"))
    if not notes:
        p["phase_status"][f"phase_{i}"]["progress_percent"] = 0
        p["phase_status"][f"phase_{i}"]["status"] = "not-started"
        continue

    completed = 0
    for note in notes:
        content = note.read_text(encoding="utf-8")
        if "status: completed" in content:
            completed += 1

    total = len(notes)
    percent = round((completed / total) * 100) if total > 0 else 0

    status = "completed" if percent == 100 else "not-started" if percent == 0 else "studying"
    p["phase_status"][f"phase_{i}"]["progress_percent"] = percent
    p["phase_status"][f"phase_{i}"]["status"] = status

# Calculate global stats
completed_phases = sum(1 for i in range(1, 7) if p["phase_status"][f"phase_{i}"]["status"] == "completed")
active_phases = sum(1 for i in range(1, 7) if p["phase_status"][f"phase_{i}"]["status"] == "studying")

p["phases_completed"] = completed_phases
p["phases_in_progress"] = active_phases

# Find current phase
for i in range(1, 7):
    if p["phase_status"][f"phase_{i}"]["status"] != "completed":
        p["current_phase"] = i
        break
else:
    p["current_phase"] = 6

with open(progress_path, "w", encoding="utf-8") as f:
    f.write("---\n")
    yaml.dump(data, f, default_flow_style=False, allow_unicode=True)
    f.write("---\n")

print(f"Progresso atualizado: {completed_phases}/6 fases completas")
