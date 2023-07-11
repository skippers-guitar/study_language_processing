from os import path
import re
import file_reading as f_r

if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    text = f_r.text_get(file_json, "イギリス")    

    list = text.split("\n")

    result = []

    for gyou in list:
        if re.match("^(?=.*(ファイル|file)\:[^/.]+\.(jpg|jpeg|mp3|mp4|ping|png)).*$",gyou) != None:    
            find_kekka = re.findall("(ファイル|file)\:([^/.]+\.(jpg|jpeg|mp3|mp4|ping|png))",gyou)
            # result.append(find_kekka[1])
            print(find_kekka)            

    print(result)

