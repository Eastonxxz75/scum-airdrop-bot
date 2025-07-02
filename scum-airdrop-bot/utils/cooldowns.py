# File: utils/cooldowns.py

import json
import os
import time

COOLDOWN_FILE = "data/cooldowns.json"

def load_cooldowns():
    if not os.path.exists(COOLDOWN_FILE):
        return {}
    with open(COOLDOWN_FILE, "r") as f:
        return json.load(f)

def save_cooldowns(data):
    with open(COOLDOWN_FILE, "w") as f:
        json.dump(data, f, indent=2)

def is_on_cooldown(user_id, command, duration):
    data = load_cooldowns()
    now = time.time()
    if user_id in data and command in data[user_id]:
        if now - data[user_id][command] < duration:
            return True
    return False

def set_cooldown(user_id, command):
    data = load_cooldowns()
    if user_id not in data:
        data[user_id] = {}
    data[user_id][command] = time.time()
    save_cooldowns(data)
