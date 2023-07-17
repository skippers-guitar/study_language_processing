import MeCab
import re
import unicodedata
from os import path
import json

"テキストファイルを開く"
def open_txt(str):
    a = path.join(path.dirname(__file__), str)

    with open(a,'r', encoding='utf-8') as f:
        result = f.read()
    return result

#unicodeを標準化
def to_unicode(text:str):
    return(unicodedata.normalize('NFKC',text))

#mecabファイルを開く
def open_mecab(str):
    a = path.join(path.dirname(__file__), str + ".txt.mecab")

    with open(a,'r', encoding='utf-8') as f:
        result = f.read()
    return result

#jsonファイルを開く
def json_read(file):
    a = path.join(path.dirname(__file__), file + ".json")

    with open(a,'r', encoding='utf-8') as f:
        result = json.load(f)
    return(result)

#ファイルを出力
def file_output(aaa,name_type):
    b = path.join(path.dirname(__file__), name_type)
    with open(b,'w',encoding='utf-8') as f2:
        f2.write(aaa) 

#ファイルを出力（追記モード）
def file_output_tuiki(aaa,name_type):
    b = path.join(path.dirname(__file__), name_type)
    with open(b,'a',encoding='utf-8') as f2:
        f2.write(aaa) 

#libraryをjsonに変換して出力
def file_output_json(json_content,name):
    b = path.join(path.dirname(__file__), name + ".json")
    with open(b,'w',encoding='utf-8') as f2:    
        json.dump(json_content,f2,indent=4,ensure_ascii = False)

#リストをjsonで出力できる形式(dictionary)に変換_階層は２つまで
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

#リストをjsonで出力できる形式(dictionary)に変換_汎用型
# 出力結果{key->文番号:val->{key->形態素番号:val->{形態素解析結果}}}
def list_json_henkan_2(list_input):
    dict_input = {}
    cnt = 0
    for i in list_input:
        if isinstance(i,list):
            i = list_json_henkan_2(i)            
        dict_input[cnt] = i
        cnt += 1    
    return(dict_input)

#Mecabにより解析（ー＞parseファイルで出力（形態素ごとに１行））
def keitaiso_analysis(file):
    text = open_txt(file)
    mecab_mode = 'mecabrc'
    keitaiso = MeCab.Tagger(mecab_mode)
    node = keitaiso.parse(text)
    file_output(str(node),file + ".mecab")
    return(node)

#空白や空行を削除
def text_kakou(text):
    text = re.sub('(EOS|[\f])','',text)
    text = re.sub('(\n+)','\n',text)
    text = text.strip()
    return(text)

#解析後のmecabファイルをリスト形式で出力
def keitaiso_yomikomi(text):
    text = re.sub('(EOS|[\f])','',text)
    text = re.sub('(\n+)','\n',text)
    text = text.strip()

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


#動詞の表層形を抽出した辞書型配列を出力
def verv_list(keitaiso_json):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1

    result_dict = {}
    for i_key,i_value in keitaiso_json.items():
        for j_key,j_value in i_value.items():
            if j_value['pos'] == '動詞' :
                if not j_value['surface'] in result_dict.keys():
                    result_dict[j_value['surface']] = j_value['base']+'_'+i_key+'_'+j_key
                else:
                    result_dict[j_value['surface']] = result_dict[j_value['surface']]+'/'+j_value['base']+'_'+i_key+'_'+j_key
    return(result_dict)

#動詞の基本形を抽出した辞書型配列を出力
def verv_kihon_list(keitaiso_json):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
    # jsonfileのフォーマット,1階層（文番号）、2階層（文字番号）、3階層（形態素解析結果）
    
    result_dict = {}
    for i_key,i_value in keitaiso_json.items():
        for j_key,j_value in i_value.items():
            if j_value['pos'] == '動詞' :
                if not j_value['base'] in result_dict.keys():
                    result_dict[j_value['base']] = i_key+'_'+j_key
                else:
                    result_dict[j_value['base']] = result_dict[j_value['base']]+'/'+i_key+'_'+j_key
    return(result_dict)

#2つの名詞が「の」で連結されている名詞句を抽出した辞書型配列を出力
def AnoB_list(keitaiso_json):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1

    result_dict = {}
    # jsonfileのフォーマット,1階層（文番号）、2階層（文字番号）、3階層（形態素解析結果）
    for i_key,i_value in keitaiso_json.items():
        for j_key,j_value in i_value.items():
            if int(j_key)+2 < len(i_value.keys()):
                if j_value['pos'] == '名詞' and \
                i_value[str(int(j_key) + 1)]['surface'] == 'の' and \
                i_value[str(int(j_key) + 2)]['pos'] == '名詞':
                    meishiku = j_value['surface'] + i_value[str(int(j_key) + 1)]['surface'] + i_value[str(int(j_key) + 2)]['surface']
                    if not meishiku in result_dict.keys():
                        result_dict[meishiku] = i_key+'_'+j_key
                    else:
                        result_dict[meishiku] = result_dict[meishiku]+'/'+i_key+'_'+j_key
    return(result_dict)

