import discord
from discord.ext import commands

TOKEN = ''

bot = commands.Bot(command_prefix = '*')

@bot.event
async def on_ready():
  print('Connecté en tant que :')
  print(user.bot.name)
  print(user.bot.id)
  print('-------')
  
 

@bot.event
async def on_member_join(member):
  chnl = bot.get_channel(696785673289596948)
  await chnl.send('Bienvenue à toi {} sur le Seveur Evonia !'.format(member))

