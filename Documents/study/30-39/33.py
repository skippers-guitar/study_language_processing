from os import path
import prepare as prep
import re
import json

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

if __name__ == "__main__":
    # file_name = 'neko' 
    # text = prep.open_mecab(file_name)
    
    # text = prep.text_kakou(text)
    # result = prep.keitaiso_yomikomi(text)
    
    # result_json = prep.list_json_henkan(result)

    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)

    result_dict = AnoB_list(keitaiso_json)

    prep.file_output_json(result_dict, jsonfile_name + '_33')

            





    