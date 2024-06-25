import discord
from discord.ext import commands
import random, os, requests
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def checkAI(ctx):
    if ctx.message.attachments:
        for file in ctx.massage.attachments:
            namafile = file.filename()
            urlfile = file.url
            await file.save(f'./{namafile}')
            await ctx.send(f'gambar telah disimpan dengan nama {namafile}')

            #klasifikasi dan inferensi
            kelas, skor = get_class('keras_model.h5', 'labels.txt', namafile)

            if kelas == 'pet\n' and skor >= 0.75:
                await ctx.send('This is a Pet.')
                await ctx.send('A pet is an animal that lives with people.')
                await ctx.send('Pets are often kept for companionship and fun.')
                await ctx.send('Pets can often be trained to follow commands.')
                await ctx.send('Owners are responsible for the pet is well being.')

            elif kelas == 'wild\n' and skor >= 0.75:
                await ctx.send('This is a Wild animal.')
                await ctx.send('A wild animal lives in natural habitats like forests, oceans, and deserts.')
                await ctx.send('A wild animal finds its own food and shelter, and protects itself from dangers.')
                await ctx.send('A Wild animal behaves according to instincts, not human training.')
                await ctx.send('A Wild animal roams freely without human control.')

            else:
                await ctx.send('It is not a pet or a wild animal')
    else:           
        await ctx.send('where is the image??')


bot.run("token")
