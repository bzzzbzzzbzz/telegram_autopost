import telegram, os, time, argparse, requests
from dotenv import load_dotenv
import download_send_img as si

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    parser = argparse.ArgumentParser(description='enter period of posting in hours or path')
    parser.add_argument('--hours', metavar='int', type=int, default=4, help='enter period in hours')
    parser.add_argument('--img_dir', default='images', help='enter your path')
    args = parser.parse_args()
    fail_connect = 0
    while True:
        data = list(os.walk(args.img_dir))
        images = data[0][2]
        for image in images:
            try:
                si.send_photo_tg_bot(args.img_dir, image, tg_token)
                fail_connect = 0
            except (requests.exceptions.RequestException, telegram.error.NetworkError) as e:
                fail_connect += 1
                if fail_connect > 2:
                    time.sleep(420)
                continue
            time.sleep(args.hours * 3600)
