import sys
import os

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    if len(sys.argv) > 1:
        tail_row = int(sys.argv[1])
    else:
        print("引数がありません")
        sys.exit()

    output_line=[]

#   デバック用
    # tail_row = 2
    # print(type(tail_row))

    with open(dir + 'popular-names.txt','r') as f:
        list = f.readlines()
        for l in range(len(list) - tail_row,len(list)):
            output_line.append(list[l].replace("\n",""))
    
    for s in output_line:
        print(s)
    # with open(dir + 'tail_list.txt','w') as f:
    #     f.write("\n".join(output_line))