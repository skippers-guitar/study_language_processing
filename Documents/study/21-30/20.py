import json
from os import path

def filter_not_empty(list_a):
    return filter(lambda x: len(x) > 0 , list_a)
    

def open_wiki():

    # dir = os.path.dirname(__file__)
    a = path.join(path.dirname(__file__), 'jawiki-country.json')

    # with open(dir + '/jawiki-country.json','r', encoding='utf-8') as f:
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

if __name__ == "__main__":
    #文字列

    file_json = open_wiki()
    result = text_get(file_json, "イギリス")    
    print(result)
