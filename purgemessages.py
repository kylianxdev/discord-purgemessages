import discord
from discord.ext import commands

client = commands.Bot(command_prefix='/', intents=discord.Intents.all())

@commands.has_permissions(manage_messages=True)
@client.command(name='purge', brief='Deletes a specified number of messages from the current channel')
async def purge(ctx, amount: int):
  # Delete the specified number of messages
  deleted = await ctx.channel.purge(limit=amount)
  if len(deleted) == 0:
    # If no messages were deleted, create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    embed.description = 'No messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_thumbnail(url=ctx.author.avatar.url)
    # Send the embed message
    await ctx.send(embed=embed)
  else:
    # Create an embed message with a custom color and text
    embed = discord.Embed(title='Purge complete', color=0xFFFF00)
    if len(deleted) == 1:
      # If only one message was deleted, use singular text
      embed.description = '1 message was deleted'
    else:
      # If more than one message was deleted, use plural text
      embed.description = f'{len(deleted)} messages were deleted'
    # Set the user's profile picture as the thumbnail of the embed
    embed.set_thumbnail(url=ctx.author.avatar.url)
    # Send the embed message
    await ctx.send(embed=embed)

client.run('BOT_TOKEN')
