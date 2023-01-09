from decouple import config
from telebot import TeleBot


API_TOKEN = config('API_TOKEN')
BOT_TOKEN = config('TOKEN')

bot = TeleBot(BOT_TOKEN)
