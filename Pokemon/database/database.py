from pymongo import MongoClient
from Pokemon.config.config import MONGODB_URL

# Create a MongoClient instance
client = MongoClient(MONGODB_URL)

# Access the 'pokemon_database' database
db = client.pokemon_database

# Access the 'users' collection
users_collection = db.users

def add_user(user_id, username, first_name, pokemon_data):
    new_user = {
        "user_id": user_id,
        "username": username,
        "first_name": first_name,
        "pokemon_data": pokemon_data
    }
    users_collection.insert_one(new_user)

def get_user(user_id):
    return users_collection.find_one({"user_id": user_id})

def get_pokemon_data(user_id):
    user = get_user(user_id)
    if user:
        return user.get("pokemon_data")
    return None

def update_pokemon_data(user_id, pokemon_data):
    users_collection.update_one({"user_id": user_id}, {"$set": {"pokemon_data": pokemon_data}})

def close_connection():
    client.close()
