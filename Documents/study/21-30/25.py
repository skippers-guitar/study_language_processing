from os import path
import re
import file_reading as f_r

if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    art_text = f_r.text_get(file_json, "イギリス")    

    result = []

    # art_text = re.sub("\n", "", art_text)

    kisoinfo_start_index = re.search("\{\{基礎情報", art_text).end()
    cnt = 0
    for i in range(kisoinfo_start_index,len(art_text)):
        if art_text[i] == "{":
            cnt += 1
        elif art_text[i] == "}":
            cnt += -1
        if cnt == -2:
            kisoinfo_end_index = i
            break
        
    kisoinfo = art_text[kisoinfo_start_index:kisoinfo_end_index-1]

    find_kekka = re.findall("(?:\n\||^\|)(.+?)\s*\=\s*(.+?)(?:(?=\n\|)|(?=\n$))",kisoinfo,re.DOTALL)

    result = {}
    for i in find_kekka:
        result[i[0]] = i[1]
    for j in result.items():
        print(j)
        
