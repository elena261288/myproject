from pathlib import Path

MYPROJECT_DIR = Path(__file__).parent.parent.parent.resolve()
PAGES_DIR = MYPROJECT_DIR / "pages"
SRC_DIR = MYPROJECT_DIR / "src"
COUNTER = PAGES_DIR / "counter" / "counter.json"
SESSION = PAGES_DIR / "hello" / "session.json"
