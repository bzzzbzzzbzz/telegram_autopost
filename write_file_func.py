import requests


def download_image(link, path):
    response = requests.get(link)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)

def download_image_with_api(link, path, token):
    params = {'api_key': token}
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)