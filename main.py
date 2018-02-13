import logging
import telegram
from telegram.ext import Updater
from config import *
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from texts import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
updater = Updater(token=TOKEN)
bot = telegram.Bot(token=TOKEN)
print(bot.get_me())
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=MSG_START)


def echo(bot, update):
    text = update.message.text.lower()
    if update.message.chat_id != MODERATION_CHAT_ID:
        bot.send_message(chat_id=MODERATION_CHAT_ID, text=update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text= MSG_SENT)
    else:
        if update.message.reply_to_message is not None:
            msg = update.message.reply_to_message
            if text == '+':
                bot.sendMessage(chat_id=CHANNEL_NAME, text=msg.text)


disp = updater.dispatcher
disp.add_handler(CommandHandler("start", start))
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
updater.idle()
