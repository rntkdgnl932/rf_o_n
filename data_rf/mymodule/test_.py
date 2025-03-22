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

    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_reg, macro_out, drag_pos, text_check_get_black_white
    from tuto import tuto_start, tuto_skip
    from action import confirm_all, juljun_off_setting, go_maul, attack_on
    from character_select_and_game_start import game_start_screen
    from schedule import myQuest_play_check
    from get_item import get_post, get_upjuk, get_event, get_item_start, get_sangjum_sohwan
    from game_check import out_check, move_check
    from boonhae_collection import collection_start
    from massenger import line_to_me
    from potion import potion_buy
    from jadong import jadong_in
    from clean_screen import clean_screen_start
    try:
        print("test")

        # data = "자동_[22/24]바이로사시추기지"
        #
        # jadong_in(cla, data)

        # clean_screen_start(cla)

        # attack_on(cla)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            clean = False
            print("close_1", imgs_)
            QTest.qWait(500)
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            clean = False
            print("close_2", imgs_)
            QTest.qWait(500)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            clean = False
            print("close_3", imgs_)

        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\not_sold_out.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(130, 140, 300, 250, cla, img, 0.9)
        # if imgs_ is not None and imgs_ != False:
        #     print("not_sold_out", imgs_)
        #
        #     x_reg = imgs_.x
        #     y_reg = imgs_.y
        #
        #     full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\can_not_buy_1.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_reg(x_reg, y_reg, x_reg + 100, y_reg + 100, cla, img, 0.8)
        #     if imgs_ is not None and imgs_ != False:
        #         print("can_not_buy_1", imgs_)
        #     else:
        #         full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\can_not_buy_2.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_reg(x_reg, y_reg, x_reg + 100, y_reg + 100, cla, img, 0.8)
        #         if imgs_ is not None and imgs_ != False:
        #             print("can_not_buy_2", imgs_)
        #         else:
        #             print("?????????????")


    except Exception as e:
        print(e)