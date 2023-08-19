from Hero.database import udb

# ... (other imports and code)

def addpoke(user_id, poke_id, poke_name):
    data = udb.find_one({"_id": user_id})
    if data:
        udb.update_one({"_id": user_id}, {"$push": {"heros": [poke_id, poke_name]}})
    else:
        register(user_id)
        addpoke(user_id, poke_id, poke_name)


def addpokefav(user_id, poke_id):
    hm = 2  # Placeholder for your implementation


def checkpoke_trade(poke_id, user_id):
    poke_id = int(poke_id)
    user_id = int(user_id)
    data = udb.find_one({"_id": user_id})
    if data:
        pokes = data["heros"]
        for poke in pokes:
            if poke_id in poke:
                return True, poke[1]
    
    return False, None


def poke_trade(poke1, pokename1, user1, poke2, pokename2, user2):
    poke1 = int(poke1)
    user1 = int(user1)
    poke2 = int(poke2)
    user2 = int(user2)
    
    udb.update_one({"_id": user1}, {"$push": {"heros": [poke2, pokename2]}})
    udb.update_one({"_id": user2}, {"$push": {"heros": [poke1, pokename1]}})
    
    udb.update_one({"_id": user1}, {"$pull": {"heros": [poke1, pokename1]}})
    udb.update_one({"_id": user2}, {"$pull": {"heros": [poke2, pokename2]}})

# ... (other functions remain the same)
