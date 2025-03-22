import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def boonhae_collection_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import macro_out
    from massenger import line_to_me

    try:
        print("boonhae_collection_start")

        collection_start(cla)


    except Exception as e:
        print(e)


def collection_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open_pure

    try:
        print("collection_start")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : collection")

                is_get = True

                # 콜렉....
                for i in range(20):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\collection_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 100, 140, 500, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\have_item.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(870, 200, 950, 700, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("have_item", imgs_)
                            click_pos_2(890, 1020, cla)
                            time.sleep(1)

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\rare_more_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 470, 430, 520, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("rare_more_notice", imgs_)
                                why = "레이이상 등록하려 한다."
                                line_to_me(cla, why)
                                macro_out(cla)
                            else:

                                click_pos_2(890, 1020, cla)
                                time.sleep(0.5)
                                click_pos_2(890, 1020, cla)
                                time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\collection_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(100, 100, 140, 500, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("collection_point_1", imgs_)
                                click_pos_2(70, 130, cla)
                                time.sleep(0.5)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(250, 150, cla)
                                QTest.qWait(500)

                    else:
                        break
                    QTest.qWait(500)

                # 장비만 업글해서 콜렉하기


            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\menu_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(730, 190, 780, 250, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_collection")
                                click_pos_reg(imgs_.x, imgs_.y - 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)

def collection_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open_pure

    try:
        print("collection_go")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : collection", imgs_)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\collection_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(100, 100, 140, 500, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("collection_point_1", imgs_)


                is_get = True




            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\collection.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\menu_open\\menu_setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\menu_collection.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(730, 190, 780, 250, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_collection")
                                click_pos_reg(imgs_.x, imgs_.y - 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)

    except Exception as e:
        print(e)