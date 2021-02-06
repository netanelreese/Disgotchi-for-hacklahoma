import discord
import os
import random
import threading
import requests
import json

class MyClient(discord.Client):

  async def on_ready(self):
      print('Logged on as', self.user)
async def on_message(self, message):
      word_list = ['cheat', 'cheats', 'hack', 'hacks', 'internal', 'external', 'ddos', 'denial of service']

      # don't respond to ourselves
      if message.author == self.user:
          return

      messageContent = message.content
      if len(messageContent) > 0:
          for word in word_list:
              if word in messageContent:
                  await message.channel.send('Do not say that!')
client = MyClient()
client.run(os.getenv ('TOKEN') )


#variables for disgotchi things, halfway implemented, hunger and happiness decays now - Nate
happiness = 0
hunger = 0;
disclipline = 0;

######## Plot ##########
# A new Disgotchi egg has arrived! Would you like to open it? (Y/N)
# Congratulations! Your Disgotchi is hatched! (Play around? : Y/N)
# Your Disgotchi is hungry. Would you like to feed it? (Y/N)
# Your Disgotchi is taking a nap! If you want to play around with it, you can wake it up (Hey/Disgotchi)
# Your Disgotchi needs to exercise. Would you scold it(1) or do excercise together(2)? (1/2)

# TODO Take the user input and convert it to all-lowercase-letters!

@client.event
async def on_ready ():
  print('We have logged in as {0.user}'.format(client))
  reduce_happiness()
  decay_hunger()
 
@client.event
async def on_ready():
   print('We have logged in as {0.user}'.format(client))

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)



client.run(os.getenv ('TOKEN') )

@client.event
async def on_message(message):
 
  if message.author == client.user:
    return
  
@client.event
async def on_message(message):
    if message.author == client.user:
      return
    if message.content.startswith('Hello'):
      await message.channel.send('Hello!')
    if message.content.startswith('compliment me'):
      await message.channel.send('https://media.giphy.com/media/3o7btREha9GkGtgJKo/giphy.gif')
    if message.content.startswith('who are you'):
      await message.channel.send('I am a discord tamagotchi bot, you can call me Disgotchi (・Θ・) ')
    if message.content.startswith('Disgotchi!'):
      await message.channel.send('I am here! ヾ(・Θ・)ノ' )
    if message.content.startswith('Good night Disgotchi'):
      await message.channel.send('Good night❤️ ϵ(＿⊖＿*)϶ Z z z ')
    if message.content.startswith('Feed'): 
      await message.channel.send('Back to happy! (•ө•)♡')
      happiness += 10
      hunger += 20
  # if message.content.startswith('Praise'):
  #   await message.channel.send('Happiness reloaded! (　＾Θ＾)❤️')
  #   happiness += 20
  # if message.content.startswith('Scold'):
  #   await message.channel.send('Sad... ( ˘⊖˘)')
  #   happiness -= 15
  #   disclipline += 10
  # if message.content.startswith('Gimme a meme face'):
  #   await message.channel.send('ლ(◉◞⊖◟◉｀ლ)')
  #   happiness += 5
  # if message.content.startswith('Sit'):
  #   await message.channel.send('Plops down* ϵ( •Θ• )϶')
  #   happiness += 5
  # if message.content.startswith('Walk'):
  #   await message.channel.send('walks* ⋋(‘Θ’◍)⋌ :.。✯*')
  #   happiness += 10
  # if message.content.startswith('Cry'):
  #   await message.channel.send('Wuuuu~* ( ⌒⃘ ◞⊖◟ ⌒⃘ )')
  #   happiness -= 10 
  # if message.content.startswith('Stand'):
  #   await message.channel.send('Stands up!* ㄟ( •ө• )ㄏ')
  # if message.content.startswith('Fetch'):
  #   await message.channel.send('⚽є(･Θ･｡)э››')
  # if message.content.startswith('Throw a tantrum'):
  #   await message.channel.send('Grrrr! o(｀Θ´)○')
  #   disclipline -= 10
    if message.content.startswith('Poop'):
      await message.channel.send('(⊙ө⊙)💩')
        
  # if message.content.startswith('how happy are you') or message.content.startswith ('how sad are you'): 

  #   if (happiness > 100 and happiness < 0):
  #     await message.channel.send("I'm kind of sad ( ˘⊖˘) ♡♡♡♡")
  
  #   if (happiness >= 0 and happiness < 100):
  #     await message.channel.send("I'm alright ㄟ( ･ө･ )ㄏ ♡♡♡♡♡")
  
  #   if (happiness >= 100 and happiness < 200):
  #     await message.channel.send('Im pretty happy ˎ₍•ʚ•₎ˏ ♥♡♡♡♡')
  
  #   if (happiness >= 200 and happiness < 300):
  #     await message.channel.send("I'm happy (　＾Θ＾) ♥♥♡♡♡")
  
  #   if (happiness >= 300 and happiness < 400):
  #     await message.channel.send("I'm super happy! (•ө•)♡ ♥♥♥♡♡")
  
  #   if (happiness >= 400 and happiness < 500):
  #     await message.channel.send("I'm super happy! (•ө•)♡ ♥♥♥♥♡")
  
  #   if (happiness >= 500):
  #     await message.channel.send("I love you!! ♫.(◕∠◕).♫ ♥♥♥♥♥")
  # # Hungry
  # if message.content.startswith('are you hungry') or message.content.startswith('how hungry are you'):

  #   if(hunger > 100):
  #     await message.channel.send("I'm starving (＠◇＠)")
  #   elif(hunger > 80):
  #     await message.channel.send("I'm hungry | •́ ◇ •̀ |")
  #   elif(hunger > 60):
  #     await message.channel.send("You may feed me if you want to! ⸜₍๑•⌔•๑ ₎⸝")
  #   elif(hunger > 40):
  #     await message.channel.send("I am okay, thank you! ꜀( ˊ̠˂˃ˋ̠ )꜆")
  #   elif(hunger > 20):
  #     await message.channel.send("I am so full ＜(´ ՞)ਊ( ՞ )＞")
  #   elif(hunger > 0):
  #     await message.channel.send("I can starve for the rest of my life ＜(´ ՞)ਊ( ՞ )＞")
  #   else:
  #     await message.channel.send("I'm about to die from overeating..")
  # #indicate points
  # if message.content.startswith('/points'):
  #   await message.channel.send("My hungriness is: " + str(hunger) + "\n")
  #   await message.channel.send("My happiness is: " + str(happiness) + "\n")
  #   await message.channel.send("My discipline is: " + str(disclipline) + "\n")
      

def reduce_happiness():
  threading.Timer(1.0, reduce_happiness).start()
  global happiness
  if(happiness>5):
    happiness*=0.96
  
def decay_hunger(): #reusing chinmay's code to decay hunger over time
  threading.Timer(1.0, decay_hunger).start()
  global hunger
  if(hunger > 10):
    hunger*=0 

def random_mood():
  async def on_message(message):
    mood = random.randomint(0, 4)

    if mood == 0:
      await message.channel.send('Grumpy (｀Θ´)' ) 
    elif mood == 1:
      await message.channel.send('Down... ( ˘⊖˘)')
    elif mood == 2:
      await message.channel.send('Happy!! (•͈⌔•͈⑅)')
    elif mood == 3:
      await message.channel.send('Excited!!! ヽ(○･▽･○)ﾉﾞ')
    if message.content.includes('happy, sad, angry, grumpy' ):
      message.reply('Mood')


  
client.run(os.getenv ('TOKEN') )

