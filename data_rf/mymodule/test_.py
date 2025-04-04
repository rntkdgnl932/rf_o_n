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

    from datetime import datetime
    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_reg, macro_out, drag_pos, text_check_get_black_white, imgs_set_for
    from tuto import tuto_start, tuto_skip
    from action import confirm_all, juljun_off_setting, go_maul, attack_on, juljun_check
    from character_select_and_game_start import game_start_screen
    from schedule import myQuest_play_check
    from get_item import get_post, get_upjuk, get_event, get_item_start, get_sangjum_sohwan, allget_btn_click, get_sangjum_sohwan_start
    from game_check import out_check, move_check, attack_check
    from boonhae_collection import collection_start, boonhae_go, boonhae_collection_start, collection_go
    from massenger import line_to_me
    from potion import potion_buy
    from jadong import jadong_in, jadong_mode
    from clean_screen import clean_screen_start
    from dead_die import dead_check
    from auction_game import auction_low_num, auction_qun_num, auction_start
    from mission import mission_get, mission_get_des

    try:
        print("test")

        # data = "자동_[22/24]바이로사시추기지"
        #
        # jadong_in(cla, data)

        # clean_screen_start(cla)

        # attack_on(cla)
        # a = 33
        # b = 125
        # c = 135
        # d = 155
        #
        # pos = (a + plus, b, c - a, d - b)
        # pyautogui.screenshot("asd.png", region=pos)

        # get_sangjum_sohwan_start(cla)
        # nowMinute = datetime.today().strftime("%Y%m%d_%H:%M:%S")
        # print("nowMinute", nowMinute)
        #
        # v_.dead_count_msg += str(nowMinute) + "//"
        #
        # why = "하루 5번 죽었다 \n" + v_.dead_count_msg
        # line_to_me(cla, why)
        #
        # print("nowMinute", nowMinute)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\out_complete_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(450, 450, 530, 500, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_complete_2", imgs_)

        # mission_get(cla)

        # print("가격 읽어오고 팔자")
        # result_low = auction_low_num(cla)
        # print("==========================================================================")
        #
        # result_qun = auction_qun_num(cla, 605, 640)
        #
        # result_ = int(result_low * result_qun)
        #
        # print("==========================================================================")
        #
        # print("result_result_result_result_result_result_result_result_result_", result_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\googa_out_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(710, 100, 745, 175, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("googa_out_btn", imgs_)

        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\soolock_mission_checked.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_for(40, 150, 270, 860, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("soolock_mission_checked", imgs_)
        #
        #     if len(imgs_) > 0:
        #         y_reg = imgs_[len(imgs_) - 1][1]
        #         print("y_reg", y_reg)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 500, 700, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)


        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\out_zero.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(230, 980, 280, 1035, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("out_zero", imgs_)
        #     need_potion = True
        #
        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\out_zero_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(230, 980, 280, 1035, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("out_zero_2", imgs_)
        #     need_potion = True
        #
        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\juljun_zero.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(250, 970, 305, 1035, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("juljun_zero", imgs_)
        #     need_potion = True
        #
        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\juljun_zero_2.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(250, 970, 305, 1035, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("juljun_zero_2", imgs_)
        #     need_potion = True

        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\out_zero.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(230, 980, 280, 1035, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("out_zero", imgs_)






        # result_out = out_check(cla)
        # if result_out == True:
        #     full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\out_zero.PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(230, 980, 280, 1035, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         print("out_zero", imgs_)
        #
        #
        # else:
        #     result_juljun = juljun_check(cla)
        #     if result_juljun == True:
        #         full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\juljun_zero.PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(250, 970, 305, 1035, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print("juljun_zero", imgs_)


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