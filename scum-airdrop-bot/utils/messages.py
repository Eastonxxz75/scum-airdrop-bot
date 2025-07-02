# File: utils/messages.py

import random
import os
import json

MESSAGES_FILE = "data/system_messages.json"

def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return [
            "☠️ You wake up covered in your own piss and regret.",
            "🔥 Someone lit the outhouse on fire again.",
            "💀 Ling pissed on my cut and I died two days later. -Easten",
            "🧠 You’re not hallucinating. The rocks *are* whispering.",
            "🥫 You traded your last can of food for a pack of gum. Worth it?"
        ]
    with open(MESSAGES_FILE, "r") as f:
        return json.load(f)

def get_random_system_message():
    messages = load_messages()
    return random.choice(messages)
