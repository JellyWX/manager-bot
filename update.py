import asyncio
import subprocess
import os
import sys

from globalvars import *

async def update(message):
  await client.change_presence(game=discord.Game(name='updating... hold on tight!'))

  print('Running pull...')
  subprocess.call(['git', 'pull'])

  print('Restarting now!')
  os.execl(sys.executable, sys.executable, *sys.argv)
