import discord
import asyncio
#from webserver import keep_alive
import os
import random
from discord.ext import commands

class Modcommands(commands.Cog):


	def __init__(self , client):
		self.client = client

#moderation commands

	@commands.command()
	async def kick(self , ctx , member : discord.Member , * , reason= 'reason not specified.Ask moderators / admins'):
	    await member.kick(reason = reason)
	    await ctx.send(f'Kicked {member.mention} , Reason: {reason}')

	@commands.command()
	async def ban(self , ctx , member : discord.Member , * , reason= 'reason not specified.Ask moderators / admins'):
	    await member.ban(reason = reason)
	    await ctx.send(f'Banned {member.mention}')

	@commands.command()
	async def clear(self , ctx , amount = 2):
	    await ctx.channel.purge(limit = amount)

	@commands.command()
	async def unban(self , ctx , * , member):
	    banned_users = await ctx.guild.bans()
	    #creates a tuple for banned users + reasons
	    member_name , member_disc = member.split('#')

	    for ban_entry in banned_users:
	        user = ban_entry.user

	        if (user.name , user.discriminator) == (member_name , member_disc):
	            await ctx.guild.unban(user)
	            await ctx.send(f'Unbanned {user.mention}')
	            return








def setup(client):
	client.add_cog(Modcommands(client))
