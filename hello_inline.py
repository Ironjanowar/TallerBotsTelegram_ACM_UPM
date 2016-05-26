import telebot
from telebot import types

# Creamos el bot
bot = telebot.TeleBot("201337136:AAHc5lIPPqAFqAcX6bNMTNV2pFTzlbzsJtI")


@bot.inline_handler(lambda query: query.query == "hola")
def hola(inline_query):
    # Envia Well Hello
    r = types.InlineQueryResultArticle('1', 'Saludo', types.InputTextMessageContent("Well hello!"))
    bot.answer_inline_query(inline_query.id, [r])

# Iniciamos el bot
print("Running...")
bot.polling()
