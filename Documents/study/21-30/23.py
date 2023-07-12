import json
from os import path
import re
import file_reading as f_r

if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    text = f_r.text_get(file_json, "イギリス")    

    list = text.split("\n")

    result = []
    gyou_dict = {}
    for gyou in list:
        if re.match("^(?=.*==+[^=]*=+=).*$",gyou) != None:
            gyou_dict["text"] = re.match("==+([^=]*)=+=",gyou).group(1)
            hantei = re.match("=(=+)[^=]*=+=",gyou).group(1)
            gyou_dict["kaisou"] = len(hantei)
            result.append(gyou_dict)
            gyou_dict = {}
            
    print(result)

    for k in result:
        print(k["text"] + "の階層は" +str(k["kaisou"]))
