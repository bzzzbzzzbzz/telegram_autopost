## fetch_spacex_last_launch.py
Script for downloading spacex launch images. 
First of all need to install packages.
Python3 should be already installed. 
Use `pip` to install requirements:
```
pip install -r requirements.txt
```

Use bash commands to run script: 


```
python3 fetch_spacex_last_launch.py --launch 'launch_id' --img_dir 'dir path'
``` 
You can use script without launch id and path:
```
python3 fetch_spacex_last_launch.py
```
In that case, script will run with the last launch and default path dir 'cd/image/'. 
Launch for test: 5eb87d47ffd86e000604b38a
Same default path using for all scripts.
## epic_nasa.py
Script for downloading EPIC nasa photos. Use bash commands to run script: 
```
python3 epic_nasa.py --token 'token' --img_dir 'path'
```


If you run script without token, it will be use demo api token('DEMO_KEY')
## apod_nasa.py
Script that choosing randomly nasa apod photos and download it. Use bash commands to run script:


```
python3 apod_nasa.py --token 'token' --img_dir 'path' --count int(count)
```

You can use '--count' option to set number of photos. Default parameter is 30.
If you run script without token, it will be use demo api token('DEMO_KEY')
## tg_post_all_images.py
Script that randomly take photos from 'images' direction and download one of them in 4 hours. Use bash commands to run script:
First, you need to create new .env file and add two variables:
    

* TG_TOKEN = 'your telegram bot api-token'
* TG_CHAT_ID ='chat id'

```
python3 tg_post_all_images.py --hours 'number'
```

* number = number of hours

If you run script without entering number, it will be use default setting and will post one image per 4 hours.


## tg_bot_post_image.py
Scrit for posting one image from direction in your telegram bot. Run script:
```
python3 tg_bot_post_image.py --img_dir 'path'
```

After running script write image name need to be post. If you leave string empty, it get randomly one photo from direction and post it.


