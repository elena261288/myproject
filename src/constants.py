from pathlib import Path
import os


PORT = int(os.getenv("PORT", 8000))  # задает адрес нашего локал хоста
MYPROJECT_DIR = Path(__file__).parent.parent.resolve()
PAGES_DIR = MYPROJECT_DIR/"pages"
SRC_DIR = MYPROJECT_DIR/"src"
COUNTER = SRC_DIR/"counter.json"
