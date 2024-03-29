#!/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging
import sys
import Adafruit_DHT as dht
import time
import os

sys.path.append('./config')
import myconfig

MY_URL = myconfig.url
TOKEN = myconfig.token

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def temp(bot, update):
    """Echo the user message."""
    try:
        h,t = dht.read_retry(dht.DHT22, 4)
        time.sleep(2)
        h,t = dht.read_retry(dht.DHT22, 4)
        #print 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)
        #print 'temp on proc:\t'; os.system("/opt/vc/bin/vcgencmd measure_temp")
        response = 'temp:\t\t{0:0.1f}\nhumidity:\t{1:0.1f}'.format(t, h)

    except Exception, e2:
      response = 'нет доступа к gpio'

    update.message.reply_text(response)

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    #updater = Updater(TOKEN)
    #TOKEN = ''
    #bot = telegram.Bot(token=TOKEN, request=pp)

    REQUEST_KWARGS={
        'proxy_url': myconfig.socks5url,
    # Optional, if you need authentication:
        'urllib3_proxy_kwargs': {
          'username': myconfig.socks5username,
          #'username': '',
          'password': myconfig.socks5password,
           #'password': '',
        }
    }
    #global updater
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    #updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("temp", temp))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    bot = updater.bot
    bot.send_message(chat_id=myconfig.chadId, text="I'm a bot, please talk to me!")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
