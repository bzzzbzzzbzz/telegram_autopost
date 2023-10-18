import telegram, os, random, argparse
from dotenv import load_dotenv

if __name__ == '__main__':
    if __name__ == '__main__':
        load_dotenv()
        tg_token = os.environ['TG_TOKEN']
        bot = telegram.Bot(token=f'{tg_token}')
        parser = argparse.ArgumentParser(description='enter path')
        parser.add_argument('--path', help='enter your path ', default='images')
        args = parser.parse_args()
        image_name = str(input('Enter your image: '))
        if not image_name:
            data = list(os.walk(args.path))
            images = data[0][2]
            image_name = random.choice(images)
        new_path = os.path.join(args.path, image_name)
        with open(new_path, 'rb') as file:
            bot.send_photo(chat_id=os.environ['TG_CHAT_ID'], photo=file)