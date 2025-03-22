import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from schedule import myQuest_play_add
    from function_game import imgs_set_
    from game_check import out_check
    from action import juljun_check

    try:
        print("potion_check")

        result_out = out_check(cla)
        if result_out == True:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\out_zero.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(230, 980, 280, 1035, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("out_zero", imgs_)


                potion_buy(cla)

        else:
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\juljun_zero.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(250, 970, 305, 1035, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("juljun_zero", imgs_)
                    potion_buy(cla)


    except Exception as e:
        print(e)


def potion_buy(cla):
    import numpy as np
    import cv2

    from function_game import drag_pos, click_pos_reg, click_pos_2, imgs_set_
    from action import go_maul
    from game_check import move_check

    try:
        print("potion_buy")

        is_data = True
        is_data_count = 0
        while is_data is True:
            is_data_count += 1
            if is_data_count > 7:
                is_data = False

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\ilgwal_buy_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 370, 540, 410, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(540, 680, cla)

                is_buy = False
                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\buy_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 70, 620, 120, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        is_buy = True
                        break
                    time.sleep(0.1)
                if is_buy == True:
                    is_data = False
                    time.sleep(0.5)


                    for i in range(10):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\ilgwal_buy.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 1000, 280, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(935, 60, cla)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\ilgwal_buy_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 370, 540, 410, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(385, 680, cla)
                            else:
                                break
                        time.sleep(0.5)

            else:

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\ilgwal_buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(150, 1000, 280, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\jabhwa_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        move_check(cla)
                    else:
                        go_maul(cla)
            QTest.qWait(1000)




    except Exception as e:
        print(e)