#名詞の連接（連続して出現する名詞）を最長一致で抽出し、辞書型で出力
def meishi_rensetsu_dict(keitaiso_json):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
    # jsonfileのフォーマット,1階層（文番号）、2階層（文字番号）、3階層（形態素解析結果）

    result_dict = {}
    cnt = 0
    meishi_rensetsu = ''
    meishi_rensetsu_no = 0

    for i_key,i_value in keitaiso_json.items():        
        for j_key,j_value in i_value.items():
            if j_value['pos'] == "名詞":
                meishi_rensetsu += j_value['surface'] 
                if cnt == 0:
                    meishi_rensetsu_no = i_key + '_' + j_key
                cnt += 1
            else:
                if cnt > 1:
                    if not meishi_rensetsu in result_dict.keys():
                        result_dict[meishi_rensetsu] = meishi_rensetsu_no
                    else:
                        result_dict[meishi_rensetsu] += "/" + meishi_rensetsu_no
                meishi_rensetsu = ''
                meishi_rensetsu_no = 0
                cnt = 0

    return(result_dict)

# 共起の結果を出力(入力は基となるjsonファイル、共起の対象となるワード、n-gramのn数)
# 出力結果{key->単語:val->出現回数}
def cooccurrence(sentence_json,word,input_n):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1

    cooccurence_word_dict = {}
    for i_key,i_value in sentence_json.items():
        for j_key,j_value in i_value.items():
            if j_value["surface"] != word:
                continue
            for n in range(input_n):
                sentence_num = int(j_key) - (n + 1)
                if sentence_num > 0:
                    if not i_value[str(sentence_num)]['surface'] in cooccurence_word_dict.keys():
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] = 1
                    else:
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] += 1
                sentence_num = int(j_key) + (n + 1)
                if sentence_num < len(i_value.keys()):
                    if not i_value[str(sentence_num)]['surface'] in cooccurence_word_dict.keys():
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] = 1
                    else:
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] += 1
    return(cooccurence_word_dict)    


#文番号を基に文を抽出
def sentence_output(keitaiso_json,sentence_num):
    result_str = ""
    for i_key,i_value in keitaiso_json.items():        
        if i_key == str(sentence_num):
            for j_value in i_value.values():
                result_str += j_value["surface"]
    return(result_str)

#各単語の表層形を抽出した辞書型配列を出力
def tango_dict(keitaiso_json):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
    # jsonfileのフォーマット,1階層（文番号）、2階層（文字番号）、3階層（形態素解析結果）
    # 出力形式はkeyが単語、valueが(文番号)_(文字番号)/(文番号)_(文字番号)...

    result_dict = {}
    for i_key,i_value in keitaiso_json.items():
        for j_key,j_value in i_value.items():
            if not j_value['surface'] in result_dict.keys():
                result_dict[j_value['surface']] = j_value['base']+'_'+i_key+'_'+j_key
            else:
                result_dict[j_value['surface']] += '/'+j_value['base']+'_'+i_key+'_'+j_key
    return(result_dict)

#結果を出現頻度に変換して出力
def result_hindo_henkan_dict(tango_pre_dict):
    result_dict = {}
    for i_key,i_value in tango_pre_dict.items():
        result_dict[i_key] = len(i_value.split("/")) + 1
    return(result_dict)

#辞書型配列をソート
def sort_dict(input_dict):
    result_dict = {}
    result_list = sorted(input_dict.items(),key=lambda x: x[1],reverse=True)
    result_dict = {x: y for x, y in result_list}
    return(result_dict)

def top10_dict(input_dict):
    cnt = 0
    top10_dict = {}
    for i_key, i_value in input_dict.items():
        top10_dict[cnt] = {i_key:i_value}
        cnt += 1
        if cnt >= 10:
            break
    return(top10_dict)

def juni_dict(input_dict,size = -1):
    cnt = 0
    top_dict = {}
    if size == -1:
        size = len(input_dict.keys())
    result_list = sorted(input_dict.items(),key=lambda x: x[1],reverse=True)
    result_dict = {x: y for x, y in result_list}
    pre_i_value = ""
    for i_key, i_value in result_dict.items():
        cnt += 1
        if i_value == pre_i_value:
            top_dict[doujuni] = {i_key:i_value}
        else:
            top_dict[cnt] = {i_key:i_value}
            doujuni = cnt
        pre_i_value = i_value
        if cnt >= size:
            break
    return(top_dict)

# if __name__ == "__main__":
#     # test = {}
#     # print(test.type())