import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def confirm_all(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import click_pos_reg, imgs_set_

    try:
        print("confirm_all")

        is_confirm = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 500, 700, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            is_confirm = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\move_confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 500, 700, 800, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("move_confirm_1", imgs_)
                is_confirm = True
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\soolock_confirm_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 500, 700, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("soolock_confirm_1", imgs_)
                    is_confirm = True
                    click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_confirm
    except Exception as e:
        print(e)


def menu_open(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, imgs_set_
    from game_check import out_check
    from clean_screen import clean_screen_start

    try:
        print("menu_open")

        is_data = False
        is_data_count = 0

        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("menu_setting", imgs_)
                is_data = True
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(930, 55, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def menu_open_pure(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, imgs_set_
    from game_check import out_check
    from clean_screen import clean_screen_start

    try:
        print("menu_open_pure")

        is_data = False
        is_data_count = 0

        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("menu_setting", imgs_)
                is_data = True
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(930, 55, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def juljun_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import click_pos_reg, imgs_set_

    try:
        print("juljun_check")

        is_data = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\juljun_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(350, 80, 580, 130, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("juljun_on", imgs_)
            is_data = True

        return is_data
    except Exception as e:
        print(e)


def juljun_off(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import drag_pos, imgs_set_

    try:
        print("juljun_off")

        for i in range(10):

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 80, 580, 130, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on", imgs_)
                drag_pos(480, 520, 860, 520, cla)
            else:
                break
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def juljun_off_setting(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_reg, imgs_set_, click_pos_2
    from clean_screen import clean_screen_start

    try:
        print("juljun_off_setting")

        is_data = False
        is_data_count = 0

        while is_data is False:
            is_data_count += 1
            if is_data_count > 10:
                is_data = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("setting", imgs_)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\set_juljun_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(90, 350, 200, 430, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("set_juljun_title", imgs_)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\not_juljun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(500, 400, 800, 500, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("not_juljun", imgs_)
                        clean_screen_start(cla)
                        is_data = True
                    else:
                        click_pos_2(600, 440, cla)

                else:
                    click_pos_2(170, 95, cla)


            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\setting.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 200, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("setting", imgs_)
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_setting", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        menu_open(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)



def juljun_on(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import drag_pos, imgs_set_, click_pos_2
    from game_check import out_check
    from clean_screen import clean_screen_start
    try:
        print("juljun_on")

        for i in range(10):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\juljun_on.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(350, 80, 580, 130, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on", imgs_)
                break
            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(25, 840, cla)
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)






