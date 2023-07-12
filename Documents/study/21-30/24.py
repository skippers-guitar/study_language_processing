from os import path
import re
import file_reading as f_r

if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    art_text = f_r.text_get(file_json, "イギリス")    

    result = []

    art_text = re.sub("\n", "", art_text)

    if re.match("^(?=.*(ファイル|file)\:[^/.]+\.(jpg|jpeg|mp3|mp4|ping|png)).*$",art_text) != None:    
        find_kekka = re.findall("(?:ファイル|file)\:([^/.]+\.(?:jpg|jpeg|mp3|mp4|ping|png))",art_text)

    for i in find_kekka:
        print(i)

