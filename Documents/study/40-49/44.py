
import re
from os import path
import json
import prepare_40_49 as prep
import chunk_morph as chmo
from Class import morph as mor
from Class import chunk as chu
import CaboCha
import graphviz

def chunk_morph(cabocha_txt):
    kakariukemoto_dic = chmo.index_kakariuke_chusyutsu(cabocha_txt)
    result1 = chmo.morph_chunkinfo_chushutsu(cabocha_txt)
    result2 = chmo.morph_chunk_seikei(result1,kakariukemoto_dic)
    return(result2)    

def chunks_graphviz_ls(al_chunk_dict):
    result = []
    for i_chunks in al_chunk_dict.values():        
        dst = i_chunks.out_dst()
        chunks_surface = i_chunks.al_morphs()
        if dst in al_chunk_dict.keys():
            dst_chunk_surface = al_chunk_dict[dst].al_morphs()
            result.append([chunks_surface,dst_chunk_surface])
    return(result)

if __name__ == "__main__":
    input_text = '人工知能（じんこうちのう、AI〈エーアイ〉）とは、「『計算（）』という概念と『コンピュータ（）』という道具を用いて『知能』を研究する計算機科学（）の一分野」を指す語。'
    c = CaboCha.Parser()
    tree = c.parse(input_text)
    c_lattice = tree.toString(CaboCha.FORMAT_LATTICE)
    al_chunk_ls = chunk_morph(c_lattice)
    al_chunk_dict = chmo.make_chunks_dict(al_chunk_ls)
    chunks_dict_chunks_ls = chunks_graphviz_ls(al_chunk_dict)

    dot = graphviz.Digraph()
    dot.attr('graph', layout='dot')
    dot.attr('node', shape='box', charset='utf-8',fontname='MS Gothic')
    j = 0
    for i in chunks_dict_chunks_ls:
        j +=1
        dot.edge(i[0],i[1],'Edge ' + str(j))

    dot.render('output44', view=True)

    # for i in al_chunk_ls:
    #     for j in range(len(i)):
    #         print(chmo.check_chunks_output_surface(al_chunk_ls,str(j)))
