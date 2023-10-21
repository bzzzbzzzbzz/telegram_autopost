import requests, os, argparse
from urllib.parse import urlsplit
import download_send_img as di

def get_image_expansion(link):
    split_link = urlsplit(link)
    temp_link = f'{split_link.netloc}{split_link.path}'
    expansion = os.path.splitext(temp_link)[1]
    return expansion

def fetch_apod_nasa_photos(path, token, count):
    os.makedirs(path, exist_ok=True)
    url = f'https://api.nasa.gov/planetary/apod'
    payload = {'count': count,
               'api_key': token}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    json_data = response.json()
    for index, data in enumerate(json_data):
        link = data['url']
        if data['media_type'] == 'image':
            filename = f'nasa{index}{get_image_expansion(link)}'
            new_path = os.path.join(path, filename)
            di.download_image(link, new_path)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your token')
    parser.add_argument('--token', metavar='token', help='enter your token: ', default='DEMO_KEY')
    parser.add_argument('--img_dir', help='enter your path ', default='images')
    parser.add_argument('--count', help='enter number of photos', type=int, default=30)
    args = parser.parse_args()
    fetch_apod_nasa_photos(args.img_dir, args.token, args.count)
