from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5319022954:AAEvOChYOQOYNe_dRPmrPFHNsV_32pfOLYw",
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Welcome to our support Bot. Type ' /help ' See Available Commands. and thank you to selecting us")
        
def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :-
    /instagram - To get the instagram URL
    /telegram - To get the telegram URL
    /linkedin - To get the LinkedIn profile URL
    /gmail - To get gmail URL
    /use - To get the GeeksforGeeks URL""")
        
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("screenrecorder1234anishubh@gmail.com")
  
  
def instagram_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://instagram.com/interest.ing_ai?igshid=YmMyMTA2M2Y=")
  

def telegram_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://t.me/interesting_ai")
  
def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("https://www.linkedin.com/in/shubham-shingare-038636221")
  
  
def use_of_app(update: Update, context: CallbackContext):
    update.message.reply_text("The use of our software is quite simple:  1::start. 2::pause. 3::end three buttons are there. you just start recording by pressing 'start' button . if you want to pause hou have to use 'pause' button and for stop you just press 'end' button. when you ended your recording that recorded video is saved at output folder. ")
  
  
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
  
  
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
        

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('instagram', instagram_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('telegram', telegram_url))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('use', use_of_app))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))
  
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()

