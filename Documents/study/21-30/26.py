from os import path
import re
import file_reading as f_r

if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    art_text = f_r.text_get(file_json, "イギリス")    

    kisoinfo_text = f_r.kisoinfo(art_text)

    chikan_kekka = re.sub("'''","",kisoinfo_text)

    f_r.file_output(chikan_kekka,"26_chikan")
