
import os
import re

import id_info
import voice_info

path = "voice"
dir_voice = os.listdir(path)
all_char_info = []
for dir_char in dir_voice:
    who = re.findall(r'char_(\d+)', dir_char)

    if len(who) > 0:
        who_cn = id_info.id_info[who[0]][1]
        new_dir_char = os.path.join(path, "out", who_cn)
        os.makedirs(new_dir_char)
        list_voice = os.listdir(path + '\\' + dir_char)
        for one_voice in list_voice:
            c_id = re.findall(r'CN_(\d+)', one_voice)
            c_name = voice_info.voice_info[c_id[0]]
            newname = who_cn + "_" + c_name + ".wav"

            try:
                os.rename(os.path.join(path, dir_char, one_voice), os.path.join(path, "out",new_dir_char, newname))
            except FileExistsError:
                newname = newname.rstrip('.wav')
                newname +="_2.wav";
                os.rename(os.path.join(path, dir_char, one_voice), os.path.join(path, "out", new_dir_char,newname))
            print(newname + " is ok")

import os


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder!  ---"
