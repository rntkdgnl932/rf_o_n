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
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\all_confirm_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 980, 550, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("all_confirm_btn", imgs_)
                        is_confirm = True
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(420, 980, 620, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("confirm", imgs_)
                            is_confirm = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)

        return is_confirm
    except Exception as e:
        print(e)

def cancle_all(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import click_pos_reg, imgs_set_

    try:
        print("cancle_all")

        is_cancle = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\cancle_all\\cancel_btn_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 500, 700, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("cancel_btn_1", imgs_)
            is_cancle = True
            click_pos_reg(imgs_.x, imgs_.y, cla)


        return is_cancle
    except Exception as e:
        print(e)

def menu_open(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, imgs_set_
    from game_check import out_check
    from clean_screen import clean_screen_start
    from get_item import get_event, get_promotion, get_post

    try:
        print("menu_open")

        plus_minus = 20

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

                # event
                this_point_x = 767
                this_point_y = 45
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\menu_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                  this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("menu_open : get_event")
                    get_event(cla)
                else:
                    # promotion
                    this_point_x = 810
                    this_point_y = 45
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\menu_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                      this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_open : get_event")
                        get_promotion(cla)
                    else:
                        # post
                        this_point_x = 770
                        this_point_y = 1000
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                          this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_open : get_event")
                            get_post(cla)
                        else:
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



def bag_open(cla):
    import numpy as np
    import cv2

    from function_game import click_pos_2, imgs_set_
    from game_check import out_check
    from clean_screen import clean_screen_start
    from get_item import get_event, get_promotion, get_post

    try:
        print("bag_open")

        is_data = False
        is_data_count = 0

        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\bag_open\\is_bag.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("is_bag", imgs_)

                is_data = True

            else:
                result_out = out_check(cla)
                if result_out == True:
                    click_pos_2(885, 55, cla)
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




def go_maul(cla):
    import numpy as np
    import cv2

    from function_game import drag_pos, imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    try:
        print("go_maul")


        is_data = True
        is_data_count = 0
        while is_data is True:
            is_data_count += 1
            if is_data_count > 7:
                is_data = False

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\jabhwa_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                is_data = False
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\guild_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    drag_pos(120, 80, 120, 190, cla)
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_maul\\maul_move_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(630, 980, 675, 1030, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                        already_maul = False
                        for i in range(10):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_maul\\already_maul_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(330, 70, 600, 120, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                already_maul = True
                                break
                            time.sleep(0.1)
                        if already_maul == True:
                            click_pos_2(24, 52, cla)
                    else:
                        clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def go_random(cla):
    import numpy as np
    import cv2

    from function_game import drag_pos, imgs_set_, click_pos_reg, click_pos_2
    from clean_screen import clean_screen_start
    from game_check import out_check
    try:
        print("go_random")


        is_data = True
        is_data_count = 0
        while is_data is True:
            is_data_count += 1
            if is_data_count > 7:
                is_data = False

            result_out = out_check(cla)
            if result_out == True:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_random\\random_move_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(580, 980, 630, 1030, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(5)
                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            is_data = False
                            break
                        QTest.qWait(1000)

            else:
                clean_screen_start(cla)

            QTest.qWait(1000)

    except Exception as e:
        print(e)


def attack_on(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from clean_screen import clean_screen_start
    from game_check import out_check, attack_check


    try:
        print("attack_on")

        attack = False
        attack_count = 0
        while attack is False:
            attack_count += 1
            if attack_count > 7:
                attack = True

            result_juljun = juljun_check(cla)
            if result_juljun == True:
                result_attack = attack_check(cla)
                if result_attack == True:
                    attack = True
                else:
                    juljun_off(cla)
            else:
                result_out = out_check(cla)
                if result_out == True:

                    result_attack = attack_check(cla)
                    if result_attack == False:

                        # go_random(cla)
                        click_pos_2(920, 925, cla)
                        attack = True
                else:
                    clean_screen_start(cla)
            QTest.qWait(1000)


    except Exception as e:
        print(e)