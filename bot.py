from config import BOT_TOKEN
from telebot import TeleBot


bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def bot_start(message):
    print('Получена команда /start')
    bot.send_message(message.chat.id, text="Я готов к работе!")

@bot.message_handler(commands=['help'])
def bot_help(message):
    print('Получена команда /help')
    bot.send_message(message.chat.id, text="Я буду повторять ваши сообщения и кидать кубик, если напишите слово 'кубик'.")


#------кидает кубик---------------------
# Функция для фильтрации сообщений: должна возвратить True
def filter_kubik(message):
    password = "кубик"
    return password in message.text.lower()

@bot.message_handler(content_types=['text'], func = filter_kubik)
def kubik(message):
    bot.send_dice(message.chat.id)

#---------------------------------------

@bot.message_handler(content_types=['text'])
def send_message(message):
    print(f'Полученo сообщение: {message.text}')
    bot.send_message(message.chat.id, text=f'Вы написали "{message.text}"')


bot.polling()


