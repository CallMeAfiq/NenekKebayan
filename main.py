python -m pip install python-telegram-bot 
from typing import Final 
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6852557784:AAHfLvaD5H-3CHdal6yRYhsnI-vnX35dZx4'
BOT_USERNAME: Final = '@HantuShopee_Bot'

async def start_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('Jangan Takut, Jangan Segan. Segala Permintaan, Nenek Sediakan. Sila lihat pada Menu...')

async def promosi_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('Promosi Terkini: ')
    await update.message.reply_text ('Tawaran Gila RM1 Pada 12 TGH \n\n Super RM1.00 - https://shope.ee/7pSkpSJhXJ ')
    await update.message.reply_text ('Akan Datang: ')
    await update.message.reply_text ('NOV25 PAYDAY SALE  \n\n Info: https://shope.ee/6016mGOGZC ')

async def voucher_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ('Maaf Sila Cuba Lagi...\n\nKalau ada nanti nenek akan update...stay tuned')
   



def handle_response(text: str) -> str:
    processed: str = text.lower()


    if 'hello' in processed:
        return 'Hi, Nenek disini...'
    return 'Sorry, nenek x faham...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace (BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print('Bot', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('promosi', promosi_command))
    app.add_handler(CommandHandler('voucher', voucher_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_response))

    app.add_error_handler(error)

    print('Polling...')
    app.run_polling(poll_interval=3)

