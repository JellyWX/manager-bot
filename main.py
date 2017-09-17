import discord
import asyncio
import time
from sys import argv, executable

from globalvars import *

from get_help import get_help
from change_prefix import change_prefix
from add_blacklist import add_blacklist
from create_issue import create_issue
from autoclear import autoclear
from clear_channel import clear_channel


async def blacklist_msg(message):
  msg = await client.send_message(message.channel, ':x: This text channel has been blacklisted :x:')
  await client.delete_message(message)
  await asyncio.sleep(2)
  await client.delete_message(msg)

command_map = {
  'help' : get_help,
  'blacklist' : add_blacklist,
  'suggestion' : create_issue,
  'issue' : create_issue,
  'autoclear' : autoclear,
  'clear' : clear_channel
}

async def validate_cmd(message):
  if message.server != None and message.server.id in prefix.keys():
    pref = prefix[message.server.id]
  else:
    pref = '&'

  if message.content[0] != pref: ## These functions call if the prefix isnt present
    if message.content.startswith('mbprefix'):

      if message.channel.id in channel_blacklist:
        await blacklist_msg(message)
        return

      await change_prefix(message)

    return

  cmd = message.content.split(' ')[0][1:] # extract the keyword
  if cmd in command_map.keys():

    if message.channel.id in channel_blacklist and cmd != 'help':
      await blacklist_msg(message)

      return

    else:
      await command_map[cmd](message)

      return

@client.event ## print some stuff to console when the bot is activated
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): ## when a message arrives at the bot ##

  if message.content in [None, '']:
    return

  await validate_cmd(message)

  if message.channel.id in autoclears.keys():
    await asyncio.sleep(autoclears[message.channel.id])
    await client.delete_message(message)

  if message.author.id in users.keys():
    if time.time() - users[message.author.id] < 0.75:
      print('quick message time...')

      if message.author.id in warnings.keys():
        print('user already has a warning.....')

        warnings[message.author.id] += 1
        if warnings[message.author.id] == 3:
          await client.send_message(message.channel, 'Please slow down {}'.format(message.author.mention))

        elif warnings[message.author.id] == 5:

          overwrite = discord.PermissionOverwrite()
          overwrite.send_messages = False
          await client.edit_channel_permissions(message.channel, message.author, overwrite)
          await client.send_message(message.channel, '{}, you\'ve been muted!'.format(message.author.mention))

      else:
        print('user added to warning list')
        warnings[message.author.id] = 1

      users[message.author.id] = time.time()

    else:
      print('long delay. user was removed from muting.')
      users[message.author.id] = time.time()
      warnings[message.author.id] = 0

  else:
    print('registered user for auto-muting')
    users[message.author.id] = time.time()

try:
  with open('token','r') as token_f:
    token = token_f.read().strip('\n')

except FileNotFoundError:
  if len(argv) < 2:
    print('Please remember you need to enter a token for the bot as an argument, or create a file called \'token\' and enter your token into it.')
  else:
    token = argv[1]

else:
  try:
    client.run(token)
  except:
    print('Error detected. Restarting in 15 seconds.')
    time.sleep(15)

    os.execl(executable, executable, *argv)
