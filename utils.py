import requests

from converter import PdfConverter


def get_documnet_url(bot, message, token):
    documend_id = message.document.file_id
    document_path = bot.get_file(documend_id).file_path
    url_to_file = f'https://api.telegram.org/file/bot{token}/{document_path}'
    return url_to_file


def convert_to_epub(pdf_file_url):
    convertor = PdfConverter()
    url_to_epub_file = convertor.convert_to_epub(pdf_file_url)
    return url_to_epub_file


def save_epub_file(filename, url_to_epub):
    with open(filename, 'wb') as new_file:
        response = requests.get(url_to_epub)
        new_file.write(response.content)
    

def send_file(bot, chat_id, filename):
    with open (filename, 'rb') as read_file:
        bot.send_document(chat_id, read_file)
