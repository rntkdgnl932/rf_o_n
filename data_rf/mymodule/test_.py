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

    try:
        print("test")

        # tuto_start(cla)
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 500, 630, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)

        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\way\\right_1.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("right_1", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\attack\\auto_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("auto_on", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\attack\\auto_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("auto_off", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\quest_check\\quest_on_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_on_1", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\quest_check\\quest_on_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_on_2", imgs_)


    except Exception as e:
        print(e)