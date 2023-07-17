from os import path
import prepare as prep
import re
import json

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

if __name__ == "__main__":
    # file_name = 'neko' 
    # text = prep.open_mecab(file_name)
    
    # text = prep.text_kakou(text)
    # result = prep.keitaiso_yomikomi(text)
    
    # result_json = prep.list_json_henkan(result)

    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)

    result_dict = prep.verv_list(keitaiso_json)

    prep.file_output_json(result_dict, jsonfile_name + '_31')

            





    