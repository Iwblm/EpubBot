import requests
import telebot

from envs import TELEGRAM_TOKEN
from utils import get_documnet_url, convert_to_epub, save_epub_file, \
                  send_file


bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "I just get PDF file and convert it to epub")


@bot.message_handler(content_types=['document'])
def handle_pds(message):
    chat_id = message.chat.id
    document_name = message.document.file_name
    if document_name.rsplit('.')[1] != 'pdf':
        bot.reply_to(message, 'Incorrect extension. Only pdf files')
        return
    document_url = get_documnet_url(bot, message, TELEGRAM_TOKEN)
    url_to_epub_file = convert_to_epub(document_url)
    filename = document_name.rsplit('.')[0] + '.epub'
    save_epub_file(filename, url_to_epub_file)
    send_file(bot, chat_id, filename)

if __name__ == '__main__':
    bot.polling()
