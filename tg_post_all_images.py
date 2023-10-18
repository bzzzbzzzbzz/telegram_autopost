import telegram, os, time, argparse,requests
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=f'{tg_token}')
    parser = argparse.ArgumentParser(description='enter period of posting in hours or path')
    parser.add_argument('--hours', metavar='int', type=int, default=4, help='enter period in hours')
    parser.add_argument('--path', default='images', help='enter your path')
    args = parser.parse_args()
    while True:
        try:
            data = list(os.walk(args.path))
            images = data[0][2]
            for image in images:
                new_path = os.path.join(args.path, image)
                with open(new_path, 'rb') as file:
                    bot.send_photo(chat_id=os.environ['TG_CHAT_ID'], photo=file)
                time.sleep(args.hours * 3600)
        except (requests.exceptions.RequestException, telegram.error.NetworkError) as e:
            continue

