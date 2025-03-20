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

    from function_game import macro_out, imgs_set_
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


def out_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_

    try:
        print("out_check")

        is_data = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\out_check\\talk.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 500, 440, 540, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("talk", imgs_)
            is_data = True

        return is_data

    except Exception as e:
        print(e)



def attack_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_

    try:
        print("attack_check")

        is_data = False

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

