import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------
# Intents
# ------------------------------
intents = discord.Intents.default()
intents.members = True          # Needed for kick/ban
intents.message_content = True  # Needed to read commands in server channels

# ------------------------------
# Create bot
# ------------------------------
client = commands.Bot(command_prefix='--', intents=intents, help_command=None)

# ------------------------------
# Bot Events
# ------------------------------
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Game('"--help" for commands')
    )
    print(f"Bot is online as {client.user}")

# ------------------------------
# Version Command
# ------------------------------
@client.command(name='version')
async def version(ctx):
    embed = discord.Embed(
        title="Current Version",
        description="The bot is in Version 1.0",
        color=0x00ff00
    )
    embed.add_field(name="Version Code:", value="v1.0.0", inline=False)
    embed.add_field(name="Date Released", value="February 14th, 2021", inline=False)
    embed.set_footer(text="Made by muiz_")
    embed.set_author(name="Muiz Bot")
    await ctx.send(embed=embed)

# ------------------------------
# Kick Command
# ------------------------------
@client.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No reason provided"):
    if member == ctx.author:
        return await ctx.send("You cannot kick yourself!")
    if not ctx.guild.me.guild_permissions.kick_members:
        return await ctx.send("I do not have permission to kick members!")

    # Try to DM the user first
    try:
        await member.send(f"You have been kicked from **{ctx.guild.name}**.\nReason: {reason}")
    except discord.Forbidden:
        await ctx.send(f"Could not DM {member.display_name} before kicking.")

    # Kick the user
    try:
        await member.kick(reason=reason)
        await ctx.send(f"User {member.display_name} has been kicked.")
    except Exception as e:
        await ctx.send(f"Failed to kick user: {e}")

    # Deletes the command message after 5 seconds after kicking the user
    await asyncio.sleep(5)
    await ctx.message.delete()
# ------------------------------
# Ban Command
# ------------------------------
@client.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No reason provided"):
    if member == ctx.author:
        return await ctx.send("You cannot ban yourself!")
    if not ctx.guild.me.guild_permissions.ban_members:
        return await ctx.send("I do not have permission to ban members!")

    # Try to DM the user first
    try:
        await member.send(f"You have been banned from **{ctx.guild.name}**.\nReason: {reason}")
    except discord.Forbidden:
        await ctx.send(f"Could not DM {member.display_name} before banning.")

    # Ban the user
    try:
        await member.ban(reason=reason)
        await ctx.send(f"User {member.display_name} has been banned.")
    except Exception as e:
        await ctx.send(f"Failed to ban user: {e}")

    # Deletes the command message after 5 seconds after banning the user
    await asyncio.sleep(5)
    await ctx.message.delete()
# ------------------------------
# Unban Command
# ------------------------------
@client.command(name ='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member: discord.User, reason="No reason provided"):
    if not ctx.guild.me.guild_permissions.ban_members:
        return await ctx.send("I do not have permission to unban members!")
    
    # Try to DM the user first
    try:
        await member.send(f"You have been unbanned from **{ctx.guild.name}**.\nReason: {reason}")
    except discord.Forbidden:
        await ctx.send(f"Could not DM {member.display_name} before unbanning.")

    # Try to unban the user
    try:
        await ctx.guild.unban(member)
        await ctx.send(f"User {member.display_name} has been unbanned.")
    except Exception as e:
        await ctx.send(f"Failed to unban user: {e}")
    
    # Deletes the command message after 5 seconds after unbanning the user
    await asyncio.sleep(5)
    await ctx.message.delete()
# ------------------------------
# Help Command
# ------------------------------
@client.command(name='help')
async def help_command(ctx):
    embed = discord.Embed(title="Muiz Bot Commands", color=0x00ff00)
    embed.add_field(name="--version", value="Tells info about the bot", inline=False)
    embed.add_field(name="--kick <user> [reason]", value="Kicks the mentioned user", inline=False)
    embed.add_field(name="--ban <user> [reason]", value="Bans the mentioned user", inline=False)
    embed.add_field(name="--help", value="Shows this help message", inline=False)
    embed.set_footer(text="Made by muiz_")
    embed.set_author(name="Muiz Bot")
    await ctx.send(embed=embed)

# ------------------------------
# Error Handling
# ------------------------------
@kick.error
@ban.error
async def perm_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permission to use this command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention a user to perform this action.")
    else:
        await ctx.send(f"An error occurred: {error}")

# ------------------------------
# Run the Bot
# ------------------------------
token = os.getenv('DISCORD_TOKEN')

if token is None:
    print("ERROR: DISCORD_TOKEN not found! Check your .env file.")
else:
    client.run(token)