import asyncio
import discord

from globalvars import *

async def clear_channel(message):
  await client.send_message(message.channel, 'ARE YOU SURE YOU WANT TO CLEAR THIS CHANNEL? (y/N)')
  t = await client.wait_for_message(author=message.author,channel=message.channel)

  if t.content[0].lower() == 'y':
    deletion_chunk = [1,2,3]
    while len(deletion_chunk) > 1:
      deletion_chunk = []
      async for message in client.logs_from(channel=message.channel,limit=100):
        deletion_chunk.append(message)

      try:
        await client.delete_messages(deletion_chunk)

      except:
        return
