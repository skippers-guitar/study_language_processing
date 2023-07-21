import re
from os import path
import json
import prepare_40_49 as prep
import chunk_morph as chmo
from Class import morph as mor
from Class import chunk as chu

if __name__ == "__main__":  
    filename = "ai.ja.txt.parsed"
    al_chunk_ls = chmo.chunk_morph(filename)
    for i in al_chunk_ls:
        for j in i:
            i.al_morphs()
            print(i.index + " " + i.dst)    



