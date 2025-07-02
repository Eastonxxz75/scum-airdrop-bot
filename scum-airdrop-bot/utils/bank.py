# File: utils/bank.py

import json
import os

BANK_FILE = "data/bank.json"

def load_bank():
    if not os.path.exists(BANK_FILE):
        return {}
    with open(BANK_FILE, "r") as f:
        return json.load(f)

def save_bank(data):
    with open(BANK_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_balance(user_id):
    data = load_bank()
    return data.get(user_id, 0)

def deposit_currency(user_id, amount):
    data = load_bank()
    data[user_id] = data.get(user_id, 0) + amount
    save_bank(data)

def deduct_currency(user_id, amount):
    data = load_bank()
    if data.get(user_id, 0) >= amount:
        data[user_id] -= amount
        save_bank(data)
        return True
    return False
