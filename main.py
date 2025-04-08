import discord
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN'

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!!", intents=intents)

@bot.command(name='pin')
async def pin_message(ctx, target: str = None):
    if target:
        if target.startswith('http'):
            try:
                message_id = int(target.split('/')[-1])
                channel_id = int(target.split('/')[-2])
                channel = bot.get_channel(channel_id)
                message = await channel.fetch_message(message_id)
            except:
                await ctx.send("Invalid URL")
                return
        else:
            try:
                message_id = int(target)
                message = await ctx.channel.fetch_message(message_id)
            except:
                await ctx.send("Invalid message ID")
                return
    else:
        async for message in ctx.channel.history(limit=2):
            if message.id != ctx.message.id:
                break

    try:
        await message.pin()
        await ctx.send("Pinner!")
    except discord.Forbidden:
        await ctx.send("No pinning permissions")
    except discord.HTTPException:
        await ctx.send("Failed pinner")

@bot.command(name='unpin')
async def unpin_message(ctx, target: str):
    if target.startswith('http'):
        try:
            message_id = int(target.split('/')[-1])
            channel_id = int(target.split('/')[-2])
            channel = bot.get_channel(channel_id)
            message = await channel.fetch_message(message_id)
        except:
            await ctx.send("Invalid URL")
            return
    else:
        try:
            message_id = int(target)
            message = await ctx.channel.fetch_message(message_id)
        except:
            await ctx.send("Invalid message ID")
            return
    try:
        await message.unpin()
        await ctx.send("Unpinnd!")
    except discord.Forbidden:
        await ctx.send("No unpinning permissions")
    except discord.HTTPException:
        await ctx.send("failed unpin")

bot.run(TOKEN)