from os import path
import prepare as prep
import re
import json
import sys

def kensaku_1(keitaiso_json,kensaku):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1

    output = {}
    for i_key,i_value in keitaiso_json.items():
        for j_key,j_value in i_value.items():
            if j_value['surface'] == kensaku:
                if not kensaku in output.keys():
                    output[kensaku] = json.dumps(j_value,ensure_ascii = False) + "_" + i_key +"_" +j_key
                else:
                    output[kensaku] = output[kensaku] + "\r\n" +  "_" + i_key +"_" +j_key
    if output =={}:
        output[kensaku] =  "存在しません"

    return output[kensaku]

if __name__ == "__main__":

    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)

    if len(sys.argv) > 1:
        kensaku = sys.argv[1]
    else:
        print("引数がありません")
        sys.exit()

    prep.file_output(kensaku_1(keitaiso_json,kensaku), jsonfile_name + '_kensaku.txt')
