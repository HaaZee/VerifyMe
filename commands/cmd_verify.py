import discord
import asyncio
import requests
import json
import random
from discord.utils import get

async def ex(args, message, client, invoke):

    report_embed = discord.Embed(title="VerifyMe:" , color=discord.Color.green())
    report_embed.add_field(name="What to do: ", value="To verify your account so you can participate in RevengeEU scrims please respond with your STEAM64 ID.")
    report_embed.add_field(name="How?: ", value="*You can get this using https://steamidfinder.com/.*")
    report_embed.set_footer(text="NOTE: All profile settings must be set to public.")

    await client.send_message(message.author, embed=report_embed)

    author = message.author

    message = await client.wait_for_message(author=author)

    if message.server is None and message.author != client.user:

        steamid = message.content

        if steamid.isdigit() and len(steamid) == 17:

            await client.send_message(message.author, embed=discord.Embed(color=discord.Color.green(), description="Your verification request has gone through, you will be verified shortly."))

            url =  "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=721E1DBC94F54A914E9B0AE1250B1C5D&steamid={}&format=json".format(steamid)
            username_url =  "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=721E1DBC94F54A914E9B0AE1250B1C5D&steamids=76561198291339880&format=json"

            r = requests.get(url)
            r_user = requests.get(url)

            for game in r.json()['response']['games']:
                if game['appid'] == 433850:
                    minutes = game['playtime_forever']

            game_time = minutes / 60
            game_time = round(game_time, 1)

            verified = get(author.server.roles, name="Verified")
            unverified = get(author.server.roles, name="Unverified")
            verified_role = "Verified"
            verif_code = random.randint(1000000, 9000000)

            if verified_role.lower() not in [y.name.lower() for y in author.roles]:

                if game_time > 10:
                    await client.send_message(message.author, embed=discord.Embed(color=discord.Color.green(), description="To confirm the authenticity of this account, please add this verification code to your steam name: **{}**\n*Please reply to this message with 'done' once you have completed the task.*".format(verif_code)))
                    message = await client.wait_for_message(author=author)
                    if message.content.lower() == "done":

                        #['response']['players']
                        #for value in item:
                        #   if value == "personaname":
                        #       name = item[value]
                        for item in r_user.json():
                            print(item)


                        if verif_code in name:

                            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.green(), description="You are now verified. Have fun playing!"))
                            await client.add_roles(author, verified)
                    else:
                        await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Must reply with 'done'.\n *Verification closed, please retype the command in RevengeEU*"))


                else:
                    await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Sorry, your verifcation request was not approved. You will not be able to play RevengeEU scrims."))
                    await client.add_roles(author, unverified)

            else:
                await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="You are already verified."))

        else:
            await client.send_message(message.channel, embed=discord.Embed(color=discord.Color.red(), description="Must be STEAM64 ID.\n *Verification closed, please retype the command in RevengeEU*"))
