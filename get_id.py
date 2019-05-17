import os
import re

path = "char_module"
files = os.listdir(path)
all_char_info = []
for file in files:
    if not os.path.isdir(file):
        f = open(path + "/" + file, encoding='UTF-8');
        iter_f = iter(f);
        str = ""
        for line in iter_f:
            str = str + line
        all_char_info.append(str)
char_co = {}
str_co = ""
for char_info in all_char_info:
    c_id = re.findall(r'id = "(\d+)"', char_info)
    c_cn_name = re.findall(r'cn = "(.*)"', char_info)
    c_en_name = re.findall(r'en = "(.*)"', char_info)
    char_co[c_id[0]] = (c_en_name[0], c_cn_name[0])
    str_co += "'%s': ('%s', '%s'),\n" % (c_id[0], c_en_name[0], c_cn_name[0])
print(str_co)

