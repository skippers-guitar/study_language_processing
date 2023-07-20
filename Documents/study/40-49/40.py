import CaboCha
import MeCab
import re
import unicodedata
from os import path
import json
import prepare_40_49 as prep

class Morph:
    def __init__(self):
        self.surface = ''
        self.base = ''
        self.pos = ''
        self.pos1 = ''

    def __init__(self, sur='', ba='',po='',po1=''):
        self.surface = sur
        self.base = ba
        self.pos = po
        self.pos1 = po1

    def set(self, sur='', ba='',po='',po1=''):
        if a != '': 
            self.surface = sur
        if b != '': 
            self.base = ba
        if c != '': 
            self.pos = po
        if d != '': 
            self.pos1 = po1
            
    def print_morph(self):
        print("表層形=" + self.surface + ",基本形=" + self.base + ",品詞=" + self.pos + ",品詞細分類１=" + self.pos1 )

def morph_chushutsu(cabocha):
    cabocha_kaigyo = cabocha.split("\n")

    sentence = []
    all_sentence = []
    for kaigyo in cabocha_kaigyo:
    # ★表層形\t★品詞大分類,★品詞細分類,*,*,活用型,活用形,★見出し語,読み,意味情報
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
        # 基本形が収録されていない単語はコンマの数が異なるため例外処理
        if kaigyo.count(',') > 6:
            result_bunkai = re.findall('(.*?)\t(.*?),(.*?),(?:.*?),(?:.*?),(?:.*?),(?:.*?),(.*?),.+', kaigyo,flags = re.DOTALL+re.MULTILINE)
        else:
            result_bunkai = re.findall('(.*?)\t(.*?),(.*?),.+', kaigyo,flags = re.DOTALL+re.MULTILINE)
        #     print(kaigyo)
    # 抽出できなかった場合にループを飛ばす
        if result_bunkai == []:
            continue
    # findallのアウトプットは一つしか発見されなくてもリストで返されるため、リストごとに処理
    # 基本は１行に一つしか該当の記載は存在しないと想定される。
        for i in result_bunkai:
        # 基本形が存在しない場合があるため、例外処理
            if len(result_bunkai[0]) > 3:
                input = Morph(i[0],i[3],i[1],i[2])
            else:
                input = Morph(sur = i[0],po = i[1],po1 = i[2])
            sentence.append(input)
            if i[2] == "句点":
                all_sentence.append(sentence)
                sentence = []
    return(all_sentence)

if __name__ == "__main__":  
    filename = "ai.ja.txt.parsed"
    cabocha_txt = prep.open_txt(filename)
    result = morph_chushutsu(cabocha_txt)
    for i in result[0]:
        i.print_morph()