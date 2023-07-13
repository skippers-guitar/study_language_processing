from os import path
import prepare as prep
import re

def text_kakou(text):
    text = re.sub('(EOS|[\t\f])','',text)
    text = re.sub('(\n+)','\n',text)
    text = text.strip()
    return(text)


if __name__ == "__main__":
    file_name = 'neko_10' 
    text = prep.open_mecab(file_name)
    
    text = text_kakou(text)
    kaigyou_split = text.split("\n")

    head_chr = [0]
    for index,i in enumerate(kaigyou_split):
        if i.split(',')[1] == '空白' or i.split(',')[1] == '句点':
            if i.split(',')[1] != '空白':            
                head_chr.append(index + 1)
    del head_chr[-1]

    all_sentence_list = [len(head_chr)]
    sentence_cnt = 0
    sentence_list = []
    chr_library = {}
    for index,i in enumerate(kaigyou_split):
        re.findall('(/+?)/t(.*?),(.*?),(?:.*?),(?:.*?),(?:.*?),(?:.*?),(.*?).+')
    # 表層形\t品詞大分類,品詞細分類,*,*,活用型,活用形,見出し語,読み,意味情報
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
    