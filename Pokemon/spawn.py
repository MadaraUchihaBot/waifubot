from pyrogram import Client, filters
import random

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual API ID and API hash
API_ID = 'YOUR_API_ID'
API_HASH = 'YOUR_API_HASH'

# Create a Pyrogram client
app = Client('my_bot', api_id=API_ID, api_hash=API_HASH)

# Counter to keep track of messages
message_counter = 0

# List of Pokémon names and their corresponding image URLs
pokemon_data = [
    {"name": "Pikachu", "image_url": "https://example.com/pikachu.png"},
    # Add more Pokémon data here
]

@app.on_message(filters.text & ~filters.command)
def send_pokemon(client, message):
    global message_counter
    message_counter += 1

    if message_counter % 10 == 0:
        random_pokemon = random.choice(pokemon_data)
        message.reply_text(f"Random Pokémon: {random_pokemon['name']}")
        message.reply_photo(photo=random_pokemon['image_url'])

# Start the Pyrogram client
app.run()
