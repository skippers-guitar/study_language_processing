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

def nC2(ls):
    output = []
    for index,value in enumerate(ls):
        for k in range(index+1,len(ls)):
            output.append([value,ls[k]])
    return(output)


def kaiki_dst_ls(index,sentence_index_ls,al_chunk_dict,output):
    if index in sentence_index_ls:
        output.append(index) 
        output = kaiki_dst_ls(al_chunk_dict[index].out_dst(),sentence_index_ls,al_chunk_dict,output)
    return(output)

def saitan_root_search_surface(index_X,index_Y,sentence_meishi_ne_dict,al_chunk_dict):
    output = ''
    flag = 0
    X_ls = sentence_meishi_ne_dict[index_X]
    Y_ls = sentence_meishi_ne_dict[index_Y]
    output_X_index = []
    output_Y_index = []
    for i in range(len(Y_ls)):
        for j in range(len(X_ls)):
            if X_ls[j] == Y_ls[i]:
                output_X_index = X_ls[0:j+1]
                output_Y_index = Y_ls[0:i+1]
                flag = 1
                break
        if flag == 1:
            break
    output_X_surface_ls = [al_chunk_dict[k].al_morphs() for k in output_X_index]
    output_Y_surface_ls = [al_chunk_dict[l].al_morphs() for l in output_Y_index]
    output_X_surface_ls[0] = al_chunk_dict[output_X_index[0]].meishi_chikan_surface('X')
    output_Y_surface_ls[0] = al_chunk_dict[output_Y_index[0]].meishi_chikan_surface('Y')

    output = ' -> '.join(output_X_surface_ls[0:len(output_X_surface_ls)-1])
    if len(output_Y_surface_ls) > 1:
        output += ' | ' + ' -> '.join(output_Y_surface_ls[0:len(output_Y_surface_ls)-1]) + ' | ' + output_Y_surface_ls[len(output_Y_surface_ls)-1]
    else:
        output += ' -> ' + output_Y_surface_ls[0]

    return(output)    

if __name__ == "__main__":  
    output = ''
    sentence_index_ls = []
    meishi_ls = []
    meishi_ne_dict = {}
    al_meishi_ne_ls = []

    input_text = 'ジョン・マッカーシーはAIに関する最初の会議で人工知能という用語を作り出した。'
    c = CaboCha.Parser()
    tree = c.parse(input_text)
    c_lattice = tree.toString(CaboCha.FORMAT_LATTICE)
    al_chunk_ls = chmo.chunk_morph_text(c_lattice)
    al_chunk_dict = chmo.make_chunks_dict(al_chunk_ls)
    for i in al_chunk_ls:
        sentence_index_ls = sentence_index_ls_output(i)
        for j in i:
            if j.meishi_surface() != "":
                meishi_ls = []
                meishi_ne_dict[j.out_index()] = kaiki_dst_ls(j.out_index(),sentence_index_ls,al_chunk_dict,meishi_ls)
        al_meishi_ne_ls.append(meishi_ne_dict)
    
    for sentence_meishi_ne_dict in al_meishi_ne_ls:
        meishi_ls = list(sentence_meishi_ne_dict.keys())
        meishi_pair = nC2(meishi_ls)
        for j in meishi_pair:
            index_X = j[0]
            index_Y = j[1]
            output += saitan_root_search_surface(index_X,index_Y,sentence_meishi_ne_dict,al_chunk_dict) + '\n'
        output = output.strip()
    
    print(output)

    prep.file_output(output,'output49.txt') 
                
