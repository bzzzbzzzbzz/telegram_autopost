import os.path
import argparse
import requests
import download_send_img as di
from datetime import datetime


def fetch_epic_nasa_today(path, token):
    os.makedirs(path, exist_ok=True)
    url = f'https://api.nasa.gov/EPIC/api/natural/images'
    params = {'api_key': token}
    response = requests.get(url, params=params)
    response.raise_for_status()
    for index, data in enumerate(response.json()):
        photo_name = data['image']
        photo_date = datetime.fromisoformat(data['date'])
        photo_link = f'https://api.nasa.gov/EPIC/archive/natural/{photo_date.year}/{photo_date.month}/{photo_date.day}/png/{photo_name}.png'
        filename = f'epic{index}.png'
        new_path = os.path.join(path, filename)
        di.download_image(photo_link, new_path, token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your token or path')
    parser.add_argument('--token', help='enter your token ', default='DEMO_KEY')
    parser.add_argument('--img_dir', help='enter your path ', default='images')
    args = parser.parse_args()
    fetch_epic_nasa_today(args.img_dir, args.token)
