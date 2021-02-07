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
hunger=Hunger(100)
happiness=Happiness(100)


@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  m_handler=M_handler(message)

  if message.content.startswith('$hello'):
    await message.channel.send('Helloooooo!!')
  if message.content.startswith('$hunger'):
    await hunger_handler(m_handler)
  if message.content.startswith("$mood"):
    await mood_handler(m_handler)
    


async def hunger_handler(m_handler):
  if m_handler.content == "$hunger":
    await m_handler.send(round(hunger.hunger))
  elif "how" in m_handler.content:
    await m_handler.send(hunger.throw_hunger_message())


async def mood_handler(m_handler):
  if "feed" in m_handler.content :
    hunger.add_hunger(20)
    happiness.add_happiness(10)
    await m_handler.send('Back to happy! (•ө•)♡')
  elif "how" in m_handler.content:
    await m_handler.send(round(happiness.happiness))
    await m_handler.send
  elif "praise" in m_handler.content:
    happiness.add_happiness(20)
    await m_handler.send('Happiness reloaded! (　＾Θ＾)❤️')

  elif "scold" in m_handler.content:
    happiness.add_happiness(-15)
    await m_handler.send('Sad... ( ˘⊖˘)')
  
  elif "meme face" in m_handler.content:
    happiness.add_happiness(5)
    await m_handler.send('ლ(◉◞⊖◟◉｀ლ)')

  elif "sit" in m_handler.content:
    happiness.add_happiness(5)
    await m_handler.send('Plops down* ϵ( •Θ• )϶')
  
  elif "walk" in m_handler.content:
    happiness.add_happiness(10)
    await m_handler.send('walks* ⋋(‘Θ’◍)⋌ :.。✯*')

  elif "cry" in m_handler.content:
    happiness.add_happiness(-10)
    await m_handler.send('Wuuuu~* ( ⌒⃘ ◞⊖◟ ⌒⃘ )')
  elif "stand" in m_handler.content:
    happiness.add_happiness(10)
    await m_handler.send('Stands up!* ㄟ( •ө• )ㄏ')
  elif "fetch" in m_handler.content:
    happiness.add_happiness(20)
    await m_handler.send('⚽є(･Θ･｡)э››')
  elif "tantrum" in m_handler.content:
    await m_handler.send(happiness.throw_tantrum())
  elif "poop" in m_handler.content:
    await m_handler.send('(⊙ө⊙)💩')
    hunger.add_hunger(-10)
  elif "feel" in m_handler.content:
    await m_handler.send(happiness.rand_mood())
  elif "compliment" in m_handler.content:
    await m_handler.send('https://media.giphy.com/media/3o7btREha9GkGtgJKo/giphy.gif')
  elif "disgotchi" in m_handler.content:
    await m_handler.send('I am here! ヾ(・Θ・)ノ')



client.run(os.getenv ('TOKEN'))
