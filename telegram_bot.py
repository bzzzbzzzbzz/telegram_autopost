import telegram

TOKEN = '1778883378:AAGAVdFnkvgDJET7rOVcUYpppzGFgWJ8aOs'

bot = telegram.Bot(token=f'{TOKEN}')

bot.send_message(chat_id='@spacepics666', text="First photo")
bot.send_photo(chat_id='@spacepics666', photo=open('images/nasa1.jpg', 'rb'))