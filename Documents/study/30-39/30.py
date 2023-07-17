from os import path
import prepare as prep
import re
import json

def text_kakou(text):
    text = re.sub('(EOS|[\f])','',text)
    text = re.sub('(\n+)','\n',text)
    text = text.strip()
    return(text)

def keitaiso_yomikomi(text):
    kaigyou_split = text.split("\n")

    end_chr = []
    for index,i in enumerate(kaigyou_split):
        if i.split(',')[1] == '空白' or i.split(',')[1] == '句点':
            if i.split(',')[1] != '空白':            
                end_chr.append(index)
    sentence_list = []
    onesentence_list = []
    chr_library = {}
    for index,text in enumerate(kaigyou_split):
        result_bunkai = re.findall('(.*?)\t(.*?),(.*?),(?:.*?),(?:.*?),(?:.*?),(?:.*?),(.*?),.+', text)
    # ★表層形\t★品詞大分類,★品詞細分類,*,*,活用型,活用形,★見出し語,読み,意味情報
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
    # 1。\t2記号,3句点,4*,5*,6*,7*,8。,9。,10。
    # 1(/+?)\t2(.*?),3(.*?),4(?:.*?),5(?:.*?),6(?:.*?),7(?:.*?),8(.*?).+
        for i in result_bunkai:
            chr_library["surface"] = i[0] 
            chr_library["base"] = i[3] 
            chr_library["pos"] = i[1] 
            chr_library["pos1"] = i[2] 
            onesentence_list.append(chr_library)
            chr_library = {}
        if index in end_chr:
            sentence_list.append(onesentence_list)
            onesentence_list = []
    return(sentence_list)

def list_json_henkan(list):
    json = {}
    cnt = 0
    for i in list:
        lib = {}
        cnt2 = 0
        for j in i:
            lib[cnt2] = j
            cnt2 += 1
        json[str(cnt) + "行目"] = lib
        cnt += 1
    return(json)

if __name__ == "__main__":
    file_name = 'neko' 
    text = prep.open_mecab(file_name)
    
    text = text_kakou(text)
    result = keitaiso_yomikomi(text)
    
    result_json = prep.list_json_henkan_2(result)

    b = path.join(path.dirname(__file__), "output30.json")
    with open(b,'w',encoding='utf-8') as f2:    
        json.dump(result_json,f2,indent=4,ensure_ascii = False)




    