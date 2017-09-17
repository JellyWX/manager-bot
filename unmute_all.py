import asyncio
import discord

from globalvars import *

async def unmute_user
  if not message.author.server_permissions.administrator:
    await client.send_message(message.channel, 'You must be an admin to run this command.')
    return
