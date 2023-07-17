from os import path
import prepare as prep
import re
import json

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

if __name__ == "__main__":


    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)

    result_dict = meishi_rensetsu_dict(keitaiso_json)

    prep.file_output_json(result_dict, jsonfile_name + '_34')

            





    