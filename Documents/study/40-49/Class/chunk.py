import pandas as pd

"""
このクラスは
形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），
係り元文節インデックス番号のリスト（srcs）
文節のインデックス番号（index）
をメンバ変数に持つ
"""

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = ''
        self.srcs = []
        self.index = ''

    def __init__(self, mors=[], dst='',srcs=[],ind = ''):
        self.morphs = mors
        self.dst = dst
        self.srcs = srcs
        self.index = ind

    def set(self, mors=[], dst='',srcs=[],ind = ''):
        if mors != []: 
            self.morphs = mors
        if dst != '': 
            self.dst = dst
        if srcs != []: 
            self.srcs = srcs
        if ind != '': 
            self.index = ind
            
    def print_morphs(self):
        print(self.morphs)
    def print_dst(self):
        print(self.dst)
    def print_srcs(self):
        print(self.srcs)                
    def print_index(self):
        print(self.index)                


    def out_morphs(self):
        return(self.morphs)
# 文節の表層形を出力
    def al_morphs(self):
        str = ''
        for i in self.morphs:
            str += i.surface
        return(str)    
#記号以外の文節の表層形を出力
    def al_morphs_without_kigo(self):
        str = ''
        for i in self.morphs:
            if i.pos != '記号':
                str += i.surface
        return(str)
    def check_al_morphs_pos(self,input):
        result = False
        for i in self.morphs:
            if i.pos == input:
                result = True
        return(result)
    def check_al_morphs_pos1(self,input):
        result = False
        for i in self.morphs:
            if i.pos1 == input:
                result = True
        return(result)

    def out_index(self):
        return(self.index)
    def out_dst(self):
        return(self.dst)

    def check_index(self,idx):
        if self.index == idx:
            return(True)
        else:
            return(False)

    def jutsugo_base(self):
        for i in self.morphs:
            if i.pos == '動詞':
                return(i.base)
                break
        return("")

    def meishi_surface(self):
        for i in self.morphs:
            if i.pos == '名詞':
                return(self.al_morphs())
                break
        return("")
    
    def sahen_jutsugo_base(self,chunks_dic):
        result = ""
        for i in self.morphs:
            if i.pos != '動詞':
                continue
            for j in self.srcs:
                for k in range(len(chunks_dic[j].morphs)):
                    if k + 1 >= len(chunks_dic[j].morphs):
                        break
                    if chunks_dic[j].morphs[k].pos == "名詞" and chunks_dic[j].morphs[k+1].pos == "助詞" and chunks_dic[j].morphs[k+1].surface == "を":
                        result = chunks_dic[j].morphs[k].surface + chunks_dic[j].morphs[k+1].surface + i.base
        return(result)
    
    def kaku_surface(self,chunks_dic):
        result_kaku_ls = []
        for i in self.srcs:
            for j in chunks_dic[i].morphs:
                if j.pos == '助詞':
                    result_kaku_ls.append(j.base)
        return(result_kaku_ls)
    
    def kaku_kou_surface_sort(self,chunks_dic):
        result_kaku_ls = []
        __kaku_info_ls = []
        for i in self.srcs:
            for j in chunks_dic[i].morphs:
                if j.pos == '助詞':
                    __kaku_info_ls.append([j.base,chunks_dic[i].al_morphs()])
        __df = pd.DataFrame(__kaku_info_ls,columns =['joshi_surface','index'])
        __df = __df.sort_values(by = ['joshi_surface'])
        __df = __df.transpose()
        result_kaku_ls = __df.values.tolist()
        return(result_kaku_ls)

    def meishi_chikan_surface(self,chikango):
        output = ''
        __meishi_flag = 0
        for i in self.morphs:
            if i.pos == '名詞':
                __meishi_flag = 1
            elif __meishi_flag == 1 :
                if i.pos == '助詞' or i.pos == '助動詞':
                    output += chikango + i.surface
                    __meishi_flag = 0
            else:
                output += i.surface
        if __meishi_flag == 1:
            output += chikango
        return(output)






