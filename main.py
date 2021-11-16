from telegram import Update
from telegram.ext import *
import logging

updater = Updater(token='2126630484:AAE7_wKynuJiO7HXkvSh1tzogiCClzkOg-g')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update: Update, context: CallbackContext):
    context.bot.sendMessage(chat_id=update.effective_chat.id,
                            text='¡Sólo monos!')

start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()