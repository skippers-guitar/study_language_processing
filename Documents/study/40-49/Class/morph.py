# 表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）

class Morph:
    def __init__(self):
        self.surface = ''
        self.base = ''
        self.pos = ''
        self.pos1 = ''

    def __init__(self, sur='', ba='',po='',po1=''):
        self.surface = sur
        self.base = ba
        self.pos = po
        self.pos1 = po1

    def set(self, sur='', ba='',po='',po1=''):
        if sur != '': 
            self.surface = sur
        if ba != '': 
            self.base = ba
        if po != '': 
            self.pos = po
        if po1 != '': 
            self.pos1 = po1
            
    def print_morph(self):
        print("表層形=" + self.surface + ",基本形=" + self.base + ",品詞=" + self.pos + ",品詞細分類１=" + self.pos1 )
