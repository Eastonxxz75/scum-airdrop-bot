# Project: SCUM Airdrop Bot (Gneis Co)
# File: bot.py (Main bot logic)

import discord
from discord.ext import commands, tasks
import asyncio
import random
import json
import os
from utils.rcon import send_rcon_command
from utils.bank import get_balance, deposit_currency
from utils.cooldowns import is_on_cooldown, set_cooldown
from utils.messages import get_random_system_message
from packs.pack_loader import load_pack
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
RCON_HOST = os.getenv("RCON_HOST")
RCON_PORT = int(os.getenv("RCON_PORT"))
RCON_PASSWORD = os.getenv("RCON_PASSWORD")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    broadcast_random_message.start()

@tasks.loop(hours=3)
async def broadcast_random_message():
    channel_id = int(os.getenv("SYSTEM_MESSAGE_CHANNEL_ID"))
    channel = bot.get_channel(channel_id)
    if channel:
        message = get_random_system_message()
        await channel.send(message)

@bot.command()
async def help(ctx):
    user_id = str(ctx.author.id)
    if is_on_cooldown(user_id, "help", 3600):
        await ctx.send("⏳ Help is on cooldown. Try again later.")
    else:
        cmd = f"#SpawnItem Bandage_Dressing 1 {ctx.author.name}"
        send_rcon_command(RCON_HOST, RCON_PORT, RCON_PASSWORD, cmd)
        set_cooldown(user_id, "help")
        await ctx.send("🩹 Emergency bandage airdropped!")

@bot.command()
async def drop(ctx, pack_name: str):
    pack = load_pack(pack_name)
    if not pack:
        await ctx.send("❌ Invalid pack name.")
        return
    for item in pack:
        cmd = f"#SpawnItem {item} 1 {ctx.author.name}"
        send_rcon_command(RCON_HOST, RCON_PORT, RCON_PASSWORD, cmd)
    await ctx.send(f"🪂 {pack_name.title()} pack inbound!")

@bot.command()
async def balance(ctx):
    bal = get_balance(str(ctx.author.id))
    await ctx.send(f"💰 Your balance: {bal} SCUM Bucks")

@bot.command()
async def deposit(ctx, amount: int):
    if amount <= 0:
        await ctx.send("❌ Invalid amount.")
        return
    deposit_currency(str(ctx.author.id), amount)
    await ctx.send(f"✅ Deposited {amount} SCUM Bucks")

@bot.command()
async def daily(ctx):
    user_id = str(ctx.author.id)
    if is_on_cooldown(user_id, "daily", 86400):
        await ctx.send("⏳ Daily bonus already claimed.")
    else:
        cmd = f"#SpawnItem Cal_22_Ammobox 1 {ctx.author.name}"
        send_rcon_command(RCON_HOST, RCON_PORT, RCON_PASSWORD, cmd)
        cmd2 = f"#SpawnItem Canned_Beef_Goulash 1 {ctx.author.name}"
        send_rcon_command(RCON_HOST, RCON_PORT, RCON_PASSWORD, cmd2)
        set_cooldown(user_id, "daily")
        await ctx.send("📦 Daily drop delivered!")

bot.run(TOKEN)
