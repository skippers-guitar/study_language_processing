def sentence_mix(sentence1,sentence2):
    len_sen1 = len(sentence1)
    len_sen2 = len(sentence2)

    i = 0
    cnt1 = 0
    cnt2 = 0

    new_sentence = ''

    while cnt1 < len_sen1 and cnt2 < len_sen2:
        if i % 2 == 0: 
            new_sentence = new_sentence + sentence1[cnt1]
            cnt1 += 1
        else:
            new_sentence = new_sentence + sentence2[cnt2]
            cnt2 += 1
        i += 1
    
    while cnt1 + cnt2 < len_sen1+len_sen2:
        if cnt1 < len_sen1:
            new_sentence = new_sentence + sentence1[cnt1]
            cnt1 += 1
        elif cnt2 < len_sen2:
            new_sentence = new_sentence + sentence2[cnt2]
            cnt2 += 1

    return new_sentence

if __name__ == "__main__":
    #文字列
    sentence1 = 'パトカーあああああああああああ'
    sentence2 = 'タクシーーーーーー'
    answer = sentence_mix(sentence1,sentence2)
    print(answer)