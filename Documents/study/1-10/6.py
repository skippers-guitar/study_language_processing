import re

def ngram(list_1,num):
    list_len = len(list_1)
    result = [0]*(list_len-num+1)
    for i in range(list_len-num+1):
        result[i] = list_1[i:i+num]

    return result

if __name__ == "__main__":
    #文字列
    sentence = 'I am an NLPer'
    sentence_word = sentence.split()
    num = 2

    answer1 = ngram(sentence,num)
    answer2 = ngram(sentence_word,num)
    print(answer1)
    print(answer2)
