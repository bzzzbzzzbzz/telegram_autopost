import requests


def download_image(link, path):
    response = requests.get(link)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)