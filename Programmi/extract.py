from io import BytesIO
import requests
from bs4 import BeautifulSoup
import pytesseract
from PIL import Image

url = "http://captcha.challs.olicyber.it/"

#----------------------------------------------------#
#                                                    #
#   ore 1:44: flag{https://xkcd.com/233/?vjc1GpKF}   #
#   tutto sto casino per trovare un meme             #
#----------------------------------------------------#

# in realtà non serviva mandare un numero, perchè funzionava si ma se trovo un captcha con uno 0 iniziale mi taglia lo zero e fallisce la challenge
# andava aggiunto uno strip però perchè si vede che la stringa estratta dall'immagine conteneva degli spazi all'inizio o alla fine
def extract_number_from_image(img_url):
    response = requests.get(img_url)
    image = Image.open(BytesIO(response.content))
    text = pytesseract.image_to_string(image)
    return text.strip()


with requests.Session() as session:
    response = session.get(url)
    cookie_value = session.cookies.get_dict().get('session')

    
    for _ in range(100):
        # ALE: il problema era qua, ogni volta che fai session.get(url) ti cambia il cookie di sessione e quindi va affanculo tutto il resto
        #response = session.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        img_tags = soup.find_all("img")

        for img in img_tags:
            img_url = url + img_tags[0]["src"]
            print(img_url)
            number = extract_number_from_image(img_url)
            print(number)
            response = session.post(url+'/next', data={'risposta': number}, cookies={'session': cookie_value})
            print(response.text)
        
        



