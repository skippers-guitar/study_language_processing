import os

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    col1 = []
    result_list =[]

    with open(dir + 'popular-names.txt','r') as f:
        list = f.readlines()
        for l in list:
            line = l.split("\t")
            col1.append(line[0])

    for i in col1: 
        if not i in result_list:
            result_list.append(i)

    result_list.sort()
    for i in result_list:
        print(i)

