import discord
from discord.ext import commands
from database import Database

# Botun Tanımlanması
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!",intents=intents)
db = Database("tasks.db")

@bot.event
async def on_ready():
    print(f"Bot {bot.user} olarak giriş yaptı!")

@bot.command()
async def add_task(ctx, *, description: str):
    task_id = db.add_task(description)
    await ctx.send(f"Görev eklendi: {description} (ID: {task_id})")

@bot.command()
async def complete_task(ctx, task_id: int):
    db.complete_task(task_id)
    await ctx.send(f"Görev tamamlandı: {task_id}")

@bot.command()
async def delete_task(ctx, task_id: int):
    db.delete_task(task_id)
    await ctx.send(f"Görev silindi: {task_id}")

@bot.command()
async def show_tasks(ctx):
    tasks = db.get_tasks()
    if not tasks:
        await ctx.send("Hiç görev yok.")
        return
    
    response = "Görev Listesi:\n"
    for task in tasks:
        status = "✅" if task[2] else "❌"
        response += f"{task[0]} - {task[1]} [{status}]\n"
    
    await ctx.send(response)

bot.run("anahtar")#tokenla calisir
