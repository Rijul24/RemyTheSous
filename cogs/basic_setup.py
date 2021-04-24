import discord
import asyncio
#from webserver import keep_alive
import os
import random
from discord.ext import commands

class Ready(commands.Cog):


	def __init__(self , client):
		self.client = client

	@commands.Cog.listener()
	async def on_ready(self):
		await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you ;cook'), status=discord.Status.idle)

		print("Ready to cook.")


def setup(client):
	client.add_cog(Ready(client))
