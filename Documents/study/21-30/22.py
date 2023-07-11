import json
from os import path
import re
import file_reading as f_r

if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    text = f_r.text_get(file_json, "イギリス")    

    list = text.split("\n")
    print(len(list))

    result = [gyou for gyou in list if re.match('^(?=.*\[Category).*$',gyou) != None]

    for k in result:
        print(k)
