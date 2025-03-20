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
        while clean is True:
            clean_count += 1
            if clean_count > 5:
                clean = True

            result_out = out_check(cla)

            if result_out == True:
                clean = True
            else:
                clean_screen_go(cla)

            QTest.qWait(1000)

    except Exception as e:
        print(e)


def clean_screen_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg
    from game_check import out_check

    try:
        print("clean_screen_go")

        clean = False
        clean_count = 0
        while clean is True:
            clean_count += 1
            if clean_count > 2:
                break

            clean = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                clean = False
                print("close_1", cla)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                QTest.qWait(500)
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\out_btn_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    clean = False
                    print("out_btn_1", cla)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)

            QTest.qWait(1000)



    except Exception as e:
        print(e)