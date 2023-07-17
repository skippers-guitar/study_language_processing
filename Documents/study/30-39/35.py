from os import path
import prepare as prep
import re
import json

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

#結果を出現頻度に変換して出力
def sort_dict(input_dict):
    result_dict = {}
    result_list = sorted(input_dict.items(),key=lambda x: x[1],reverse=True)
    result_dict = {x: y for x, y in result_list}
    return(result_dict)

if __name__ == "__main__":

    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)

    result_tango_dict = tango_dict(keitaiso_json)
    result_hindo_dict = result_hindo_henkan_dict(result_tango_dict)
    result_dict = sort_dict(result_hindo_dict)
    # result_dict = dict((x, y) for x, y in result_sort)

    prep.file_output_json(result_dict, jsonfile_name + '_35')
    
