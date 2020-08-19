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
    file_content = requests.get(url, allow_redirects=True)
    file_name = url[-18:-4].replace('/', '_')
    open("Files/{0}.wav".format(file_name), 'wb').write(file_content.content)


def main():
    if not os.path.exists("Files"):
        os.mkdir("Files")

    while True:
        file_url = generate_random_DA_url()
        req = requests.get(file_url)
        stat = req.status_code
        if stat == 200:
            print("Saving {0}".format(file_url))
            save_DA_audio(file_url)

if __name__ == '__main__':
    main()
