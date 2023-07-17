from os import path
import prepare as prep
import matplotlib.pyplot as plt
import json

# 共起の結果を出力
# 出力結果{key->単語:val->出現回数}
def cooccurrence(sentence_json,word,input_n):
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1

    cooccurence_word_dict = {}
    for i_key,i_value in sentence_json.items():
        for j_key,j_value in i_value.items():
            if j_value["surface"] != word:
                continue
            for n in range(input_n):
                sentence_num = int(j_key) - (n + 1)
                if sentence_num > 0:
                    if not i_value[str(sentence_num)]['surface'] in cooccurence_word_dict.keys():
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] = 1
                    else:
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] += 1
                sentence_num = int(j_key) + (n + 1)
                if sentence_num < len(i_value.keys()):
                    if not i_value[str(sentence_num)]['surface'] in cooccurence_word_dict.keys():
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] = 1
                    else:
                        cooccurence_word_dict[i_value[str(sentence_num)]['surface']] += 1
    return(cooccurence_word_dict)    

if __name__ == "__main__":
    plt.rcParams['font.family'] = "meiryo"

    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)
    result_cooccurence = cooccurrence(keitaiso_json,"猫",3)
    result_cooccurence = prep.sort_dict(result_cooccurence)
    result_cooccurence_10 = prep.top10_dict(result_cooccurence)

    x = list(result_cooccurence_10.keys())
    word = [l_key for k_value in result_cooccurence_10.values() for l_key in k_value.keys()]
    height = [l_value for k_value  in result_cooccurence_10.values() for l_value in k_value.values()]
    plt.bar(x,height,tick_label=word)
    plt.show()
    # prep.file_output_json(result_dict, jsonfile_name + '_35')




    