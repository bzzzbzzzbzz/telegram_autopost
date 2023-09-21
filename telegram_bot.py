import telegram, os, time, random

TOKEN = '1778883378:AAGAVdFnkvgDJET7rOVcUYpppzGFgWJ8aOs'

bot = telegram.Bot(token=f'{TOKEN}')

while True:
    data = list(os.walk('images'))
    print(data)
    images = data[0][2]
    random.shuffle(images)
    for image in images:
        bot.send_photo(chat_id='@spacepics666', photo=open(f'images/{image}', 'rb'))
        time.sleep(14400)