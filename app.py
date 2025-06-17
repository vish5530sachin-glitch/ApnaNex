import os
from flask import Flask
from threading import Thread
from pyrogram import Client

# ---- Dummy web server for Render ----
app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Telegram Bot is Running!"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()

# ---- Telegram Bot Setup ----
API_ID = int(os.environ.get("API_ID", "15964777"))
API_HASH = os.environ.get("API_HASH", "ef448f85b780cdf26f8ffe390a5d8262")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

bot = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ---- Start the bot ----
bot.run()
