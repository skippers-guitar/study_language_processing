from os import path
import re
import file_reading as f_r

def link_delete(str):
    result = re.sub(r"\[\[(?:[^\|]+?\|)??(?P<link_content>[^\|]+?)\]\]",r"\g<link_content>",str,flags = re.DOTALL+re.MULTILINE)
    return(result)
    
if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    art_text = f_r.text_get(file_json, "イギリス")    

    kisoinfo_text = f_r.kisoinfo(art_text)

    result_emphasize_delete = f_r.emphasize_delete(kisoinfo_text)

    result_link_delete = link_delete(result_emphasize_delete)

    f_r.file_output(result_link_delete,"27_chikan")

    result_library = f_r.kisoinfo_template_library(result_link_delete)

    for i in result_library.items():
        print(i)
