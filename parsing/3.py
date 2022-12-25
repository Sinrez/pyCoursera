import requests
import os

url1 = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
response = requests.get(url=url1, stream=True)
with open('file.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)