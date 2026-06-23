# 🎮 SBURB SESSION 4-PLAYER DISCORD BOT — STEAMPECK SETUP

## What This Does
You now have a fully functional Homestuck-themed Discord bot that:
- Tracks 4-player character archetypes (Kamryn, Taylor, Geo, [REDACTED])
- Simulates an Alchemy/Grist economy
- Maintains Pesterlog chat history
- Provides immersive role-based commands
- Runs on your SteamDeck in Desktop Mode

---

## 🔧 INSTALLATION (SteamDeck Desktop Mode)

### Step 1: Open Terminal
Press `Ctrl+Alt+T` or open Konsole from the application menu.

### Step 2: Clone the Repository
```bash
cd ~/Desktop
git clone https://github.com/1AnLonelyMarionette/k.s.github.d.git
cd k.s.github.d
```

### Step 3: Create a Python Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Create Your `.env` File
```bash
cp .env.example .env
nano .env
```

Replace `your_token_here_from_developer_portal` with your actual Discord Bot Token (instructions below), then save:
- Press `Ctrl+X` → `Y` → `Enter`

---

## 🤖 GET YOUR DISCORD BOT TOKEN

### On Another Device (Browser):
1. Go to https://discord.com/developers/applications
2. Click **"New Application"** → name it anything (e.g., "Sburb")
3. Go to **"Bot"** section → click **"Add Bot"**
4. Under **TOKEN**, click **"Copy"**
5. Paste it into your `.env` file on the SteamDeck

### Set Up Bot Permissions:
1. In Developer Portal, go to **"OAuth2"** → **"URL Generator"**
2. Check these scopes: `bot` + `applications.commands`
3. Check these permissions:
   - ✅ Send Messages
   - ✅ Read Message History
   - ✅ Read Messages/View Channels
   - ✅ Manage Messages
4. Copy the generated URL and open it in your browser
5. Select your Discord server and authorize

### Final Discord Server Setup:
1. Go to your Discord server → **Settings** → **Roles**
2. Find the bot's role (same name as your bot)
3. **Drag it to the TOP** of the role list (above all other roles)
4. This prevents permission errors when bot tries to manage things

---

## ▶️ RUN THE BOT

### From Terminal:
```bash
# Make sure you're in the k.s.github.d directory
cd ~/Desktop/k.s.github.d

# Activate the virtual environment
source venv/bin/activate

# Run the bot
python .discord/bot.py
```

You should see:
```
✓ AN TREE: X SLASH COMMANDS SYNCHRONIZED GLOBALLY.
==================================================
✓ AN MASTER LOG: [BotName] IS LIVE ON STEAMOS
✓ Guild(s) connected: 1
✓ Bot ID: [numbers]
==================================================
```

---

## 🎮 COMMANDS

### Text Commands (prefix: `!`)
```
!session          — View all 4 players and their status
!pester [handle] [message]  — Add a message to Pesterlog
!dump             — Show recent Pesterlog entries
!grist            — Check Grist pool balance
```

### Slash Commands (type `/` in Discord)
```
/view_archetype [slot]  — View character data (slots 1-4)
/alchemize [item_a] [item_b]  — Combine two items
/stabilize_substrate [zone]  — Fix environmental drift (Admin only)
/access_void [key]  — Access Void Operator logs (Admin only)
```

**Void Operator Key:** `Pr0t0c0l_V01d_Unkn0wn!`

---

## 🔧 TROUBLESHOOTING

### "Bot won't start"
- Check that `.env` file exists in the k.s.github.d folder
- Verify your Discord token is correct and not expired
- Make sure `discord.py` and `python-dotenv` installed: `pip list`

### "Commands not showing up"
- Wait 1-2 minutes after bot starts
- Try typing `/` in Discord to see if they appear
- If not: restart bot, wait, try again

### "Permission denied" errors
- Check bot role is at TOP of role list in server settings
- Make sure bot has "Administrator" permissions if running admin commands

### "Token invalid or expired"
- Generate a new token from Developer Portal
- Update `.env` file with the new token
- Restart bot

---

## 🛑 STOP THE BOT

In terminal:
```bash
Ctrl+C
```

---

## 📁 FILE STRUCTURE

```
k.s.github.d/
├── .github/archetypes/     ← Character specs
│   ├── slot_01_kamryn.md
│   ├── slot_02_taylor.md
│   ├── slot_03_geo.md
│   └── slot_04_void.md
├── .discord/
│   └── bot.py              ← Main bot code
├── .env                    ← Your secret token (NEVER commit)
├── .env.example            ← Template
├── .gitignore              ← Prevents .env from uploading
├── requirements.txt        ← Python dependencies
└── SETUP_STEAMPECK.md      ← This file
```

---

## 🎯 NEXT STEPS

1. **Test the bot** in your Discord server
2. **Try all commands** to make sure they work
3. **Customize the archetypes** in `.github/archetypes/` if you want
4. **Add more players** by editing `SESSION_DATA` in `bot.py`
5. **Create Discord channels** for different zones if you want (e.g., #grist-exchange, #pesterlog)

---

**You're good to go.** 🎮♠️

If something breaks: check error messages, verify token, restart bot. Most issues resolve with a restart.
