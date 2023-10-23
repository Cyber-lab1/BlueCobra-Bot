import random

import discord
from discord.ext import commands
import Pass00wrd_Changer

intents = discord.Intents.default()
intents.typing = False
intents.message_content = True


bot = commands.Bot(command_prefix='!' , intents=intents)

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Don't count the days, make the days count. – Muhammad Ali",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt",
    "Life is really simple, but we insist on making it complicated. – Confucius",
    "The only thing standing between you and your goal is the story you keep telling yourself as to why you can't achieve it. – Jordan Belfort",
    "The best time to plant a tree was 20 years ago. The second best time is now. – Chinese Proverb",
    "The road to success and the road to failure are almost exactly the same. – Colin R. Davis",
]


@bot.event

async def on_ready():
    print(f"Logged in as {bot.user.name}")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

class InfoCog(commands.Cog, name='Info'):
    def __int__(self, bot):
        self.bot = bot


@bot.command(name='hello')
async def hello_command(ctx):
    await ctx.send('Hello, I am BlueCobra Bot I have Been Created By CyberShark Team!')


@bot.command(name='commands')
async def help_command(ctx, *args):
    if not args:
        command_list = [command.name for command in bot.commands]
        command_list_str = '\n'.join(command_list)
        await ctx.send(f"Available commands: \n ,,, {command_list_str} ,,,")
    else:
        command_name = args[0]
        command = bot.get_command(command_name)
        if command:
            await ctx.send(f"Usage: {command_name} {command.signature}\n{command.help}")
        else:
            await ctx.send("Command Not Found, It will be soon :)")

@bot.command(name='Info')
async def Info_command(ctx, user: discord.User):
    embed = discord.Embed(title=f"Information about {user.display_name}", color=discord.Color.blue())
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Username", value=user.name, inline=True)
    embed.add_field(name="Discriminator", value=user.discriminator, inline=True)
    embed.add_field(name="User ID", value=user.id, inline=False)
    await ctx.send(embed=embed)

class ModerationCog(commands.Cog, name='Moderation'):
    def __int__(self, bot):
        self.bot = bot

@Info_command.error
async def Info_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please provide a user to fetch information about it >>")


@bot.command(name='ping')
async def ping_command(ctx):
    lat = round(bot.latency * 1000)
    await ctx.send(f"Pong! Latency is {lat}ms")


@bot.command(name='quote')
async def quote_command(ctx):
    random_quote = random.choice(quotes)
    await ctx.send(f"Here \ s an inspirational or humorous quote: \n{random_quote}")


@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear_command(ctx, amount: int):
    try:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"Cleared {amount} messages.")
    except discord.Forbidden:
        await ctx.send("I don't have permission to delete message in this channel :(")
@clear_command.error
async def clear_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You don't have permissions")

@bot.command(name='change_password')
async def change_password_command(ctx):
    try:
        result = Pass00wrd_Changer.change_password()
        await ctx.send(f"Password changed successfully. Result: {result}")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        

bot.run("MTE2NjExMzI5MzYxODkxMzM2MQ.GGZmZw.LaihEEdA6cx2ckfxNcoSjVXNA-ISd0V1ob_owk")

