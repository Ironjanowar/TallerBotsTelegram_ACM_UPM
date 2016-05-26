import telebot
from telebot import types

# Creamos el botapi
bot = telebot.TeleBot("TOKEN")

# Listener


def listener(messages):
    # When new messages arrive TeleBot will call this function.
    for m in messages:
        if m.content_type == 'text':
            # Prints the sent message to the console
            if m.chat.type == 'private':
                print("Chat -> " + str(m.chat.first_name) +
                      " [" + str(m.chat.id) + "]: " + m.text)
        else:
            print("Group -> " + str(m.chat.title) +
                  " [" + str(m.chat.id) + "]: " + m.text)

# Initializing listener
bot.set_update_listener(listener)

# Handlers


@bot.message_handler(commands=['hello'])
def hello(message):
    # Envia un mensaje al recibir /hello
    bot.reply_to(message, "Hello Telegram")

markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
markup.add(types.KeyboardButton("Yes!", request_location=True))


@bot.message_handler(commands=['location'])
def location(message):
    bot.send_message(message.chat.id, "Me envias tu ubicacion?", reply_markup=markup)


@bot.message_handler(commands=['teclado'])
def teclado(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton("Si"))
    bot.send_message(message.chat.id, "Quieres cerrar el teclado?", reply_markup=markup)


def toggle_trigger(t):
    return not t


@bot.message_handler(commands=['trigger'])
def send_toggle_trigger(m):
    toggle_trigger(trigger_var)
    bot.reply_to(m, "Changing trigger")

trigger_var = False


@bot.message_handler(trigger_var)
def send_trigger(m):
    bot.send_message(m.chat.id, "Trigger changed to true!")

# Ignorar mensajes antiguos
bot.skip_pending = True

# Iniciamos el polling
print("Running...")
bot.polling()
