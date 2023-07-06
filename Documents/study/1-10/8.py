import re

def cipher(sen):
    new_sentence = ''
    for i in range(len(sen)):
        if re.match("[a-z]",sen[i]):
            ci_letter = chr(219-ord(sen[i]))
            new_sentence = new_sentence + ci_letter
        else:
            new_sentence = new_sentence + sen[i]

    return new_sentence

if __name__ == "__main__":
    #文字列
    sentence = 'fasdsfafsdfasffdasfa'
    answer1 = cipher(sentence)
    answer2 = cipher(answer1)
    print(answer1)
    print(answer2)