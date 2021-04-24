import discord
import asyncio
#from webserver import keep_alive
import os
import random
from discord.ext import commands

class Bcommands(commands.Cog):


	def __init__(self , client):
		self.client = client


	@commands.command()

	async def cook(self , ctx):

		await ctx.send('Hey there!')


	@commands.command()
	async def sed(self , ctx):
		await ctx.send('bery sed\nso cruel\nSuch sedness\n~Aayush 2021')


	@commands.command(case_insensitive=True , aliases=['Cball', '8ball', 'cb', 'Cb', 'CB'])
	#, aliases = ['Cball'  , '8ball' , 'cb', 'Cb', 'CB']
	async def Codeball(self , ctx, *, question=None):
		if question == None:
		    await ctx.send(f"Ask a question {random.choice(['pls' , 'sweetie' , 'dude'])} {random.choice([':)' , ':>'])}")
		    return

		responses = ['It is certain that this must happen', 'Without a doubt son',
		'You must work on it', 'Yes definitely, after all you are a coder!',
		'Yes :) fate has decided so', 'Most likely', 'Plagiarism is a big NO!',
		'Signs point to yes', "I'm busy cooking , ttyl",
		'Let me ask Chef and tell you', 'Practice on it  and  ask me again',
		"Don't count on plagiarism silly",
		"I don't know  , you are the coder not me!", 'Hmmm good question',
		'Very doubtful', 'Let me check the documentation for that...',
		'Um actually , no :)']

		await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')



def setup(client):
	client.add_cog(Bcommands(client))
