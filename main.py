from messages import M_handler
from happiness import Happiness
from hunger import Hunger
import discord
import os
import random
import threading
from discord import client
import requests
import json
from dotenv import load_dotenv

load_dotenv()
client=discord.Client()
hunger=Hunger(1000)
happiness=Happiness(1000)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  m_handler=M_handler(message)

  if message.content.startswith('$hello'):
    await message.channel.send('This message is sent form localhost')
  if message.content.startswith('$hunger'):
    await hunger_handler(m_handler)
  if message.content.startswith("$mood"):
    await mood_handler(m_handler)
    


async def hunger_handler(m_handler):
  if m_handler.content == "$hunger":
    await m_handler.send(hunger.hunger)
  elif "how" in m_handler.content:
    await m_handler.send(hunger.throw_hunger_message())

async def mood_handler(m_handler):
  if "feed" in m_handler.content :
    hunger.add_hunger(20)
    happiness.add_happiness(10)
    await m_handler.send("'Back to happy! (•ө•)♡'")
  
  if "praise" in m_handler.content:
    happiness.add_happiness(20)
    await m_handler.send('Happiness reloaded! (　＾Θ＾)❤️')


client.run(os.getenv ('TOKEN'))
