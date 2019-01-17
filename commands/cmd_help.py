import discord

async def ex(args, message, client, invoke):

    verify = "**.verify** - Allows you to verify your account so you can participate in scrims."
    botinfo = "**.botinfo** - Prints info about VerifyMe."

    embed = discord.Embed(title="COMMANDS:", description=" ", color=0x00ff00)
    embed.add_field(name="__**Default Commands**__", value="\n{}\n{}".format(verify, botinfo), inline=True)
    embed.set_footer(text="Bot created by: HaZe#7197 ")

    await client.send_message(message.author, embed=embed)
