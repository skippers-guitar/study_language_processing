import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": "File:Billy_Tipton.jpg"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

print(PAGES.items())

# for k, v in PAGES.items():
#     print(v["title"] + " is uploaded by User:" + v["imageinfo"][0]["user"])