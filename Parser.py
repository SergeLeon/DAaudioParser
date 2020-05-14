import os
import requests
import random

if not os.path.exists("Files"):  # Checking for the "Files" directory
    os.mkdir("Files")  # Creating the "Files" directory if it is not available

while True:
    url = 'http://static.donationalerts.ru/audiodonations/'  # Generating a download link
    url1 = "6" + str(random.randrange(4, 6)) + str(random.randrange(111, 999))
    url2 = str(random.randrange(111, 999))
    url = url + url1 + '/' + url1 + url2 + ".wav"
    req = requests.get(url)
    stat = req.status_code
    if stat == 200:  # Access check
        print("Есть подключение " + url)
        myFile = requests.get(url, allow_redirects=True)
        open(os.path.join("Files" , url1 + "_" + url1 + url2 + ".wav"), 'wb').write(myFile.content)  # Save file
