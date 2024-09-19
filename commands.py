import discord
from discord.ext import commands
from database import Session, Task


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def add_task(ctx, *, description):
    session = Session()
    new_task = Task(description=description)
    session.add(new_task)
    session.commit()
    session.close()
    await ctx.send(f"Görev eklendi: {description}")


@bot.command()
async def delete_task(ctx, task_id: int):
    session = Session()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task:
        session.delete(task)
        session.commit()
        await ctx.send(f"\"{task.description}\" görevi silindi.")
    else:
        await ctx.send(f"ID'si {task_id} olan görev bulunamadı.")
    session.close()


@bot.command()
async def show_tasks(ctx):
    session = Session()
    tasks = session.query(Task).all()
    if tasks:
        task_list = '\n'.join([f"{task.id}: {task.description} - {'Tamamlandı' if task.completed else 'Yapılacak'}" for task in tasks])
        await ctx.send(f"Görevler:\n{task_list}")
    else:
        await ctx.send("Hiç görev yok.")
    session.close()


@bot.command()
async def complete_task(ctx, task_id: int):
    session = Session()
    task = session.query(Task).filter(Task.id == task_id).first()
    if task and task.completed == 0:
        task.completed = True
        session.commit()
        await ctx.send(f"\"{task.description}\" görevi tamamlandı olarak işaretlendi.")
    elif task:
        await ctx.send(f"\"{task.description}\" görevi zaten tamamlanmış.")
    else:
        await ctx.send(f"ID'si {task_id} olan görev bulunamadı.")
    session.close()
