import re

def word_ini_library(sen,sp_num):
    sen = re.sub('[^A-Za-z0-9 ]','',sen)
    sen_list = sen.split()
    ini_libr={}
    for index,x in enumerate(sen_list):
        if index+1 in sp_num:
            ini_libr[x[0]]=index+1
        else:
            ini_libr[x[:2]]=index+1

    return ini_libr

if __name__ == "__main__":
    #文字列
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    special_number = [1, 5, 6, 7, 8, 9, 15, 16, 19]

    answer = word_ini_library(sentence,special_number)
    print(answer)