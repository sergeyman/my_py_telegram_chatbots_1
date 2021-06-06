#pip install pyTelegramBotAPI

import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

# /start command handler  (send sticker + hello msg)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(message.from_user, bot.get_me()),
        parse_mode='html')

@bot.message_handler(content_types=['text'])
def repeat_all_msgs(message):
    bot.send_message(message.chat.id, message.text) 

#RUN
bot.polling(none_stop=True)

#>python asv_1_bot.py