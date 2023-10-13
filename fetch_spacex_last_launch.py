import requests, os, argparse
import write_file_func as wf

def fetch_spacex_last_launch(url, path):
    os.makedirs(path,exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    if not data['links']['flickr']['original']:
        print('There are no images from this launch')
    else:
        for index, link in enumerate(data['links']['flickr']['original']):
            file_name = f'space{index}.jpg'
            new_path = os.path.join(path, file_name)
            wf.download_image(link, new_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your launch')
    parser.add_argument('--launch', help='enter your url: ', default='latest')
    path = 'images/'
    args = parser.parse_args()
    url = f'https://api.spacexdata.com/v5/launches/{args.launch}'
    fetch_spacex_last_launch(url,path)

