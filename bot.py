import os
import random
import discord
from discord.ext import commands
import datetime
dt = datetime.datetime.now()

from dotenv import load_dotenv
file_path = '.\mat_lista.txt'
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = '!', intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to {guild.name}'
    )

@client.command(name='mat', help='Visar maten för den angivna rotationen. 1-5 eller alla.')
async def mat(ctx, mat_vecka):
    with open(file_path,'r', encoding='utf-8') as mat_lista:
        mat_lista_data = [line.rstrip() for line in mat_lista]
        if mat_vecka == "1":
            response = ""
            for i in range(0,6):
                response += mat_lista_data[i]
                response += '\n'
            await ctx.send(response)
        elif mat_vecka == "2":
            response = ""
            for i in range(6,12):
                response += mat_lista_data[i]
                response += '\n'
            await ctx.send(response)
        elif mat_vecka == "3":
            response = ""
            for i in range(12,18):
                response += mat_lista_data[i]
                response += '\n'
            await ctx.send(response)
        elif mat_vecka == "4":
            response = ""
            for i in range(18,24):
                response += mat_lista_data[i]
                response += '\n'
            await ctx.send(response)
        elif mat_vecka == "5":
            response = ""
            for i in range(24,30):
                response += mat_lista_data[i]
                response += '\n'
            await ctx.send(response)
        elif mat_vecka == "alla":
            response = ""
            for i in mat_lista_data:
                response += i
                response += '\n'
            await ctx.send(response)

        else:
            response = 'Opps something went wrong, try enter a rotation number. You can do !help for help.'
            await ctx.send(response)

@client.command(name='week', help='Visar datum, tid, vecka och veckodag.')
async def week(ctx):
    #week = dt.strftime("%Y-%m-%d \n%H:%M \nVecka: %W \nVeckodag: %A")
    week = datetime.datetime.today().isocalendar()
    week = week[1]
    await ctx.send(week)

@client.command(name='smile',help='😎')
async def smile(ctx):
    smile = '😎'
    await ctx.send(smile)


client.run(TOKEN)