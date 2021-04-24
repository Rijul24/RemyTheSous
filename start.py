import discord
import asyncio
from webserver import keep_alive
import os
import random
from discord.ext import commands

client = commands.Bot(command_prefix=';')



@client.command()
async def load(ctx , extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx , extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx , extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')



'''


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching, name='you ;cook'),
                                 status=discord.Status.idle)

    print("Ready to cook.")
'''


#-------------------------------------------------------------------------------
'''
#moderation commands

@client.command()
async def kick(ctx , member : discord.Member , * , reason= 'reason not specified.Ask moderators / admins'):
    await member.kick(reason = reason)

@client.command()
async def ban(ctx , member : discord.Member , * , reason= 'reason not specified.Ask moderators / admins'):
    await member.ban(reason = reason)
    await ctx.send(f'Banned {member.mention}')

@client.command()
async def clear(ctx , amount = 2):
    await ctx.channel.purge(limit = amount)

@client.command()
async def unban(ctx , * , member):
    banned_users = await ctx.guild.bans()
    #creates a tuple for banned users + reasons
    member_name , member_disc = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name , user.discriminator) == (member_name , member_disc):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return





'''






'''

#here goes all commands----------------------------------------
@client.command()
async def cook(ctx):
    await ctx.send('Hey there!')


@client.command()
async def sed(ctx):
    await ctx.send('bery sed\nso cruel\nSuch sedness\n~Aayush 2021')


@client.command(case_insensitive=True,
                aliases=['Cball', '8ball', 'cb', 'Cb', 'CB'])
#, aliases = ['Cball' , '8ball' , 'cb', 'Cb', 'CB']
async def Codeball(ctx, *, question=None):
    if question == None:
        await ctx.send(
            f"Ask a question {random.choice(['pls' , 'sweetie' , 'dude'])} {random.choice([':)' , ':>'])}"
        )
        return

    responses = [
        'It is certain that this must happen', 'Without a doubt son',
        'You must work on it', 'Yes definitely, after all you are a coder!',
        'Yes :) fate has decided so', 'Most likely', 'Plagiarism is a big NO!',
        'Signs point to yes', "I'm busy cooking , ttyl",
        'Let me ask Chef and tell you', 'Practice on it  and  ask me again',
        "Don't count on plagiarism silly",
        "I don't know  , you are the coder not me!", 'Hmmm good question',
        'Very doubtful', 'Let me check the documentation for that...',
        'Um actually , no :)'
    ]

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

'''
#client run command-------------------------------------------------------------------------
keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

client.run(TOKEN)

#token links code to application , imp to keep safe
