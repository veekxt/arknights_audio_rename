
import os
import re

import id_info
import voice_info

path = r"arknights_audio_voice"
dir_voice = os.listdir(path)
all_char_info = []
for dir_char in dir_voice:
    list_voice = os.listdir(path + '\\' + dir_char)
    for one_voice in list_voice:
        if '战斗' in one_voice:
            newname = one_voice.replace("战斗","行动")
            os.rename(os.path.join(path, dir_char, one_voice), os.path.join(path, dir_char, newname))
            print(os.path.join(path, dir_char, one_voice)," -> ", os.path.join(path, dir_char, newname))