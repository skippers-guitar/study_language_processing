def sentence_reverce(sentence):
    len_sen = len(sentence)
    i = 0
    for x in sentence:
        new_sentence = new_sentence & sentence[len_sen-i]
        i += 1

if __name__ == "__main__":
    #文字列
    sentence = 'stressed'

    answer = sentence_reverce(sentence)
    print(answer)