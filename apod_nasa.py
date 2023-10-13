import requests, os, argparse
from urllib.parse import urlsplit
import write_file_func as wf

def fetch_apod_nasa_photos(path, url):
    os.makedirs(path, exist_ok=True)
    payload = {'count': 30}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    json_data = response.json()
    for index, data in enumerate(json_data):
        link = data['url']
        if 'nasa' in link:
            splited_link = urlsplit(link)
            temp_link = f'{splited_link.netloc}{splited_link.path}'
            filename = f'nasa{index}{os.path.splitext(temp_link)[1]}'
            new_path = os.path.join(path, filename)
            wf.download_image(link,new_path)




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your token')
    parser.add_argument('--token', metavar='token', help='enter your token: ', default='DEMO_KEY')
    args = parser.parse_args()
    url = f'https://api.nasa.gov/planetary/apod?api_key={args.token}'
    path = 'images/'
    fetch_apod_nasa_photos(path,url)
