import telebot
from telebot import types

with open("token", "r") as TOKEN:
    # Creamos el bot
    bot = telebot.TeleBot(TOKEN.readline().strip())


def listener(messages):
    # When new messages arrive TeleBot will call this function.
    for m in messages:
        if m.content_type == 'text':
            # Prints the sent message to the console
            if m.chat.type == 'private':
                print("User: " + str(m.from_user.username) + "      Id: " + str(m.chat.id) + "  \nSaid: " + str(m.text) + "\n\n")
            else:
                print("Group: " + str(m.chat.title) + "      Id: " + str(m.chat.id) + "  \nSaid: " + str(m.text) + "\n\n")

# Initializing listener
bot.set_update_listener(listener)

# Handlers


@bot.message_handler(commands=['id'])
def send_id(message):
    # Envia la ID y el Username de quien le ha hablado
    toSend = "Username: " + str(message.from_user.username) + "\nID: " + str(message.from_user.id)
    bot.send_message(message.chat.id, toSend)


@bot.inline_handler(lambda query: query.query.lower() == "id")
def inline_id(query):
    # Envia la  ID y el Username de quien le habla por inline
    toSend  = "Username: " + str(query.from_user.username) + "\nID: " + str(query.from_user.id)
    r = types.InlineQueryResultArticle('1', 'My ID and Username', types.InputTextMessageContent(toSend))
    bot.answer_inline_query(query.id, [r])

# Arrancamos el bot
print("Running...")
bot.polling()
