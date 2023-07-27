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
    al_chunk_dict = chmo.make_chunks_dict(al_chunk_ls)
    morphs_surface_dict = chmo.make_morphs_surface_dict(al_chunk_ls)
    for i in al_chunk_ls:
        for j in i:
            kakarimoto_surface = j.al_morphs_without_kigo()
            if j.out_dst() != '-1':
                kakarisaki_chunk = al_chunk_dict[j.out_dst()]
                kakarisaki_surface = kakarisaki_chunk.al_morphs_without_kigo()
            if j.check_al_morphs_pos("名詞") and kakarisaki_chunk.check_al_morphs_pos("動詞"):
                output += kakarimoto_surface + '\t' + kakarisaki_surface + '\n'
            kakarimoto_surface = ''
            kakarisaki_surface = ''
    prep.file_output(output,'output43.txt')
