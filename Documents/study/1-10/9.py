import random

def Typoglycemia(sen):
    word_list=sen.split()
    new_list=[]

    for wd in word_list:
        if len(wd) > 4:
            new_wd = wd[0] + ''.join(random.sample(wd[1:len(wd)-1],len(wd)-2)) + wd[len(wd)-1:]            
        else:
            new_wd = wd
        new_list.append(new_wd)

    answer = ' '.join(new_list)
    return answer

if __name__ == "__main__":
    #文字列
    sentence = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'
    print(sentence)
    answer = Typoglycemia(sentence)
    print(answer)
