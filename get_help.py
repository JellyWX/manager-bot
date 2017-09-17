import discord
import asyncio
from globalvars import *


async def get_help(message):
  await client.send_message(message.channel, 'I\'ve PM\'d you a list of commands')
  await client.send_message(message.author, '**HELP**')

  await client.send_message(message.author, '__Key Commands__')
  await client.send_message(message.author, '> `rbprefix <string>` - change the prefix from $ to anything less than 5 characters. This variable is stored on a per-server level. This command does not use a prefix!')
  await client.send_message(message.author, '> `$help` - get a PM of this page.')
  await client.send_message(message.author, '> `$issue <text>` - send us an issue report.')
  await client.send_message(message.author, '> `$blacklist <channel-name>` - Block or unblock a channel from sending commands. If the bot has sufficient rights, it will also remove any commands in blacklisted channels.')

  await client.send_message(message.author, '__Reminder Commands__')
  await client.send_message(message.author, '> `$remind <server/me> <time-to-reminder> <message>` - set up a reminder. Takes times in the format of \[num][s/m/h/d], for example 10s for 10 seconds, 2s10m for 2 seconds 10 minutes or 10m15s1h2d for 10 minutes, 15 seconds, 1 hour and 2 days.')
  await client.send_message(message.author, '> `$event <server/me> <date-and-time> <message` - set up an event. Takes times in the format of \[num]m[num]h[num]d[num]M[num]y, for example 0m0h31d12M2018y for 00:00 UTC on the 31st of December 2018.')
  await client.send_message(message.author, '**The difference between an event and a reminder is that an event is given an explicit time and date that it occurs, whereas a reminder acts more like a countdown timer for an amount of time you can specify.**')

  await client.send_message(message.author, '__Other Commands__')
  await client.send_message(message.author, '> `$etime` - get the current time in seconds.')
  await client.send_message(message.author, '> `$playing <string>` - set the \'Playing\' subtext.')
  await client.send_message(message.author, '> `$invite <URL>` - invite the bot to another server via URL.')
  await client.send_message(message.author, '> `$suggestion <text>` - send us a feature suggestion.')
  await client.send_message(message.author, '> `$transport_me` - PROTECT YOURSELF FROM ORANG AND THE VEGETALS.')


  await client.send_message(message.author, '**__FAQ__**')
  await client.send_message(message.author, '*What do I do if I blacklist all the channels?!*')
  await client.send_message(message.author, '**__Don\'t panic!__** No, but seriously don\'t. Just make another text channel and then use the blacklist command again to un-blacklist (or as some may call, whitelist) the other channels. Simple :)')

  await client.send_message(message.author, '*What if the prefix gets set to a character that\'s difficult to access?*')
  await client.send_message(message.author, 'The `rbprefix` command doesn\'t require a prefix to access. Therefore, you can always easily change or reset the prefix.')

  await client.send_message(message.author, '*Why does the help command work even on blacklisted channels?*')
  await client.send_message(message.author, 'The help command functions on blacklisted channels so that users can still access important information, for example how to un-blacklist a channel.')

  await client.send_message(message.author, '*Should I use `event` or `remind`?*')
  await client.send_message(message.author, 'To decide on this, consider: would you use a timer or a calendar to set the reminder? An event accepts a specific date and time as the argument, whereas a remind accepts the amount of time until the reminder, like a stopwatch.')

  await client.add_reaction(message,'📬')
