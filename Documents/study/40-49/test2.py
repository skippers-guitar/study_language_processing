import MeCab

mt = MeCab.Tagger("-Ochasen")
s = "私は人間です。"
result = mt.parse(s).split("\n")
for i in result:
    print(i)