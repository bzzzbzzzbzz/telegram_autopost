import os.path

import requests

def epic_nasa_today(url,path):
    if not os.path.exists(path):
        os.makedirs(path)
    response = requests.get(url)
    response.raise_for_status()
    for index, data in enumerate(response.json()):
        photo_name = data['image']
        photo_date = data['date']
        split_date = photo_date.split(' ')
        new_split = split_date[0].split('-')
        photo_link = f'https://api.nasa.gov/EPIC/archive/natural/{new_split[0]}/{new_split[1]}/{new_split[2]}/png/{photo_name}.png?api_key=DEMO_KEY'
        new_response = requests.get(photo_link)
        new_response.raise_for_status()
        filename = f'epic{index}.png'
        with open (f'{path}{filename}', 'wb') as file:
            file.write(new_response.content)



url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
path = 'images/'

epic_nasa_today(url, path)