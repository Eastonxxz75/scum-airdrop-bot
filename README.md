# 🪂 Gneis Co Airdrop Bot – Your Chaos, Delivered

**Unleash tactical madness with a button.**  
The Gneis Co Airdrop Bot is a fully automated, player-driven loot system built for SCUM servers that don’t take themselves too seriously—but still want elite tools.

Whether you're begging for an emergency bandage, cashing in your daily login bonus, or calling down the absurdly powerful *Unhinged Mystery Pack™*, this bot is built to deliver.

---

## 🎮 Features

- 🛠️ **Self-Serve Airdrops**  
  Players can select from pre-made packs or custom loadouts using Discord commands or a future player dashboard.

- 💰 **Bank & Currency System**  
  Earn money, deposit/withdraw, and buy airdrops. Daily login streaks give bonuses.

- ⏱️ **Cooldown & Abuse Control**  
  Commands like `!help` are restricted to once/hour per player to maintain balance and hilarity.

- 🧠 **Streamlit Admin Dashboard**  
  Admins get a clean, password/Steam-locked UI for managing packs, triggering events, editing system messages, and more.

- 🧼 **400+ System Messages**  
  Sent every 3 hours via in-game RCON. Most are funny. 1% are awkward. 1% are disturbingly medical.

- 🎭 **Steam Login Integration**  
  All player commands are tied to their Steam64 ID using OAuth, ensuring safe tracking and cool future features.

- 🧟 **Event Triggers**  
  Admins can initiate custom missions (like “Weed Drop at Police Station”) guarded by puppets/NPCs for massive loot.

---

## 🚀 Quick Start

### 📦 Requirements

- Python 3.10+
- PostgreSQL DB
- SCUM Server with RCON access
- Discord Bot Token
- Steam Web API Key

### 🔧 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Eastonxxz75/scum-airdrop-bot.git
   cd scum-airdrop-bot


scum-airdrop-bot/
│
├── bot.py                  # Main Discord bot logic
├── streamlit_app.py        # Streamlit admin/player dashboard
├── steam_login/            # Flask Steam OAuth backend
├── packs/                  # JSON loadouts and airdrop kits
├── utils/                  # DB, cooldown, RCON utilities
├── data/                   # Phrase pool, cooldowns
├── .env.example            # Template config
├── requirements.txt
└── README.md
