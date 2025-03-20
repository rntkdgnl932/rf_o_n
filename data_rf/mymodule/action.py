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
        imgs_ = imgs_set_(410, 500, 700, 700, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            is_confirm = True
            click_pos_reg(imgs_.x, imgs_.y, cla)
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\move_confirm_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 500, 700, 700, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("move_confirm_1", imgs_)
                is_confirm = True
                click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_confirm
    except Exception as e:
        print(e)


def menu_open(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import click_pos_reg, imgs_set_

    try:
        print("menu_open")

        is_confirm = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 500, 550, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            is_confirm = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_confirm
    except Exception as e:
        print(e)


def menu_open_pure(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import click_pos_reg, imgs_set_

    try:
        print("menu_open")

        is_confirm = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\confirm_all\\confirm_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(410, 500, 550, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            is_confirm = True
            click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_confirm
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
        imgs_ = imgs_set_(400, 80, 580, 130, cla, img, 0.85)
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
            imgs_ = imgs_set_(400, 80, 580, 130, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("juljun_on", imgs_)
                drag_pos(480, 520, 860, 520, cla)
            else:
                break
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
            imgs_ = imgs_set_(400, 80, 580, 130, cla, img, 0.85)
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






