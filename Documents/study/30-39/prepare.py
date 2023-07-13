import MeCab
import unicodedata
from os import path

def open_txt(str):
    a = path.join(path.dirname(__file__), str)

    with open(a,'r', encoding='utf-8') as f:
        result = f.read()
    return result

def to_unicode(text:str):
    return(unicodedata.normalize('NFKC',text))

def open_mecab(str):
    a = path.join(path.dirname(__file__), str + ".txt.mecab")

    with open(a,'r', encoding='utf-8') as f:
        result = f.read()
    return result

def file_output(aaa,name_type):
    b = path.join(path.dirname(__file__), name_type)
    with open(b,'w',encoding='utf-8') as f2:
        f2.write(aaa) 

def keitaiso_analysis(file):
    text = open_txt(file)
    mecab_mode = 'mecabrc'
    keitaiso = MeCab.Tagger(mecab_mode)
    node = keitaiso.parse(text)
    file_output(str(node),file + ".mecab")
    return(node)

if __name__ == "__main__":
    file = "neko_1.txt"
    output = keitaiso_analysis(file)
    # print(output)
