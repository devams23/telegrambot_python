from telegram import Update
from typing import Final
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
'''
            FOLLOW THE STEPS BELOW TO GET YOUR TOKEN FOR FREE!
            1) Open telegram (app/webapp) , and search for BotFather 
            2) CLICK ON THE START BUTTON AND TYPE THE COMMAND - '/newbot'
            3) Fill the required Details it will ask for .
            4) YOUR TOKEN WILL BE IN THE MESSAGE.

            NEXT YOU HAVE TO TELL THE BOT FATHER TO ACCEPT THE COMMANDS GIVEN IN THE SCRIPT 
            1) TYPE COMMAND '/setcommands' , and fill in the details as instructed .
            2) Take care while writing  commands , it should match with the one in the script.
'''
TOKEN: Final = "YOUR_TOKEN"
BOT_USERNAME: Final = "YOUR_BOT_USERNAME"


# Bot Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is start commmand")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is help commmand")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("this is custom commmand")

# message Responses


def handle_response(text: str):
    usertext = text.lower()
    if 'hello' in usertext:
        return 'Hey , There !'

    elif 'how are you' in usertext:
        return 'Im fine !'

    elif 'life' in usertext:
        return 'this is life  !'

    return 'I can understand that !'


# Handle Message

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    message_text = update.message.text

    print(f'user:{update.message.chat.id} ::: {message_type} ::: {message_text} ')

    if message_type == 'group':
        if BOT_USERNAME in message_text:
            response = handle_response(
                message_text.replace(BOT_USERNAME, "").strip())

        else:
            return

    else:
        print("Private Message")
        response = handle_response(
            message_text.replace(BOT_USERNAME, "").strip())
        print(response)
    print("Bot : ", response)
    await update.message.reply_text(response)

# errors


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause an error {context.error}')


if __name__ == "__main__":
    print("Bot Started...")
    app = Application.builder().token(TOKEN).build()

# Handling commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

# Handling responses
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

# Handling Errors
    app.add_error_handler(error)

# Polling
    print("Polling.....")
    app.run_polling(poll_interval=3)
