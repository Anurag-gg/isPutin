import requests
import json

URL = "http://127.0.0.1:8000"
files = {'file': open('images.jpg', 'rb')}


a = requests.post(url=URL , files= files)
b = json.loads(a.content)
if b['isPutin']:
    print("Image is Putin")
else:
    print("Image not Putin")