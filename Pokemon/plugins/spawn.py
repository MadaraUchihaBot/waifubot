from pyrogram import Client, filters, app
import random
from Pokemon.database.database import add_user, get_pokemon_data, update_pokemon_data, close_connection

# Counter to keep track of messages
message_counter = 0

# List of Pokémon names and their corresponding image URLs
# List of Pokémon names and their corresponding image URLs
pokemon_data = [
    {"name": "Pikachu", "image_url": "https://example.com/pikachu.png"},
    {"name": "Charmander", "image_url": "https://example.com/charmander.png"},
    {"name": "Squirtle", "image_url": "https://example.com/squirtle.png"},
    {"name": "Bulbasaur", "image_url": "https://example.com/bulbasaur.png"},
    {"name": "Eevee", "image_url": "https://example.com/eevee.png"},
    # Add more Pokémon data here
]


@app.on_message(filters.text & ~filters.command)
def send_pokemon(client, message):
    global message_counter
    message_counter += 1

    if message_counter % 10 == 0:
        random_pokemon = random.choice(pokemon_data)
        user_id = message.from_user.id
        user_pokemon_data = get_pokemon_data(user_id)
        
        if user_pokemon_data is None:
            add_user(user_id, message.from_user.username, message.from_user.first_name, random_pokemon['name'])
        else:
            update_pokemon_data(user_id, random_pokemon['name'])
        
        message.reply_text(f"Random Pokémon: {random_pokemon['name']}")
        message.reply_photo(photo=random_pokemon['image_url'])
