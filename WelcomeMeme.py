# Created by Arves100
# 19/09/2019
# File: WelcomeMeme.py
# Deps: python-telegram-api
# Desc: Done for a meme that an italain group asked for, sorry target xD
# License: MIT
import os
import logging
import signal
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
from telegram.error import TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError

TOKEN_FILE = "token.txt"

class WelcomeMeme():
    def __init__(self, botToken):
        logging.basicConfig(format="[%(asctime)s] [%(name)s] [%(levelname)s] >> %(message)s", level=logging.INFO)
        self.bot = Updater(token=botToken, use_context=True)
        self.addHandlers()
        
    def addHandlers(self):
        #start_handler = CommandHandler('start', self.commandStart)
        #self.bot.dispatcher.add_handler(start_handler)
        
        message_handler = MessageHandler(Filters.status_update, self.messageHandler)
        self.bot.dispatcher.add_handler(message_handler)
      
    def commandStart(self, update, context):
        context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

    def messageHandler(self, update, context):
        print(update.message.text)
        
        if update.message.new_chat_members:
            for user in update.message.new_chat_members:
                if user.is_bot:
                    continue
                update.message.reply_text("Benvenuto Master! Sono la maid del gruppo. Spero che ti divertirai qui! 😊")

    def start(self):
        print("Started!")
        self.bot.start_polling()
		
def runBot():
    if not os.path.isfile(TOKEN_FILE):
        print("Sorry, cannot find {} used to store the bot token\nPlease create it and try again.".format(TOKEN_FILE))
        return

    tokenFile = open(TOKEN_FILE, "r")
    token = tokenFile.readlines()[0]
    tokenFile.close()
    print("Starting WelcomeMeme...")
    bot = WelcomeMeme(token)
    bot.start()

if __name__ == "__main__":
    runBot()
