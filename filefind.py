# SkillsForAll
# Python Essentials 2 - 4.4.8 LAB
# The os module: LAB

import os

def find(path, to_find):
    if not os.path.isdir(path):
        return

    for entry in os.listdir(path):
        new_path = path + "/" + entry

        if entry == to_find:
            print(new_path)
        find(new_path, to_find)
