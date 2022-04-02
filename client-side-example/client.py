import requests
import json

URL = "http://localhost/"
files = {'file': open('client-side-example\images.jpg', 'rb')}


a = requests.post(url=URL , files= files)
b = json.loads(a.content)
if b['isPutin']:
    print("Image is Putin")
else:
    print("Image not Putin")