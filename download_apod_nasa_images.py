import requests, os, argparse
from urllib.parse import urlsplit
import write_file_func as wf

def get_image_expansion(link):
    splited_link = urlsplit(link)
    temp_link = f'{splited_link.netloc}{splited_link.path}'
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
            wf.download_image(link, new_path)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your token')
    parser.add_argument('--token', metavar='token', help='enter your token: ', default='DEMO_KEY')
    parser.add_argument('--path', help='enter your path ', default='images')
    parser.add_argument('--count', help='enter number of photos', type=int, default=30)
    args = parser.parse_args()
    fetch_apod_nasa_photos(args.path, args.token, args.count)
