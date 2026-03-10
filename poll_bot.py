import requests
import os
import sys
from datetime import datetime

# Читаем переменные окружения (секреты GitHub)
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

# Текст опроса (вы можете изменить под свои нужды)
QUESTION = "Отчёт о выходе на практику:"
OPTIONS = [
    "На рабочее место на предприятии.",
    "Дистанционно.",
    "На больничном, со справкой.",
    "Дата выхода на практику отложена предприятием.",
    "Другое."
]

def send_poll():
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Ошибка: не заданы BOT_TOKEN или CHAT_ID")
        sys.exit(1)

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": QUESTION,
        "options": OPTIONS,
        "is_anonymous": False,          # True, если хотите анонимный опрос
        "allows_multiple_answers": False # Разрешить только один ответ
    }

    try:
        # Используем json=data вместо data=data для корректной передачи списка опций
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()
        if result.get("ok"):
            print(f"✅ Опрос успешно отправлен в {datetime.now()}")
        else:
            print(f"❌ Ошибка Telegram API: {result}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка при отправке запроса: {e}")
        sys.exit(1)

if __name__ == "__main__":
    send_poll()
