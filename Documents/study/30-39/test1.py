from os import path
import prepare as prep
import re

if __name__ == "__main__":
    # 1。\t2記号,3句点,4*,5*,6*,7*,8。,9。,10。
    # 1(/+?)\t2(.*?),3(.*?),4(?:.*?),5(?:.*?),6(?:.*?),7(?:.*?),8(.*?).+
    # text = "。\t記号,句点,*,*,*,*,。,。,。"
    text = "。\t記号,句点,*,*,*,*,。,。,"
    result_bunkai = re.findall('(.*?)\t(.*?),(.*?),(?:.*?),(?:.*?),(?:.*?),(?:.*?),(.*?),.+', text)
    print(result_bunkai)