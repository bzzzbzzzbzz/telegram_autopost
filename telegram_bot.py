import telegram, os, time, random, argparse
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    tg_token = os.environ['TG_TOKEN']
    bot = telegram.Bot(token=f'{tg_token}')
    path = 'images'
    parser = argparse.ArgumentParser(description='enter period of posting in hours')
    parser.add_argument('--hours', metavar='int', type=int, default=4, help='enter period in hours')
    args = parser.parse_args()
    while True:
        data = list(os.walk(path))
        images = data[0][2]
        random.shuffle(images)
        for image in images:
            new_path = os.path.join(path, image)
            with open(new_path, 'rb') as file:
                bot.send_photo(chat_id=os.environ['TG_CHAT_ID'], photo=file)
            time.sleep(args.hours*3600)

