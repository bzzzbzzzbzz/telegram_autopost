import os
import random
import argparse
from dotenv import load_dotenv
import download_send_img as si

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']
    parser = argparse.ArgumentParser(description='enter path')
    parser.add_argument('--img_dir', help='enter your path ', default='images')
    parser.add_argument('--img', help='enter your img ', default=None)
    args = parser.parse_args()
    if not args.img:
        images = si.list_of_path_images(args.img_dir)
        args.img = random.choice(images)
    else:
        args.img = os.path.join(args.img_dir, args.img)
    si.send_photo_tg_bot(args.img, tg_token, tg_chat_id)
