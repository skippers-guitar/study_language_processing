import re
from os import path
import json
import prepare_40_49 as prep
import chunk_morph as chmo
from Class import morph as mor
from Class import chunk as chu
import CaboCha

def sentence_index_ls_output(chunk_ls):
    output = []
    for i in chunk_ls:
        output.append(i.out_index())
    return(output)

def kaiki_dst(index,output,sentence_index_ls,al_chunk_dict):
    if al_chunk_dict[index].out_dst() in sentence_index_ls:
        output += al_chunk_dict[index].al_morphs() + ' -> ' 
        output = kaiki_dst(al_chunk_dict[index].out_dst(),output,sentence_index_ls,al_chunk_dict)
    else:
        output += al_chunk_dict[index].al_morphs()
    return(output)


if __name__ == "__main__":  
    sentence_index_ls = []
    meishi_ne = ''
    output = ''

    input_text = 'ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。'
    c = CaboCha.Parser()
    tree = c.parse(input_text)
    c_lattice = tree.toString(CaboCha.FORMAT_LATTICE)
    al_chunk_ls = chmo.chunk_morph_text(c_lattice)
    al_chunk_dict = chmo.make_chunks_dict(al_chunk_ls)
    for i in al_chunk_ls:
        print(len(al_chunk_ls))
        sentence_index_ls = sentence_index_ls_output(i)
        for j in i:
            if j.meishi_surface() != "":
                meishi_ne = kaiki_dst(j.out_index(),meishi_ne,sentence_index_ls,al_chunk_dict)
                output += meishi_ne + '\n'
                meishi_ne = ''
    output = output.strip()

    prep.file_output(output,'output48_2.txt') 
