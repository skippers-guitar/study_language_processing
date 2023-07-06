import re

def word_len_list(sen):
    sen = re.sub('[^A-Za-z0-9 ]','',sen)
    sen_list = sen.split()
    app_list = [0] * len(sen_list)
    for index,x in enumerate(sen_list):
        app_list[index] = len(x)
    return app_list

if __name__ == "__main__":
    #文字列
    sentence = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'

    answer = word_len_list(sentence)
    print(answer)