import MeCab

mt = MeCab.Tagger("-Ochasen")
s = "ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。"
result = mt.parse(s).split("\n")
for i in result:
    print(i)