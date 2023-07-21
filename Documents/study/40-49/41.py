import re
from os import path
import json
import prepare_40_49 as prep
from Class import morph as mor
from Class import chunk as chu

def index_kakaruke_chusyutsu(cabocha):
    cabocha_kaigyo = cabocha.split("\n")
    kakariukemoto_index_dic = {}

    for kaigyo in cabocha_kaigyo:
        result_bunsetsu = re.findall('^\* .*', kaigyo,flags = re.DOTALL+re.MULTILINE)
        if result_bunsetsu != []:
            bunsetsuinfo = kaigyo.split(" ")
            kakariuke_index = bunsetsuinfo[2].replace("D","")
            if kakariuke_index != '-1':
                if not kakariuke_index in kakariukemoto_index_dic.keys():
                    kakariukemoto_index_dic[kakariuke_index] = [bunsetsuinfo[1]]
                else:
                    kakariukemoto_index_dic[kakariuke_index].append(bunsetsuinfo[1])
    return(kakariukemoto_index_dic)

def morph_chunkinfo_chushutsu(cabocha):
    cabocha_kaigyo = cabocha.split("\n")

    bunsetsu_dic = {}
    sentence = []
    all_sentence = []
    kuten_flag = 0

    for kaigyo in cabocha_kaigyo:
    # ★表層形\t★品詞大分類,★品詞細分類,*,*,活用型,活用形,★見出し語,読み,意味情報
    # 表層形（surface），基本形（base），品詞（pos），品詞細分類1
        # 基本形が収録されていない単語はコンマの数が異なるため例外処理
        if kaigyo.count(',') > 6:
            result_bunkai = re.findall('(.*?)\t(.*?),(.*?),(?:.*?),(?:.*?),(?:.*?),(?:.*?),(.*?),.+', kaigyo,flags = re.DOTALL+re.MULTILINE)
        else:
            result_bunkai = re.findall('(.*?)\t(.*?),(.*?),.+', kaigyo,flags = re.DOTALL+re.MULTILINE)

        result_bunsetsu = re.findall('^\* .*', kaigyo,flags = re.DOTALL+re.MULTILINE)
        if result_bunsetsu != []:
            if bunsetsu_dic != {}:
                sentence.append(bunsetsu_dic)
            if kuten_flag > 0:
                all_sentence.append(sentence)
                sentence = []
                kuten_flag = 0
            bunsetsu_dic = {}
            bunsetsu_info = kaigyo
            bunsetsu_dic[bunsetsu_info] = []
        if result_bunkai == []:
            continue
    # result_bunkai[0]:基本は１行に一つしか該当の記載は存在しないと想定される。
        if len(result_bunkai[0]) > 3:
            input = mor.Morph(result_bunkai[0][0],result_bunkai[0][3],result_bunkai[0][1],result_bunkai[0][2])
    # 基本形が存在しない場合があるため、例外処理
        else:
            input = mor.Morph(sur = result_bunkai[0][0],po = result_bunkai[0][1],po1 = result_bunkai[0][2])
        bunsetsu_dic[bunsetsu_info].append(input)
        if result_bunkai[0][2] == "句点":
            kuten_flag = 1

    # 文章の一番最後の句点の処理
    if kuten_flag > 0:
        if bunsetsu_dic != {}:
            sentence.append(bunsetsu_dic)
            all_sentence.append(sentence)

    return(all_sentence)

# reusult_chusyutsuはmorph_chunkinfo_chushutsuの出力結果がinputされる。
# result_chusyutsu: [(全文)[(一文){(文節情報)...:[morphs]},{},...],[...]...]
# kakaruikemoto_dic: {文節インデックス:[係り受け元のインデックスリスト]}
def morph_chunk_seikei(result_chusyutsu,kakariukemoto_dic):
    sentence = []
    allsentence = []
    for i in result_chusyutsu:
        for j in i:
            for j_key,j_value in j.items():
                bunsetsuinfo = j_key.split(" ")
# 形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）
                j_morphs = j_value
                j_dst = bunsetsuinfo[2].replace("D","")
                if bunsetsuinfo[1] in kakariukemoto_dic.keys():
                    j_srcs = kakariukemoto_dic[bunsetsuinfo[1]]
                else:
                    j_srcs = ''
                j_index = bunsetsuinfo[1]
                input = chu.Chunk(j_morphs,j_dst,j_srcs, j_index)
            sentence.append(input)
        allsentence.append(sentence)
        sentence = []
    return(allsentence)

if __name__ == "__main__":  
    filename = "ai.ja.txt.parsed"
    cabocha_txt = prep.open_txt(filename)
    kakariukemoto_dic = index_kakaruke_chusyutsu(cabocha_txt)
    result1 = morph_chunkinfo_chushutsu(cabocha_txt)
    result2 = morph_chunk_seikei(result1,kakariukemoto_dic)
    for i in result2[0]:
        print(i.al_morphs())
        print(i.index + " " + i.dst)

