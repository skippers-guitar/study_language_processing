from os import path
import prepare as prep
import matplotlib.pyplot as plt
import json
    
def top10_dict(input_dict):
    cnt = 0
    top10_dict = {}
    for i_key, i_value in input_dict.items():
        top10_dict[cnt] = [i_key,i_value]
        cnt += 1
        if cnt >= 10:
            break
    return(top10_dict)

if __name__ == "__main__":
    plt.rcParams['font.family'] = "meiryo"

    jsonfile_name = 'output30_35'
    tango_hindo_json = prep.json_read(jsonfile_name)
    tango_hindo_10_dict = top10_dict(tango_hindo_json)

    x = list(tango_hindo_10_dict.keys())
    word = [k[0] for k in tango_hindo_10_dict.values()]
    height = [k[1] for k in tango_hindo_10_dict.values()]
    print(word)
    plt.bar(x,height,tick_label=word)
    plt.show()
    # prep.file_output_json(result_dict, jsonfile_name + '_35')

    