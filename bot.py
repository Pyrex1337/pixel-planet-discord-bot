import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from selenium import webdriver
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

gif = "https://media.discordapp.net/attachments/906960772788281367/1084810478104092732/ezgif.com-gif-maker_29.gif?width=320&height=320"

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(bot.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name="!yardim")
    await bot.change_presence(activity=activity)

@bot.command()
async def fb(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,6252,-8955,13')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)
    time.sleep(2)
    driver.save_screenshot('fb.png')
    driver.quit()

    file = discord.File('fb.png')
    await ctx.send(file=file)

@bot.command()
async def gs(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,5561,-7044,10')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)
    time.sleep(2)
    driver.save_screenshot('gs.png')
    driver.quit()

    file = discord.File('gs.png')
    await ctx.send(file=file)

@bot.command()
async def bjk(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,5746,-8977,10')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('bjk.png')
    driver.quit()

    file = discord.File('bjk.png')

    embed = discord.Embed(title="Beşiktaş'ın güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://bjk.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def aze(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,8764,-8279,-3')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('aze.png')
    driver.quit()

    file = discord.File('aze.png')

    embed = discord.Embed(title="Azerbaycan'ın güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://aze.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def ts(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,7215,-8674,6')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('ts.png')
    driver.quit()

    file = discord.File('ts.png')

    embed = discord.Embed(title="Trabzonspor'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://ts.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def giresun(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,7033,-8689,10')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('giresun.png')
    driver.quit()

    file = discord.File('giresun.png')

    embed = discord.Embed(title="Giresunspor'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://giresun.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def rize(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,7454,-8743,7')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('rize.png')
    driver.quit()

    file = discord.File('rize.png')

    embed = discord.Embed(title="Rizespor'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://rize.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def ordu(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,6835,-8729,11')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('ordu.png')
    driver.quit()

    file = discord.File('ordu.png')

    embed = discord.Embed(title="Orduspor'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://ordu.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def samsun(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,6621,-8753,10')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('samsun.png')
    driver.quit()

    file = discord.File('samsun.png')

    embed = discord.Embed(title="Samsunspor'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://samsun.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def erzurum(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,5469,-8800,14')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('erzurum.png')
    driver.quit()

    file = discord.File('erzurum.png')

    embed = discord.Embed(title="Erzurum'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://erzurum.png")

    await message.edit(content=None, embed=embed, file=file)

@bot.command()
async def bursa(ctx):
    driver = webdriver.Chrome()
    driver.get('https://pixelplanet.fun/#d,5485,-8603,16')
    driver.set_window_size(800, 1100)
    driver.set_window_position(600, 600)

    embed = discord.Embed(title="Pyrex PPF", description="Birkaç saniye bekleyin.", color=discord.Color.blurple())
    message = await ctx.send(embed=embed)

    time.sleep(2)
    driver.save_screenshot('bursa.png')
    driver.quit()

    file = discord.File('bursa.png')

    embed = discord.Embed(title="Bursaspor'un güncel hali:", color=discord.Color.blurple())
    embed.set_image(url="attachment://bursa.png")

    await message.edit(content=None, embed=embed, file=file)


@bot.command()
async def yardim(ctx):

    embed = discord.Embed(title="Pyrex PPF", description="Kullanım:", color=discord.Color.blurple())
    embed.set_thumbnail(url=gif)
    embed.add_field(name=f"!fb", value="Fenerbahçe'nin anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!gs", value="Galatasaray'ın anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!bjk", value="Beşiktaş'ın anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!aze", value="Azerbaycan'ın anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!ts", value="Trabzonspor'un anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!giresun", value="Giresunspor'un anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!rize", value="Çaykur Rizespor'un anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!ordu", value="Orduspor'un anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!samsun", value="Samsunspor'un anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!bursa", value="Bursaspor'un anlık durumunu gösterir.", inline=False)
    embed.add_field(name=f"!erzurum", value="Bursaspor'un anlık durumunu gösterir.", inline=False)
    await ctx.send(embed=embed)

bot.run(TOKEN)
