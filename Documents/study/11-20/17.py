import math
import sys
import os

def slice(list,n):
    #list:入力配列
    #n:分割数

    step = math.ceil(len(list)/n)
    result_list = [[step]]*n
    k = 0

    for i in range(0,len(list),step):
        for j in range(k*step,k*step+step):
            result_list[j][k].append(list[i:i + step])
        k += 1
    return result_list

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    # if len(sys.argv) > 1:
    #     bunkatsu = int(sys.argv[1])
    # else:
    #     print("引数がありません")
    #     sys.exit()

    output_line=[]

#   デバック用
    bunkatsu = 3

    with open(dir + 'popular-names.txt','r') as f:
        output_line = f.readlines()

    result = slice(output_line,bunkatsu)

    for i in range(bunkatsu):
        with open(dir + 'head_list' + str(i) + '.txt','w') as f:
            f.write(result[i])