import requests 
import telebot 

PRIVATE = ''

def main():
    global PRIVATE
    print('👇')
    PRIVATE = input("😀Por favor, introduce el token de tu bot: ")
    bot = telebot.TeleBot(PRIVATE)

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.reply_to(message,f'''•• Bienvenido al bot que convierte imágenes en enlaces de descarga directa. Envía la imagen ahora para crear el enlace ← [⌛]

        [⌥] 𝘽𝙔:  Team JXLL/BSZ  '''
        ) 

    @bot.message_handler(content_types=['photo']) #@JXLL_Commander
    def handle_photo(message):
        photo_id = message.photo[-1].file_id
        file_info = bot.get_file(photo_id)
        file_url = f"https://api.telegram.org/file/bot{PRIVATE}/{file_info.file_path}"
        bot.reply_to(message, file_url)

    bot.polling()

if __name__ == "__main__":
    main()
