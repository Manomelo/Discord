import os
import discord
from dotenv import load_dotenv



TOKEN = "NzYwODUyMTg1NzM0NzA5Mjk5.X3SE0Q.m4PTOiYJ6NWQlr5ZWQz_Pguo4No"

client = discord.Client()


@client.event
async def on_ready():
    print("{} ta on!".format(client.user))







client.run(TOKEN)