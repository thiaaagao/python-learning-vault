"""Validate vault integrity: frontmatter, data files, required structure."""
import os
import yaml
import glob
from pathlib import Path

VAULT = Path(__file__).parent.parent
REQUIRED_DIRS = ["data", "notes/fase-1-fundamentos", "notes/fase-6-proj-final", "templates", "scripts"]
REQUIRED_DATA = ["progress.yaml", "xp.yaml", "flashcards.yaml", "resources.yaml"]

errors = []
warnings = []

def error(msg): errors.append(f"❌ {msg}")
def warn(msg): warnings.append(f"⚠️  {msg}")

# Check required dirs
for d in REQUIRED_DIRS:
    if not (VAULT / d).exists():
        error(f"Diretório ausente: {d}")

# Check required data files
for f in REQUIRED_DATA:
    if not (VAULT / "data" / f).exists():
        error(f"Arquivo de dados ausente: data/{f}")

# Check YAML validity
for yaml_file in (VAULT / "data").glob("*.yaml"):
    try:
        data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
        if not data:
            warn(f"Arquivo YAML vazio: data/{yaml_file.name}")
    except yaml.YAMLError as e:
        error(f"YAML inválido: data/{yaml_file.name} — {e}")

# Check note frontmatter
for md_file in (VAULT / "notes").rglob("*.md"):
    content = md_file.read_text(encoding="utf-8")
    if not content.startswith("---"):
        warn(f"Nota sem frontmatter: {md_file.relative_to(VAULT)}")

print(f"Validação completa: {len(errors)} erros, {len(warnings)} avisos")
for e in errors: print(e)
for w in warnings: print(w)
