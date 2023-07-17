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

    ax=plt.figure(figsize=(5,5)).add_subplot(111)
    hist_x = []
    for i in hindo_dict.values():
        hist_x.append(i)
    ax.hist(hist_x,range=(0,10000),log = True)

    # ax.hist(hist_x,bins = np.logspace(0, 5, 10),log = True)
    # ax.set_xscale('log')
    plt.show()

