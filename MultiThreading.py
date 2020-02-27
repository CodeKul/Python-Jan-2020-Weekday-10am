import shutil
import requests # pip install requests / pip3 install requests / python -m pip install requests
from threading import Thread
import time
 
def download_image(url, imagename):
    print(imagename + ' Download started ' + time.ctime(time.time()))
    response = requests.get(url, stream=True)
    with open(imagename, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    print(imagename + ' Download finished ' + time.ctime(time.time()))

url1 = 'https://vignette.wikia.nocookie.net/deathbattlefanon/images/b/b7/Epic_Iron_Man.png/revision/latest?cb=20150404070629'
url2 = 'https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/c/c0/AoU_Iron_Man_01.png/revision/latest?cb=20150309164237'
url3 = 'https://clipart.info/images/ccovers/1516940925ironman-png-33.png'

# download_image(url1,'ironMan1.png')
# download_image(url2,'ironMan2.png')
# download_image(url3,'ironMan3.png')

t1 = Thread(target=download_image, args=(url1,'ironMan1.png'))
t1.start()

t2 = Thread(target=download_image, args=(url2,'ironMan2.png'))
t2.start()

t3 = Thread(target=download_image, args=(url3,'ironMan3.png'))
t3.start()

print("Main Thread Exiting")
