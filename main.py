token = "5933312715:AAEzq0UWAc-5OjihgLDBJFsGsreztC_j3M0"
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters


async def hello(update, context):
    await update.message.reply_text("hello")


app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.Regex(r"([Пп]рив(ет)|[Дд]о(нат))"), hello))
app.run_polling()
