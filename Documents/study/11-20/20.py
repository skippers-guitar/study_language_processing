import os

if __name__ == "__main__":

    dir = os.path.dirname(__file__)

    col1 = []
    result_list ={}

    with open(dir + 'popular-names.txt','r') as f:
        list = f.readlines()
        for l in list:
            line = l.split("\t")
            col1.append(line[0])

    for i in col1: 
        if not i in result_list.keys():
            result_list[i] = 1
        else:
            result_list[i] = result_list[i] + 1

    result_list = dict(sorted(result_list.items(), key=lambda t: t[1],reverse = True))
    for i in result_list.keys():
        print(i)

