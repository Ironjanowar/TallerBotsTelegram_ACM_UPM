import telebot
from telebot import types

bot = telebot.TeleBot("201337136:AAHc5lIPPqAFqAcX6bNMTNV2pFTzlbzsJtI")


@bot.inline_handler(lambda query: query.query == "handler")
def hola(inline_query):
    r1 = types.InlineQueryResultArticle('1', 'Titulo1', types.InputTextMessageContent("Respuesta"))
    r2 = types.InlineQueryResultArticle('2', 'Titulo2', types.InputTextMessageContent("Respuesta2"))

    bot.answer_inline_query(inline_query.id, [r1, r2])

print("Running...")
bot.polling()
