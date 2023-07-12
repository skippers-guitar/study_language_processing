import json
from os import path
import re

def filter_not_empty(list_a):
    return filter(lambda x: len(x) > 0 , list_a)
    

def open_wiki():
    a = path.join(path.dirname(__file__), 'jawiki-country.json')

    with open(a,'r', encoding='utf-8') as f:
        json_lines = f.read().splitlines()
        json_lines = filter_not_empty(json_lines)
        
        result = [json.loads(j) for j in json_lines]
    return result

def text_get(wiki_list,title):
    flag = 0
    for i in wiki_list:
        if i.get("title") == title:
            result_2 = i.get("text")
            flag += 1

    if flag == 0:
        result_2 = "this title is not found."
    elif flag > 1:
        result_2 = "This title is duplicate."
    
    return (result_2)

def file_output(str,name):
    b = path.join(path.dirname(__file__), name + '.txt')
    with open(b,'w',encoding='utf-8') as f2:
        f2.write(str) 

def kisoinfo(art_text):
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
    return(art_text[kisoinfo_start_index:kisoinfo_end_index-1])

def kisoinfo_template_library(kisoinfo):
    find_kekka = re.findall("(?:\n\||^\|)(.+?)\s*\=\s*(.+?)(?:(?=\n\|)|(?=\n$))",kisoinfo,re.DOTALL)
    result = {}
    for i in find_kekka:
        result[i[0]] = i[1]
    return(result)

def emphasize_delete(str):
    return(re.sub(r"(\'{2,5})(?P<emphasize_content>.+?)(\'{2,5})","\g<emphasize_content>",str,flags = re.DOTALL+re.MULTILINE))

def link_delete(str):
    result = re.sub(r"\[\[(?:[^\|]+?\|)??(?P<link_content>[^\|]+?)\]\]",r"\g<link_content>",str,flags = re.DOTALL+re.MULTILINE)
    return(result)

def html_delete(str):
    str = re.sub('<[^>]*>',"",str,flags = re.DOTALL+re.MULTILINE)
    return(str)

def lang_delete(str):
    str = re.sub('\{\{lang\|[^\|]*\|(?P<lang_content>[^\|]+?)\}\}',"\g<lang_content>",str,flags = re.DOTALL+re.MULTILINE)
    return(str)
    
def indent_delete(str):
    str = re.sub('\*{1,5}',"",str,flags = re.DOTALL+re.MULTILINE)
    return(str)

if __name__ == "__main__":
    #文字列

    file_json = open_wiki()
    result = text_get(file_json, "イギリス")    

    file_output(result,"result")