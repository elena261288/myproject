from pathlib import Path
import os


PORT = int(os.getenv("PORT", 8000))  # задает адрес нашего локал хоста
MYPROJECT_DIR = Path(__file__).parent.parent.resolve()
PAGES_DIR = MYPROJECT_DIR/"pages"
SRC_DIR = MYPROJECT_DIR/"src"
COUNTER = PAGES_DIR/"counter"/"counter.json"
SESSION = PAGES_DIR/"hello"/"session.json"
