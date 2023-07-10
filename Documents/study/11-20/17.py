import math
import sys
import os

def slice(list,n):
    #list:入力配列
    #n:分割数

    step = math.ceil(len(list)/n)
    bunkatsu_list = []
    result_list = {}
    k = 0

    for i in range(n):
        for j in range(i*step,i*step+step):
            if j < len(list):
                bunkatsu_list.append(list[j])
        result_list[str(i+1)] = bunkatsu_list
        bunkatsu_list=[]

    return result_list

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    if len(sys.argv) > 1:
        bunkatsu = int(sys.argv[1])
    else:
        print("引数がありません")
        sys.exit()

    output_line=[]

#   デバック用
#   bunkatsu = 3

    with open(dir + 'popular-names.txt','r') as f:
        output_line = f.readlines()

    result = slice(output_line,bunkatsu)

    for i in result.keys():
        with open(dir + 'bunkatsu_list' + str(i) + '.txt','w') as f:
            f.write("".join(result[i]))
