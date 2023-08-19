

@Client.on_message(filters.command("addpoke"))
async def add_pokemon_character(client, message):
    try:
        text = message.text.split(None, 1)[1]
        splitted = text.split(" ")
        poke_id = splitted[0]
        name = text.split(None, 1)[1]
        url = splitted[2]  # Use the URL provided in the command
    except:
        return await message.reply_text("format:\n`/addpoke (pokemon id) (name) (url)`")
    
    upload_pokemon(url, poke_id, name)
    await message.reply_text(f"Done!!\nID: {poke_id}\nName: {name}\nUrl: `{url}`")

@Client.on_message(filters.command("pokelist"))
async def pokelist(client, message):
    listt = get_list(pokedb)  # Replace pokedb with the appropriate database function
    
    if not listt:
        await message.reply_text("No Pokémon characters registered.")
        return
    
    ffile = "Pokémon List\n"
    ffile = "[x] - ID - Name - URL\n"  # Added "URL" header
    x = 0
    for obj in listt:
        x = x + 1
        ffile += f"[{x}] {obj['_id']} - {obj['name']} - {obj['url']}\n"  # Include URL
    
    with BytesIO(str.encode(ffile)) as output:
        output.name = "pokelist.txt"
        await message.reply_document(
            document=output,
            file_name="pokelist.txt",
            caption="Here is the Pokémon character list.",
        )



