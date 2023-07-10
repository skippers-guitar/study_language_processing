import os
import numpy as np

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    with open(dir + 'popular-names.txt','r') as f:
        list = f.readlines()

    row = len(list)
    column = len(list[0].split("\t"))

    result_list = np.full((row,column),"a")
    result_list = result_list.astype("U10")

    j = 0
    for i in list:         
        result_list[j:j+1,:] = i.split("\t")
        j+=1

    # print(len(list))
    print(result_list[result_list[:,2].argsort()[::-1],:])
