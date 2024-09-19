from commands import bot

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')


bot.run('') 