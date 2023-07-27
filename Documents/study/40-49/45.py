import re
from os import path
import json
import prepare_40_49 as prep
import chunk_morph as chmo
from Class import morph as mor
from Class import chunk as chu

if __name__ == "__main__":  
    filename = "ai.ja.txt.parsed"
    output = ''
    kaku_ls = []
    result = ''

    al_chunk_ls = chmo.chunk_morph(filename)
    al_chunk_dict = chmo.make_chunks_dict(al_chunk_ls)
    for i in al_chunk_dict.values():
        if i.jutsugo_base() != "":
            result += i.jutsugo_base() + "\t"
            kaku_ls = i.kaku_surface(al_chunk_dict)
            kaku_ls.sort()
            if kaku_ls != []:
                for j in kaku_ls:
                    result += j + " "
            result.strip()
            result += "\n"
    result.strip()
    prep.file_output(result,'output45.txt')
