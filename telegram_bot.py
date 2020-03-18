import logging
from telegram.ext import Updater
from scrapty import *
from telegram.ext import CommandHandler
from dotenv import load_dotenv

load_dotenv()

# log any errors
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# telegram token
botToken = os.getenv('BOT_TOKEN')
print(botToken)
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token=botToken, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    """
     start bot command handler
    """
    context.bot.send_message(chat_id="@toplessmemes",
                             text="Hello , its a private Bot ! not working for every one")


def send(update, context):
    # call the scrapper
    downloader = Reddit()
    downloader.dl_reddit_memes(5000, 50000, True, False)
    for image in images_url:
        context.bot.send_photo(chat_id="@toplessmemes", photo=image,
                               caption="Join top memes: https://t.me/toplessmemes \n")
        # time.sleep(2) # 15 sec pause before sending
        print( image + " send to channel " + str(t.now())) # cmd log


# get user /start command
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# get send /send command
send_handler = CommandHandler('send', send)
dispatcher.add_handler(send_handler)

# start the bot
updater.start_polling()
