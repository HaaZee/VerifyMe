import discord
from discord import Game, Embed
import subprocess
import json
import os
import STATICS
from commands import cmd_verify, cmd_help

client = discord.Client()

commands = {

    "verify": cmd_verify,
    "help": cmd_help
}


@client.event
async def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    [(lambda s: print("  - %s (%s)" % (s.name, s.id)))(s) for s in client.servers]
    await client.change_presence(game=Game(name=".help"))

@client.event
async def on_message(message):

    if not message.author.bot:
        if message.content.startswith(STATICS.PREFIX):
            invoke = message.content[len(STATICS.PREFIX):].split(" ")[0]
            args = message.content.split(" ")[1:]
            if commands.__contains__(invoke):
                await commands.get(invoke).ex(args, message, client, invoke)
            else:
                await client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=("The command `%s` is not valid!" % invoke)))

client.run(os.environ['TOKEN'])
