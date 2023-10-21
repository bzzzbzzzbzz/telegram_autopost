import telegram, os, random, argparse
from dotenv import load_dotenv
import download_send_img as si


if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    parser = argparse.ArgumentParser(description='enter path')
    parser.add_argument('--img_dir', help='enter your path ', default='images')
    parser.add_argument('--img', help='enter your img ', default=None)
    args = parser.parse_args()
    if not args.img:
        data = list(os.walk(args.img_dir))
        images = data[0][2]
        args.img = random.choice(images)
    si.send_photo_tg_bot(args.img_dir, args.img, tg_token)