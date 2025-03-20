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
        imgs_ = imgs_set_(410, 500, 630, 630, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("confirm_1", imgs_)
            is_confirm = False
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
            is_confirm = False
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
            is_confirm = False
            click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_confirm
    except Exception as e:
        print(e)