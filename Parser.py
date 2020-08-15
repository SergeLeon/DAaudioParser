import os
import requests
import random


def generate_random_DA_url():
    url = 'http://static.donationalerts.ru/audiodonations/'
    url1 = "6{0}{1}".format(str(random.randrange(4, 6)), str(random.randrange(111, 999)))
    url2 = str(random.randrange(111, 999))
    url = "{0}{1}/{1}{2}.wav".format(url, url1, url2)
    return url


def save_DA_audio(url):
    filecontent = requests.get(url, allow_redirects=True)
    filename = url[-18:-4].replace('/', '_')
    open("Files/{0}.wav".format(filename), 'wb').write(filecontent.content)


if not os.path.exists("Files"):
    os.mkdir("Files")

while True:
    fileurl = generate_random_DA_url()
    req = requests.get(fileurl)
    stat = req.status_code
    if stat == 200:
        print("Conected {0}".format(fileurl))
        save_DA_audio(fileurl)
