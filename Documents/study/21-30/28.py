from os import path
import re
import file_reading as f_r
    
def html_delete(str):
    str = re.sub('<[^>]*>',"",str,flags = re.DOTALL+re.MULTILINE)
    return(str)

def lang_delete(str):
    str = re.sub('\{\{lang\|[^\|]*\|(?P<lang_content>[^\|]+?)\}\}',"\g<lang_content>",str,flags = re.DOTALL+re.MULTILINE)
    return(str)
    
def indent_delete(str):
    str = re.sub('\*{1,5}',"",str,flags = re.DOTALL+re.MULTILINE)
    return(str)
    
if __name__ == "__main__":
    #文字列

    file_json = f_r.open_wiki()
    art_text = f_r.text_get(file_json, "イギリス")    

    kisoinfo_text = f_r.kisoinfo(art_text)

    result_emphasize_delete = f_r.emphasize_delete(kisoinfo_text)

    result_lang_delete = lang_delete(result_emphasize_delete)

    result_link_delete = f_r.link_delete(result_lang_delete)

    result_html_delete = html_delete(result_link_delete)
    
    result_indent_delete = indent_delete(result_html_delete)

    f_r.file_output(result_indent_delete,"28_chikan")

    result_library = f_r.kisoinfo_template_library(result_indent_delete)

    for i in result_library.items():
        print(i)        
