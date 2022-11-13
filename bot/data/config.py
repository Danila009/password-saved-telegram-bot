import os
from pathlib import Path


BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')
DATABASE_URL = os.environ.get('DATABASE_URL')

I18N_DOMAIN = "password_save_telegram_bot"
BASE_DIR = Path('main.py').parent
LOCALES_DIR = BASE_DIR / 'locales'
