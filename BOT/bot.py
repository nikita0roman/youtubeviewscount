import telebot
import config
import test

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
    # bot.send_message(message.chat.id, message.text)
    # bot.send_message(message.chat.id, message.text)
    if 'https://www.youtube.com' in message.text:
        bot.send_message(message.chat.id, test.couner(message.text) + ' views')
    else:
        bot.send_message(message.chat.id, "incorrect link")

bot.polling(none_stop=True)