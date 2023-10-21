import requests, os
import telegram

def download_image(link, path, token=None):
    params = {'api_key': token}
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def send_photo_tg_bot(path, img_name, token):
    bot = telegram.Bot(token=token)
    new_path = os.path.join(path, img_name)
    with open(new_path, 'rb') as file:
        bot.send_photo(chat_id=os.environ['TG_CHAT_ID'], photo=file)