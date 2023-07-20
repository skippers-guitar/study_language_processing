import CaboCha

c = CaboCha.Parser()
s = "鉛筆を使ってキャンパスに絵を描く"
tree = c.parse(s)
print(tree.toString(CaboCha.FORMAT_TREE))