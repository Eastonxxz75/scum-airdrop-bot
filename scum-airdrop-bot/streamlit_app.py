# File: streamlit_app.py

import streamlit as st
import os
from utils.bank import get_balance, deposit_currency
from packs.pack_loader import load_pack
from utils.rcon import send_rcon_command

RCON_HOST = os.getenv("RCON_HOST", "83.223.203.32")
RCON_PORT = int(os.getenv("RCON_PORT", 28616))
RCON_PASSWORD = os.getenv("RCON_PASSWORD", "YOUR_PASSWORD")

st.set_page_config(page_title="🪂 Gneis Co Airdrop Control", layout="wide")
st.title("🪂 Gneis Co Airdrop Admin Panel")

st.sidebar.header("Login")
admin_password = st.sidebar.text_input("Admin password", type="password")

if admin_password != os.getenv("ADMIN_PASSWORD", "gneisrockz"):
    st.warning("Please enter a valid admin password to continue.")
    st.stop()

st.success("✅ Logged in as admin")

st.header("📦 Manual Airdrop")
user_id = st.text_input("Enter Discord User ID or Steam ID")
pack_name = st.selectbox("Select Pack", os.listdir("packs"))

if st.button("Deploy Airdrop"):
    if not user_id:
        st.error("Please enter a user ID.")
    else:
        pack = load_pack(pack_name.replace(".py", ""))
        if not pack:
            st.error("Could not load pack.")
        else:
            success = True
            for item in pack:
                cmd = f"#SpawnItem {item} 1 {user_id}"
                if not send_rcon_command(RCON_HOST, RCON_PORT, RCON_PASSWORD, cmd):
                    success = False
            if success:
                st.success("Airdrop deployed!")
            else:
                st.error("Error deploying airdrop.")

st.header("💰 Bank Manager")
uid = st.text_input("Check User ID Balance")
if uid:
    st.info(f"💰 Balance for {uid}: {get_balance(uid)} credits")
    add_amt = st.number_input("Deposit amount", step=1)
    if st.button("Deposit"):
        deposit_currency(uid, add_amt)
        st.success(f"Deposited {add_amt} credits to {uid}")
