import discord
from discord.ext import commands
from googletrans import Translator

languages = {"🇫🇷": "fr" , "🇲🇫": "fr" , "🇬🇧": "en" , "🇪🇸": "es", "🇪🇦":"es"}

intents = discord.Intents.default()
intents.reactions = True
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())
translator = Translator()


# logging in
@client.event
async def on_ready():
    await client.tree.sync()
    print(f"{client.user} initiated!")


# translation
@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji in languages.keys():
        try:
            translation = translator.translate(reaction.message.content, dest=languages.get(reaction.emoji))
            await reaction.message.channel.send(translation.text)
        except Exception as e:
            await reaction.message.channel.send(f"```Error when translating:{reaction.message.content}```")
    else:
        await reaction.message.channel.send(f"```Language not supported:{reaction.emoji}```")
        print(reaction.emoji)


client.run("YOUR TOKEN HERE")
