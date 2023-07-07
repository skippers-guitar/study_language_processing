import sys
import os

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    tester = len(sys.argv)

    if len(sys.argv) > 1:
        head_row = sys.argv[1]
    else:
        print("引数がありません")
        sys.exit()

    output_line=[]

#   デバック用
#   print(type(head_row))
    # head_row = 2

    with open(dir + 'popular-names.txt','r') as f:
        list = f.readlines()
        for l in range(int(head_row)):
            output_line.append(list[l].replace("\n",""))
    with open(dir + 'head_list.txt','w') as f:
        f.write("\n".join(output_line))