import argparse
import os
import requests
import telegram
import time
from dotenv import load_dotenv

import download_send_img as si

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser(description='enter period of posting in hours or path')
    parser.add_argument('--hours', metavar='int', type=int, default=4, help='enter period in hours')
    parser.add_argument('--img_dir', default='images', help='enter your path')
    args = parser.parse_args()
    fail_connect = 0
    while True:
        images = si.list_of_path_images(args.img_dir)
        for image in images:
            try:
                si.send_photo_tg_bot(image, tg_token, tg_chat_id)
                fail_connect = 0
            except (requests.exceptions.RequestException, telegram.error.NetworkError) as e:
                fail_connect += 1
                if fail_connect > 2:
                    time.sleep(420)
                continue
            time.sleep(args.hours * 3600)
