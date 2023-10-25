import requests
import os
import argparse
import download_send_img as di


def fetch_spacex_last_launch(launch, path):
    os.makedirs(path, exist_ok=True)
    url = f'https://api.spacexdata.com/v5/launches/{launch}'
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    launch_images = data['links']['flickr']['original']
    if not launch_images:
        print('There are no images from this launch')
    else:
        for index, link in enumerate(launch_images):
            file_name = f'space{index}.jpg'
            new_path = os.path.join(path, file_name)
            di.download_image(link, new_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your launch')
    parser.add_argument('--launch', help='enter your url: ', default='latest')
    parser.add_argument('--img_dir', help='enter your path ', default='images')
    args = parser.parse_args()
    fetch_spacex_last_launch(args.launch, args.img_dir)
