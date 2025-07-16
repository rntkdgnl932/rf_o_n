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
    from get_item import get_post, get_upjuk, get_event, get_item_start, get_sangjum_sohwan, allget_btn_click, get_sangjum_sohwan_start, jaelyo_jejak, get_memorychip, guild_start
    from game_check import out_check, move_check, attack_check
    from boonhae_collection import collection_start, boonhae_go, boonhae_collection_start, collection_go, boonhae_go_memorychip
    from massenger import line_to_me
    from potion import potion_buy, potion_check
    from jadong import jadong_in, jadong_mode
    from clean_screen import clean_screen_start
    from dead_die import dead_check
    from auction_game import auction_low_num, auction_qun_num, auction_start
    from mission import mission_get, mission_get_des
    from gyucjunji import gyucjunji_in
    from dungeon import dun_in
    from server import server_get_version
    plus_minus = 20
    try:
        print("test")

        # boonhae_go_memorychip(cla)
        data = "일일미션"

        guild_start(cla)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\guild\\guild_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("guild_point_1", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("close_2", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("close_3", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_4.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("close_4", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\all_get_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("all_get_point_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\all_get_point_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("all_get_point_2", imgs_)
            click_pos_reg(imgs_.x + 90, imgs_.y + 10, cla)
            time.sleep(0.5)
            click_pos_reg(imgs_.x + 90 + 40, imgs_.y + 10, cla)
            time.sleep(0.5)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_random\\no_have_random_item.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(580, 980, 630, 1030, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("no_have_random_item", imgs_)


        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("post_point_1", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\menu_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("menu_point_1", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("post_point_2", imgs_)

        dun_name = "pyegijang"

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(dun_name) + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 515, 900, 555, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("pyegijang", imgs_)

        dun_name = "secret_base"

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(dun_name) + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 515, 900, 555, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("secret_base", imgs_)

        dun_name = "chaegool"

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(dun_name) + ".PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 515, 900, 555, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("chaegool", imgs_)

        # mission_get_des(cla, "month", data)
        # mission_get_des(cla, "week", data)
        # mission_get_des(cla, "daily", data)
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_allget_btn\\allget_btn_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(130, 340, 830, 730, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("allget_btn_1", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_allget_btn\\allget_btn_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(130, 340, 830, 730, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("allget_btn_2", imgs_)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_allget_btn\\allget_btn_3.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(130, 340, 830, 730, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("allget_btn_3", imgs_)

        # boonhae_collection_start(cla)
        #
        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\chapter_lock.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(50, 135, 110, 600, cla, img, 0.7)
        # if imgs_ is not None and imgs_ != False:
        #     print("chapter_lock", imgs_)
        #
        #     for i in range(6):
        #         lock_reg = 165 + 25 + (50 * i)
        #
        #         print("lock_reg", lock_reg)
        #
        #         if imgs_.y < lock_reg:
        #             is_lock = str(i)
        #             break
        #
        # else:
        #     is_lock = "6"
        #
        # print("is_lock", is_lock)
        #
        # for i in range(3):
        #     step = i +1
        #     full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\pyegijang\\num\\" + str(step) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(250, 430, 325, 680, cla, img, 0.9)
        #     if imgs_ is not None and imgs_ != False:
        #         print("step", str(step), imgs_)
        #
        # full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\pyegijang\\num\\" + str(step) + ".PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(280, 430, 325, 680, cla, img, 0.9)
        # if imgs_ is not None and imgs_ != False:
        #     print("step", str(step), imgs_)

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

        # gyucjunji_in(cla, "data")

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\jangsigan_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 500, 500, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan_1", imgs_)

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

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\full_honjab.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(280, 680, 530, 710, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("full_honjab", imgs_)
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\full_wonhwal.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(280, 680, 530, 710, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("full_wonhwal", imgs_)

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