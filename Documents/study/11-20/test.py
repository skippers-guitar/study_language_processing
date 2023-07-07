import os

if __name__ == "__main__":

    col1 = []
    col2 = []

    dir = os.path.dirname(__file__)

    with open(dir + '/col1_sh.txt','r') as f1:
        content1 = f1.read()
        list1 = content1.split("\n")

    with open(dir + "/col1.txt",'r') as f2:
        content2 = f2.read()
        list2 = content2.split("\n")

    list3=[]

    if len(list1) == len(list2):
        for index in range(len(list1)):
            list3.append(list1[index] + "\t" + list2[index]) 

    with open(dir + "/merge.txt",'w') as f3:
        f3.write("\n".join(list3))

