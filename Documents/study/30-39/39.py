from os import path
import numpy as np
import prepare as prep
import matplotlib.pyplot as plt
import json

if __name__ == "__main__":
    plt.rcParams['font.family'] = "meiryo"

    jsonfile_name = 'output30'
    keitaiso_json = prep.json_read(jsonfile_name)
    hindo_dict = prep.result_hindo_henkan_dict(prep.tango_dict(keitaiso_json))
    hindo_juni = prep.juni_dict(prep.sort_dict(hindo_dict))

    hindo_juni_list = list(hindo_juni.keys())
    hindo_num_list = [j_value for i_value in hindo_juni.values() for j_value in i_value.values()]

    ax=plt.figure(figsize=(5,5)).add_subplot(111)
    ax.scatter(hindo_juni_list,hindo_num_list)
    plt.xscale("log")
    plt.yscale("log")
    plt.show()
