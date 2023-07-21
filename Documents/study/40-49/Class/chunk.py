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
    def al_morphs(self):
        str = ''
        for i in self.morphs:
            str += i.surface
        return(str)

