import os

if __name__ == "__main__":

    col1 = []
    col2 = []

    dir = os.path.dirname(__file__)

    with open(dir + 'popular-names.txt','r') as f:
        list = f.readlines()
        for l in list:
            line = l.split("\t")
            col1.append(line[0])
            col2.append(line[1])

    with open(dir + "col1.txt",'w') as f1:
        f1.write('\n'.join(col1))        

    with open(dir + "col2.txt",'w') as f2:
        f2.write('\n'.join(col2))            

