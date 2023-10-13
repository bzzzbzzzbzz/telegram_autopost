import os.path
import argparse
import requests
import write_file_func as wf

def fetch_epic_nasa_today(url,path, token):
    os.makedirs(path, exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    for index, data in enumerate(response.json()):
        photo_name = data['image']
        photo_date = data['date']
        split_date = photo_date.split(' ')
        new_split = split_date[0].split('-')
        photo_link = f'https://api.nasa.gov/EPIC/archive/natural/{new_split[0]}/{new_split[1]}/{new_split[2]}/png/{photo_name}.png?api_key={token}'
        filename = f'epic{index}.png'
        new_path = os.path.join(path, filename)
        wf.download_image(photo_link, new_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='enter your token')
    parser.add_argument('--token', help='enter your token ', default='DEMO_KEY')
    args = parser.parse_args()
    url = f'https://api.nasa.gov/EPIC/api/natural/images?api_key={args.token}'
    path = 'images/'
    fetch_epic_nasa_today(url, path, args.token)