from telegram.ext import Updater, MessageHandler, Filters

import os
TOKEN = os.environ.get("8126644790:AAF9ldB6hSvPBKGG7mIRYH1WV1mH7eHJFWk")  # Render-də gizli saxlanması üçün

def cavabla(update, context):
    mesaj = update.message.text.lower()
    if 'salam' in mesaj:
        update.message.reply_text("Aleykum")

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
handler = MessageHandler(Filters.text & ~Filters.command, cavabla)
dispatcher.add_handler(handler)

updater.start_polling()
print("Bot işləyir...")
updater.idle()
