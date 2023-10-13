## fetch_spacex_last_launch.py
Scpirt for downloading spacex launch images. 
First of all need to install packages.
Python3 should be already installed. 
Use `pip` to install requirements:
```
pip install -r requirements.txt
```

Use bash commands to run script: 


```
python3 fetch_spacex_last_launch.py 'launch id'
``` 
You can use script without launch id:
```
python3 fetch_spacex_last_launch.py
```
In that case, script will run with latest launch. 
Launch for test: 5eb87d47ffd86e000604b38a

## epic_nasa.py
Script for downloading EPIC nasa photos. Use bash commands to run script: 
```
python3 epic_nasa.py 'api_token'
```


If you run script without token, it will be use demo api token('DEMO_KEY')
## apod_nasa.py
Script that choosing randomly 30 nasa apod photos and download it. Use bash commands to run script:


```
python3 apod_nasa.py 'api token'
```
If you run script without token, it will be use demo api token('DEMO_KEY')
## telegram_bot.py
Script that randomly take photos from 'images' direction and download one of them in 4 hours. Use bash commands to run script:
First, you need to create new .env file and add two variables:


* TG_TOKEN = 'your telegram bot api-token'
* TG_CHAT_ID ='chat id'

```
python3 telegram_bot.py --hours 'number'
```

* number = number of hours

If you run script without entering number, it will be use default setting and will post one image per 4 hours.


