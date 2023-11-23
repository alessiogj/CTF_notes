import requests
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract
from io import BytesIO
from PIL import ImageEnhance
import urllib.request as urllib2



# Creare una sessione persistente
session = requests.Session()

def estrai_testo_da_immagine(url_immagine):
    url_immagine_completo = 'http://captcha.challs.olicyber.it' + url_immagine

    print(f"URL immagine completo: {url_immagine_completo}")
    response = session.get(url_immagine_completo)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))

        # Esempio di pre-elaborazione per migliorare il contrasto
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(2.0)  # Aumenta il contrasto

        testo_estratto = pytesseract.image_to_string(img)
        print(f"Testo estratto: {testo_estratto}")
        return testo_estratto
    else:
        print(f"Errore nella richiesta dell'immagine: {response.status_code}")
        return None

def estrai_testo_dalla_pagina(url_pagina):
    response_html = session.get(url_pagina)
    if response_html.status_code == 200:
        soup = BeautifulSoup(response_html.text, 'html.parser')
        testo_pagina = soup.get_text()
        return testo_pagina
    else:
        print(f"Errore nella richiesta della pagina HTML: {response_html.status_code}")
        return None

def main():
    testo_pagina = 1
    url_html = "http://captcha.challs.olicyber.it/"
    flag = 1
    for _ in range(100):
        if testo_pagina:
            testo_pagina = estrai_testo_dalla_pagina(url_html)
            soup = BeautifulSoup(testo_pagina)
            tags=soup.findAll('img')
            print(f"Tag immagine: {tags}")
            if tags:
                url_immagine = tags[0]['src']
                print(f"URL immagine: {url_immagine}")
                testo_estratto = estrai_testo_da_immagine(url_immagine)

                if testo_estratto:
                    response = session.post(url_html, data={'input': testo_estratto, 'next': 'Next'})
                    if flag:
                        flag = 0
                        url_html += '/next'
                else:
                    print("Errore nell'estrazione del testo dall'immagine.")
        else:
            print("Errore nell'estrazione del testo dalla pagina HTML.")

    # Stampa il cookie di sessione alla fine dei 100 cicli
    cookie_di_sessione = session.cookies.get_dict()
    print(f"\nCookie di sessione alla fine dei 100 cicli: {cookie_di_sessione}")

if __name__ == "__main__":
    main()
