import requests, os, argparse

def fetch_spacex_last_launch(url, path):
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if not data['links']['flickr']['original']:
        print('There are no images from this launch')
    else:
        for index, link in enumerate(data['links']['flickr']['original']):
            file_name = f'space{index}.jpg'
            new_response = requests.get(link)
            new_response.raise_for_status()
            if new_response.status_code == 200:
                with open(f'{path}/{file_name}', 'wb') as file:
                    file.write(new_response.content)
            else:
                return 'Failed to retrive data'

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your url http://...')
    parser.add_argument('url', metavar='url', help='enter your url: ')
    path = 'images/'
    if not parser:
        url = 'https://api.spacexdata.com/v5/launches/latest'
        fetch_spacex_last_launch(url, path)
    else:
        args = parser.parse_args()
        fetch_spacex_last_launch(args.url,path)

#https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a