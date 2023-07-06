def sentence_reverce(sentence):
    len_sen = len(sentence)
    i = 0
    new_sentence = ''
    for x in sentence:
        if i == 0:
            new_sentence = sentence[len_sen-i-1]
        else:
            new_sentence = new_sentence + sentence[len_sen-i-1]
        i += 1
    return new_sentence

if __name__ == "__main__":
    #文字列
    sentence = 'stressed'

    answer = sentence_reverce(sentence)
    print(answer)