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
    al_chunk_ls = chmo.chunk_morph(filename)
    morphs_surface_dict = chmo.make_morphs_surface_dict(al_chunk_ls)
    for i in al_chunk_ls:
        for j in i:
            kakarimoto = j.al_morphs_without_kigo()
            if j.out_dst() != '-1':
                kakarisaki = morphs_surface_dict[j.out_dst()]
            output += kakarimoto + '\t' + kakarisaki + '\n'
            kakarimoto = ''
            kakarisaki = ''
    prep.file_output(output,'output42.txt')



