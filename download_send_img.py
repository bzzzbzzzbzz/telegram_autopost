import requests
import os
import telegram


def download_image(link, path, token=None):
    params = {'api_key': token}
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def send_photo_tg_bot(img_name, token, chat_id):
    bot = telegram.Bot(token=token)
    with open(img_name, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)


def list_of_path_images(path):
    data = list(os.walk(path))
    empty_list = []
    for image in data[0][2]:
        new_path = os.path.join(path, image)
        empty_list.append(new_path)
    return empty_list
