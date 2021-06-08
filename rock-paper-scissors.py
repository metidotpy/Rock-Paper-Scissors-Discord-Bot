import discord
from discord import player
from discord import colour
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import random

GAMES=["rock","paper","scissors","rock","paper","scissors","paper","paper","paper","rock","scissors","rock","paper","rock","scissors","scissors","rock","rock","rock","scissors","paper"]


client=commands.Bot(command_prefix=">>", help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=">>help"))
    print("We Are Ready Now")

@client.command(name="help")
async def _help(ctx):
    embed=discord.Embed(
        name="Help Commands"
    )
    embed.add_field(
        name="Play A Game",
        value="**`play [your move]`**, **`p [your move]`**, **`game [your move]`**",
        inline=False
    )
    embed.set_author(name=ctx.author.name,icon_url=ctx.author)
    embed.set_footer(text=f"Requested By {ctx.author}",icon_url=ctx.author.avatar_url)

@client.command(name="play",aliases=["p","game"],pass_context=True)
async def _play(ctx,move):
    computer=random.choice(GAMES)
    embed=discord.Embed(
        name="Moves",
        colour=discord.Color.dark_grey()
    )

    if move.lower() not in ["rock","paper","scissors"]:
        await ctx.send("You Should Use [**`rock`**,**`paper`**,**`scissors`**]")
    
    if move.lower() == "rock":
        if computer == "scissors":
            res=(f"{ctx.author.mention} Wins!")
        elif computer == "paper":
            res=("<@851920383723831356> Wins!")
    elif move.lower == "paper":
        if computer == "rock":
            res=(f"{ctx.author.mention} Wins!")
        elif computer == "scissors":
            res=("<@851920383723831356> Wins!")
    elif move.lower() == "scissors":
        if computer == "paper":
            res=(f"{ctx.author.mention} Wins!")
        elif computer == "rock":
            res=("<@851920383723831356> Wins!")
    else:
        await ctx.send("Something Went Wrong!")

    embed.add_field(
        name="Players Moves",
        value=f"""
{ctx.author.mention} Choice => **{move}**,

<@851920383723831356> Choice => **{computer}**

**Result is:** => **{res}**

        """
    )
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.set_footer(text=f"Requested By {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_image(url="https://pxt.azureedge.net/blob/68f66c3ddc3acfc4c53157abf92eace202d46db2/static/courses/csintro/conditionals/rock-paper-scissors-items.png")
    await ctx.send(embed=embed)


@_play.error
async def _play_error(ctx, error):
    if isinstance(error,commands.MissingRequiredArgument):
        print("We Have An Error, Missing Bad Arguments")
        await ctx.send("Please Compelete Required Argument")
    elif isinstance(error,commands.BadArgument):
        print("We Have An Error, Bad Argument")
        await ctx.send("Bad Arguments")

client.run("ODUxOTIwMzgzNzIzODMxMzU2.YL_Srw.pXcWBWE26d1yC8JSIOl1ODYvM9E")