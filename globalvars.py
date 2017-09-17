import discord
import asyncio
import json

client = discord.Client() ## defined the client

prefix = {}
channel_blacklist = []
autoclears = {}

try:
  with open('prefix.json','r') as f:
    prefix = json.load(f)

except FileNotFoundError:
  print('no prefix file found')

try:
  with open('autoclears.json','r') as f:
    autoclears = json.load(f)

except FileNotFoundError:
  print('no prefix file found')

try:
  with open('blacklist','r') as f:
    bl = f.read().strip('\n')
    bl = ''.join(bl)
    channel_blacklist = bl.split(',')

except FileNotFoundError:
  print('no blacklist file found')


for item in channel_blacklist:
  if len(item) < 3:
    channel_blacklist.remove(item)

print(channel_blacklist)
print(prefix)
