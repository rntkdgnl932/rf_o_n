import sys
import os
import time
import requests
from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random


    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    from function_game import imgs_set_, click_pos_2
    from tuto import tuto_start
    from action import confirm_all
    from character_select_and_game_start import game_start_screen

    try:
        print("test")

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\jangsigan_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 500, 500, 600, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan_1", imgs_)
            confirm_all(cla)
            time.sleep(1)
        result_schedule = myQuest_play_check(cla, "check")
        print("result_schedule", result_schedule)
        character_id = result_schedule[0][1]
        result_schedule_ = result_schedule[0][2]
        game_start_screen(cla,character_id)


    except Exception as e:
        print(e)