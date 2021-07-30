from telebot import TeleBot
from sqlite import get_subscribe
from dotenv import load_dotenv
import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))
TOKEN = os.getenv("TOKEN")

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["subscribe"])
def subscribe_user(message):
    """Подписываем пользователя на уведомления"""
    get_subscribe(message.chat.id)
    bot.send_message(message.chat.id, 'Вы успешно подписались!!!')


if __name__ == '__main__':
    bot.polling()
