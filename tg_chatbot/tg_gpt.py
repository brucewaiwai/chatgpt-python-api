
import openai
import logging

from telegram import Update
from telegram.ext import Updater, Filters, CallbackContext
from telegram.ext import MessageHandler, CommandHandler, InlineQueryHandler, CallbackQueryHandler

logging.basicConfig(level=logging.DEBUG)



def read_file(file):
    text = ''
    try:
        with open(file, "r") as file:
            text = file.read()
    except Exception as e:
        print(e)

    return text



def message_handler(update: Update, context: CallbackContext):

    reply = user_input(update.message.text)
    context.bot.send_message(chat_id=update.message.chat.id, text=reply)

def user_input(msg):
    message = msg
    # generate text with the GPT-3 model
    if message:
        messages.append({"role": "user", "content": message})

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    # print the generated text
    reply = chat['choices'][0]['message']['content']
    print(f'Bot: {reply}')
    return reply
    


if __name__ == "__main__":
    api_key = read_file("api_key.txt")
    tg_token = read_file("tg_token.txt")
    company_info = read_file("customer_service/company/company_info.txt")
    preset = read_file("customer_service/company/preset.txt")
    
    if api_key != '':
        # set up the API credentials
        # openai config
        openai.api_key = api_key
        messages = [{"role": "system", "content": f"{preset}, {company_info}"}]
        # TG config
        updater = Updater(tg_token)
        updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=message_handler))


        updater.start_polling()
        updater.idle()
        updater.stop()

    
