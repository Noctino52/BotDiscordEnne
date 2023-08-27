import os
import random

import discord
from discord.ext import commands, tasks
import pyodbc
from dotenv import load_dotenv

load_dotenv(dotenv_path="token.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)
counter = 0


def db_conn():
    server = '136.243.15.120'
    database = 'master'
    username = 'sito'
    password = 'Y0K9h42j20Ek8M4C'
    cnxn = pyodbc.connect(
        'DRIVER=SQL Server;'
        'SERVER=' + server +
        ';DATABASE=' + database +
        ';UID=' + username +
        ';PWD=' + password
    )
    cursor = cnxn.cursor()
    return cursor


def query(cursor):
    cursor.execute("SELECT RegistrationIP FROM Enne.dbo.Account")
    row = cursor.fetchone()
    ip_address = []
    while row:
        ip_address.append(row[0])
        row = cursor.fetchone()
    return ip_address


async def pick_a_message(message):
    rnd = random.randint(1, 6)

    if rnd == 1:
        await message.channel.send("Hai qualche problema? manda un ticket https://discord.com/channels/993924008229752933/1051317241049780344")
    elif rnd == 2:
        await message.channel.send("Non riesci ad entrare in gioco? https://discord.com/channels/993924008229752933/1137687384960553040")
    elif rnd == 3:
        await message.channel.send("Sei un nuovo utente? Segui tutte le istruzioni su come iniziare a giocare https://discord.com/channels/993924008229752933/1109823763517808781")
    elif rnd == 4:
        await message.channel.send("Non scrivete in direct ad i GM! usa i ticket https://discord.com/channels/993924008229752933/1051317241049780344")
    elif rnd == 5:
        await message.channel.send("La vendita account è momentaneamente disattivata, aspettate nuove direttive per poter vendere il vostro account")
    elif rnd == 6:
        await message.channel.send("Usa la https://discord.com/channels/993924008229752933/1109804524429910016 per sapere tutti i segreti di Enne!")


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_message(message):
    global counter
    counter = counter + 1
    if message.author == bot.user:
        return
    print(counter)
    # Controlla se il messaggio è nel canale desiderato e soddisfa il conteggio dei messaggi
    if message.channel.id == 1092458091917881454 and counter == 12:
        counter = 0
        pick_a_message(message)


bot.run(TOKEN)
