import CaboCha
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

"テキストファイルを開く"
def file_output(aaa,name_type):
    b = path.join(path.dirname(__file__), name_type)
    with open(b,'w',encoding='utf-8') as f2:
        f2.write(aaa) 

if __name__ == "__main__":
    filename = 'ai.ja\\ai.ja.txt'
    input_text = open_txt(filename)
    c = CaboCha.Parser()
    tree = c.parse(input_text)
    # print(type(tree.toString(CaboCha.FORMAT_TREE))))
    file_output(tree.toString(CaboCha.FORMAT_LATTICE),'ai.ja.txt.parsed')
