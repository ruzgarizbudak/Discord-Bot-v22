import discord
from discord.ext import commands
import hbjdh
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def topla(ctx,*args):
    toplam=0
    for i in (args):
        toplam+=int(i)
    await ctx.send(toplam)

@bot.command()
async def cikar(ctx,s1,*args):
    cikarim=int(s1)
    for i in (args):
        cikarim-=int(i)
    await ctx.send(cikarim)

@bot.command()
async def carp(ctx,*args):
    carpim=1#sıfır olmaz çünkü sıfırla herşeyin çarpımı sıfır'a eşşittir
    for i in (args):
        carpim*=int(i)
    await ctx.send(carpim)

@bot.command()
async def bol(ctx,s1,*argss):
    bolum=int(s1)
    for i in (argss) :
        bolum/=int(i)
    await ctx.send(bolum)

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def tekrarla(ctx,kez:int,kelime:str):
    for i in range(kez):
        await ctx.send(kelime)

@bot.command()
async def sifre(ctx,sayi=10):
    await ctx.send(hbjdh.sifre(sayi))

@bot.command()
async def meme(ctx):
    with open("resim/x.png","rb") as f:
        ilkr=discord.File(f)
    await ctx.send(file=ilkr)

@bot.command()
async def ymeme(ctx):
    with open("resim/x1.png","rb") as f:
        ilkr=discord.File(f)
    await ctx.send(file=ilkr)

@bot.command()
async def fmeme(ctx):
    with open("resim/x2.png","rb") as f:
        ilkr=discord.File(f)
    await ctx.send(file=ilkr)

@bot.command()
async def mem(ctx):
    bilinmez=random.choice(os.listdir("resim"))
    with open(f"resim/{bilinmez}","rb") as f:
        r=discord.File(f)
    await ctx.send(file=r)

@bot.command()
async def kelimesec(ctx,*argss):
    for i in(argss):
        x=random.choice(i)
    await ctx.send(x)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)








def get_fox_image_url():    
    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    return data['image']



@bot.command('fox')
async def fox(ctx):
    image_url = get_fox_image_url()
    await ctx.send(image_url)


def get_pokeman_image_url():    
    url = "https://pokeapi.co/api/v2/pokemon/ditto"
    res = requests.get(url)
    data = res.json()
    x = random.choice(list(data["sprites"].keys()))  
    return data["sprites"][x]



   
@bot.command("pokeman")
async def pokeman(ctx):
    image_url = get_pokeman_image_url()
    await ctx.send(image_url)



def get_dog_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data['url']



@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)




@bot.command()
async def hikaye(ctx):
    x=random.choice(os.listdir("hikayeler"))
    with open(f"hikayeler/{x}","r",encoding='utf-8')as f:
        q=discord.File(f)
    await ctx.send(file=q)


@bot.command()
async def naber(ctx):
    x=["iyi,sen?","stabil,senden?","olumsuzluk yok,sen?","iyi diyelim iyi olalım,sen?"]
    xq=random.choices(x,weights=[9,2,5,7],k=1)
    await ctx.send(xq)


@bot.command()
async def nerelisin(ctx):
    await ctx.send("Türküm.Sen nerelisin?")

@bot.command()
async def satranc_acilis(ctx):
    x=["İtalyan Açılışı","Fransız Savunması","Caroo-Kann Defansı","Sicilyan Savunması","Vezir Gambiti","Şah Hint Açılışı"]
    qx=random.choices(x,weights=[8,5,7,6,3,1],k=1)
    await ctx.send(qx)
