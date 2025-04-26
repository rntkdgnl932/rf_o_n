import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import macro_out
    from game_check import out_check

    try:
        print("clean_screen_start")

        clean = False
        clean_count = 0
        while clean is False:
            clean_count += 1
            if clean_count > 5:
                clean = True
            print("clean_count", clean_count)
            result_out = out_check(cla)

            if result_out == True:
                clean = True
            else:
                dead = clean_screen_go(cla)
                if dead == True:
                    clean = True

            QTest.qWait(1000)

    except Exception as e:
        print(e)


def clean_screen_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from game_check import out_check
    from action import juljun_off
    from stop_event18 import _stop_please
    from dead_die import dead_check
    from tuto import tuto_skip, quest_complete

    try:
        print("clean_screen_go")

        tuto_skip(cla)

        result_dead = dead_check(cla)

        if result_dead == False:

            juljun_off(cla)

            _stop_please(cla)

            quest_complete(cla)

            clean = False
            clean_count = 0
            while clean is False:
                clean_count += 1
                if clean_count > 2:
                    break

                clean = True

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("menu_setting", imgs_)
                    clean = False
                    click_pos_2(930, 50, cla)
                    QTest.qWait(500)
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("close_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("close_2", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_3.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("close_3", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_4.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("close_4", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_5.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("close_5", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_6.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("close_6", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\out_btn_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(900, 30, 960, 200, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("out_btn_1", imgs_)
                        click_pos_2(940, 60, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\get_sotang.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 430, 570, 490, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        clean = False
                        print("get_sotang", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 60, 700, 540, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("dead_notice", imgs_)
                        clean = False
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_notice2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(330, 60, 700, 540, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("dead_notice", imgs_)
                            clean = False
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            QTest.qWait(500)


                QTest.qWait(1000)
        return result_dead
    except Exception as e:
        print(e)

