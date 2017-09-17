import discord
import asyncio
from globalvars import *


async def get_help(message):
  em = discord.Embed(title='**HELP**',description=
  '''
__Key Commands__
  > `mbprefix <string>` - change the prefix from & to anything less than 5 characters. This variable is stored on a per-server level. This command does not use a prefix!
  > `$help` - get this page.
  > `$issue <text>` - send us an issue report.
  > `$blacklist <channel-name>` - block or unblock a channel from sending commands. If the bot has sufficient rights, it will also remove any commands in blacklisted channels.

__Management Commands__
  > `$autoclear <time (default: 10)> <channel (default: current)>` - set the channel to autoclear, deleting messages automatically after a certain amount of time.
  > `$clear` - wipe the entire message history of the current channel.
  '''
  )

  em2 = discord.Embed(description=
  '''

  **__FAQ__**
*What do I do if I blacklist all the channels?!*
  **__Don't panic!__** No, but seriously don't. Just make another text channel and then use the blacklist command again to un-blacklist (or as some may call, whitelist) the other channels. Simple :)

*What if the prefix gets set to a character that's difficult to access?*
  The `mbprefix` command doesn't require a prefix to access. Therefore, you can always easily change or reset the prefix.

*Why does the help command work even on blacklisted channels?*
  The help command functions on blacklisted channels so that users can still access important information, for example how to un-blacklist a channel.

*Do you have a place I can go to get more assistance?*
  Please join our Discord server :)

  https://discord.gg/WQVaYmT
  '''
  )

  await client.send_message(message.channel, embed=em)
  await client.send_message(message.channel, embed=em2)

  await client.add_reaction(message,'📬')
