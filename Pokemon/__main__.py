import asyncio
from pyrogram import Client, idle
from Pokemon.config.config import API_ID, API_HASH, BOT_TOKEN, DOWNLOAD_DIRECTORY, SUPPORT_CHAT
from Pokemon.database.database import load_db

async def load_start():
    # Your existing code for loading and starting
    pass

    app = Client(
        "NarutoBot",
        api_id=API_ID,
        api_hash=API_HASH,
        bot_token=BOT_TOKEN,
        workdir=DOWNLOAD_DIRECTORY,
        sleep_threshold=60,
        plugins={"root": "Pokemon.plugins"},
    )

    # Load the database and plugins
    load_db(app)

    # Send a message to the support chat upon bot startup
    try:
        with app:
            app.send_message(SUPPORT_CHAT, "Naruto Bot has started!\nDev: @SexyNano")
            print("Bot deployed successfully.")
    except Exception as e:
        print(f"Error sending startup message: {e}")
     
    app.run()
    idle() 
