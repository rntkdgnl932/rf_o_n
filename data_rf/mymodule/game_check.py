import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def game_check_start(cla):
    import numpy as np
    import cv2

    from function_game import macro_out, imgs_set_, click_pos_2
    from massenger import line_to_me

    try:
        print("game_check")
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\fix_notice_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 500, 440, 540, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("fix_notice_1", imgs_)
            why = "점검 중...."
            line_to_me(cla, why)
            macro_out(cla)
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\jangsigan_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 500, 500, 600, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("jangsigan_1", imgs_)

                click_pos_2(480, 620, cla)

                # why = "장시간...."
                # line_to_me(cla, why)
                # macro_out(cla)
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\new_path_notice.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 500, 500, 600, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("new_path_notice", imgs_)
                    why = "새로운 패치...."
                    line_to_me(cla, why)
                    macro_out(cla)
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\fix_server_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 500, 500, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("fix_server_2", imgs_)
                        why = "서버점검"
                        line_to_me(cla, why)
                        macro_out(cla)

    except Exception as e:
        print(e)


def loading_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_


    try:
        print("loading_check")

        is_loading = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\loading\\loading_tip.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 960, 120, 1040, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("loading_tip", imgs_)
            is_loading = True

        loding_count = 0
        while is_loading is True:

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\loading\\loading_tip.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 960, 120, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("loading_tip", imgs_)
                loding_count = 0
            else:
                loding_count += 1
                if loding_count > 7:
                    is_loading = False
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        loding_count += 1
            QTest.qWait(500)

    except Exception as e:
        print(e)


def move_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_


    try:
        print("move_check")

        is_move = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\move\\m.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(485, 880, 520, 910, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("m", imgs_)
            is_move = True

        is_move_count = 0
        count = 0
        while is_move is True:
            count += 2
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\move\\m.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(485, 880, 520, 910, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("m :", count, "초", imgs_)
                is_move_count = 0
            else:
                is_move_count += 1
                if is_move_count > 5:
                    is_move = False
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        is_move_count += 1
            QTest.qWait(2000)

    except Exception as e:
        print(e)


def move_check_pure(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_


    try:
        print("move_check_pure")

        is_move = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\move\\m.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(485, 880, 520, 910, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("m", imgs_)
            is_move = True

        return is_move

    except Exception as e:
        print(e)

def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from dead_die import dead_check
    from massenger import line_to_me
    from schedule import myQuest_play_check
    from character_select_and_game_start import game_start_screen

    try:
        print("out_check")

        is_data = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\jangsigan_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 500, 500, 600, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("jangsigan_1", imgs_)

            click_pos_2(480, 620, cla)

            # why = "장시간인데 로그인 되는지 확인하라"
            # line_to_me(cla, why)

        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("menu_setting", imgs_)

            else:
                for i in range(3):

                    is_list = i + 1

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\out_check\\talk" + str(is_list) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 850, 60, 920, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("talk", str(is_list), imgs_)
                        is_data = True
                        break
                    
        if is_data == True:
            is_data = close_check(cla)

            if is_data == True:
                dead_check(cla)
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\character_start\\next.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(550, 450, 930, 600, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("hi")
                result_schedule = myQuest_play_check(v_.now_cla, "check")
                character_id = result_schedule[0][1]

                game_start_screen(v_.now_cla, character_id)

        return is_data

    except Exception as e:
        print(e)


def close_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_

    try:
        print("close_check")

        clean = True

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("menu_setting", imgs_)
            clean = False
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                clean = False
                print("close_1", imgs_)
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                clean = False
                print("close_2", imgs_)

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                clean = False
                print("close_3", imgs_)

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_4.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                clean = False
                print("close_4", imgs_)

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\out_btn_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(900, 30, 960, 200, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                clean = False
                print("out_btn_1", imgs_)

        return clean

    except Exception as e:
        print(e)

def attack_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    from function_game import imgs_set_, text_check_get_black_white
    from action import juljun_check

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

    try:
        print("attack_check")

        is_data = False

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            result_exp_1 = text_check_get_black_white(33, 125, 135, 155, cla)

            # a = 33
            # b = 125
            # c = 135
            # d = 155
            #
            # pos = (a + plus, b, c - a, d - b)
            # pyautogui.screenshot("asd.png", region=pos)


            for i in range(20):
                result_exp_2 = text_check_get_black_white(33, 125, 135, 155, cla)

                if result_exp_1 != result_exp_2:
                    is_data = True
                    break

                QTest.qWait(1000)

        else:
            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\attack\\auto_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("auto_on", imgs_)
                    is_data = True

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\attack\\auto_off.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("auto_off", imgs_)
                    is_data = False




        return is_data

    except Exception as e:
        print(e)

