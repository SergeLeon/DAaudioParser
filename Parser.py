import os
import random

import requests


def generate_random_DA_url():
    url = 'http://static.donationalerts.ru/audiodonations/'
    url1 = "6{0}{1}".format(str(random.randrange(4, 6)), str(random.randrange(111, 999)))
    url2 = str(random.randrange(111, 999))
    url = "{0}{1}/{1}{2}.wav".format(url, url1, url2)
    return url


def save_file(url, path, name):
    file_content = requests.get(url, allow_redirects=True)
    open(f"{path}\\{name}", 'wb').write(file_content.content)


def validate_url(url):
    req = requests.get(url)
    stat = req.status_code
    return stat == 200


def main():
    if not os.path.exists("Files"):
        os.mkdir("Files")

    while True:
        file_url = generate_random_DA_url()
        if validate_url(file_url):
            print("Saving {0}".format(file_url))
            save_file(file_url, "Files\\", file_url[-18:].replace('/', '_'))


if __name__ == '__main__':
    main()
