def sentence_reverce(sentence):
    i = 1
    len_sen = len(sentence)
    new_sentence = sentence[0]
    while i < len_sen:
        if i % 2 == 0:
            new_sentence = punew_sentence + sentence[i]
        i += 1

    return new_sentence

if __name__ == "__main__":
    #文字列
    sentence = 'パタトクカシーー'

    answer = sentence_reverce(sentence)
    print(answer)