## fetch_spacex_last_launch.py
Scpirt for downloading spacex launch images. Use bash commands to run script: 


```
python3 fetch_spacex_last_launch.py 'launch id'
``` 

Link for test: https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a

If you dont put any launch id, script will automaticaly download images from last launch photos was taken 
Python3 should be already installed. 
Use `pip` to install requirements:
```
pip install -r requirements.txt
```
## epic_nasa.py
Script for downloading EPIC nasa photos. Use bash commands to run script: 
```python3 epic_nasa.py 'api_token'```
Use `pip` to install requirements:
```
pip install -r requirements.txt
```

Link for test: https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY
## apod_nasa.py
Script that choosing randomly 30 nasa apod photos and download it. Use bash commands to run script:


```
python3 apod_nasa.py 'link'
```
Link for test: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
## telegram_bot.py
Script that randomly take photos from 'images' direction and download one of them in 4 hours. Use bash commands to run script:


```
python3 telegram_bot.py
```

Create new 'env' file to insert your TOKEN and chat_id