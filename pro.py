import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "U!", description = "Bot de Urania")

@bot.event
async def on_ready():
	print("Ready !")

async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")

@bot.command()
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    mutedRole = await getMutedRole(ctx)
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")
@bot.command()
async def coucou(ctx):
	await ctx.send("Coucou !")

@bot.command()
async def serverinfo(ctx):
	server = ctx.guild
	numberOfTextChannels = len(server.text_channels)
	numberOfVoiceChannels = len(server.voice_channels)
	serverDescription = server.description
	numberOfPerson = server.member_count
	serverName = server.name
	message = f"Le serveur **{serverName}** contient **{numberOfPerson}** personnes ! \nLa description du serveur est **{serverDescription}**. \nCe serveur possède **{numberOfTextChannels}** salons écrit et **{numberOfVoiceChannels}** salon vocaux."
	await ctx.send(message)

bot.run("ODI5NTExNTI2NzY3NTI1OTA4.YG5Mzw.VaOIcNb99o4sN_ggfO7uR7sfMFk")