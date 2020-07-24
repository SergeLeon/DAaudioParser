import os
import requests
import random

if not os.path.exists("Files"):  # Checking for the "Files" directory
    os.mkdir("Files")  # Creating the "Files" directory if it is not available

while True:
    url = 'http://static.donationalerts.ru/audiodonations/'  # Generating a download link
    url1 = "6{0}{1}".format(str(random.randrange(4, 6)), str(random.randrange(111, 999)))
    url2 = str(random.randrange(111, 999))
    url = "{0}{1}/{1}{2}.wav".format(url, url1, url2)
    req = requests.get(url)
    stat = req.status_code
    if stat == 200:  # Access check
        print("Есть подключение {0}".format(url))
        myFile = requests.get(url, allow_redirects=True)
        open(os.path.join("Files/{0}_{0}{1}.wav".format(url1, url2)), 'wb').write(myFile.content)  # Save file
