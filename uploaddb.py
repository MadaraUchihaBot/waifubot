from database import pokedb

def upload_pokemon(pokemon_img, pokemon_id, pokemon_name):
    pokemon_id = int(pokemon_id)
    data = {
        "_id": pokemon_id,
        "name": pokemon_name,
        "img": pokemon_img
    }
    pokedb.insert_one(data)
