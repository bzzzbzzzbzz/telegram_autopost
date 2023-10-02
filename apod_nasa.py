import requests, os
from urllib.parse import urlsplit

def fetch_apod_nasa_photos(path):
    os.makedirs(path, exist_ok=True)
    payload = {'api_key': 'DEMO_KEY',
               'count': 30}
    response = requests.get(f'https://api.nasa.gov/planetary/apod', params=payload)
    response.raise_for_status()
    json_data = response.json()
    for index, data in enumerate(json_data):
        link = data['url']
        if 'nasa' in link:
            splited_link = urlsplit(link)
            temp_link = f'{splited_link.netloc}{splited_link.path}'
            filename = f'nasa{index}{os.path.splitext(temp_link)[1]}'
            new_response = requests.get(link)
            new_response.raise_for_status()
            new_path = os.path.join(path, filename)
            if new_response.ok:
                with open(new_path, 'wb') as file:
                    file.write(new_response.content)
            else:
                return 'Failed to retrive data'


if __name__ == '__main__':
    path = 'images/'
    fetch_apod_nasa_photos(path)
