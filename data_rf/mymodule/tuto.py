import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2

    from function_game import macro_out, imgs_set_, click_pos_2, drag_pos
    from game_check import out_check
    from clean_screen import clean_screen_start
    from action import confirm_all, juljun_check, juljun_off
    from dead_die import dead_check

    try:
        print("tuto_start")
        # 절전모드는 무조건 풀고

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            juljun_off(cla)

        quest_complete(cla)

        dead_check(cla)

        # 스토리모드부터 확인
        result_story = tuto_story(cla)
        if result_story == False:
            result_quest_on = quest_on_check(cla)
            if result_quest_on == False:

                result_out = out_check(cla)
                if result_out == False:
                    clean_screen_start(cla)
                    click_pos_2(895, 100, cla)
                else:
                    drag_pos(820, 100, 820, 160, cla)
                    time.sleep(1)
                    click_pos_2(895, 100, cla)

                for i in range(5):
                    result_confirm = confirm_all(cla)
                    if result_confirm == True:
                        break
                    QTest.qWait(500)


    except Exception as e:
        print(e)


def quest_complete(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg


    try:
        print("quest_complete")

        is_data = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\out_complete_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(820, 80, 920, 250, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("out_complete_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_data = True


        return is_data
    except Exception as e:
        print(e)
def quest_on_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_


    try:
        print("quest_on_check")

        is_data = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\quest_check\\quest_on_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("quest_on_1", imgs_)
            is_data = True
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\quest_check\\quest_on_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(890, 900, 950, 950, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("quest_on_2", imgs_)
                is_data = True


        return is_data
    except Exception as e:
        print(e)


def tuto_story(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_2
    from game_check import out_check
    from action import confirm_all

    try:
        print("tuto_story")
        is_data = False

        tuto_skip(cla)

        way_check(cla)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\story\\attack_click.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(540, 940, 700, 1020, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("attack_click", imgs_)
            click_pos_2(890, 985, cla)
            is_data = True
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(20, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("quest", imgs_)
                is_data = True

                for i in range(5):
                    result_confirm = confirm_all(cla)
                    if result_confirm == False:
                        result_out = out_check(cla)
                        if result_out == True:
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\story\\cancle_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(770, 940, 960, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("cancle_1", imgs_)
                                click_pos_2(935, 60, cla)
                            else:
                                click_pos_2(890, 1020, cla)



                    QTest.qWait(1000)


        return is_data
    except Exception as e:
        print(e)



def way_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos, drag_pos_reg

    try:
        print("way_check")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\way\\left_drag_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("left_drag_1", imgs_)
                drag_pos(930, 590, 800, 590, cla)

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\way\\right_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("right_1", imgs_)
                click_pos_reg(imgs_.x + 35, imgs_.y, cla)
                is_data_count = 0
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\way\\down_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("down_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y + 40, cla)
                    time.sleep(0.1)
                    click_pos_reg(imgs_.x, imgs_.y + 40, cla)
                    is_data_count = 0
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\way\\up_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("up_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y - 40, cla)
                        time.sleep(0.5)
                        is_data_count = 0

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\tuto\\way\\up_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("up_2", imgs_)
                        drag_pos_reg(imgs_.x, imgs_.y + 30, imgs_.x, imgs_.y - 30, cla)
                        is_data_count = 0

            if is_data_count > 3:
                is_data = True

            QTest.qWait(500)


        return is_data

    except Exception as e:
        print(e)


def tuto_skip(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos
    from action import confirm_all

    try:
        print("tuto_skip")

        is_data = False
        is_data_count = 0
        while is_data is False:
            is_data_count += 1

            confirm_all(cla)

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\skip\\skip_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 30, 960, 200, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("skip_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_data_count = 0
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\skip\\skip_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 30, 960, 200, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("skip_2", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_data_count = 0
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\skip\\quest_complete_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(370, 450, 600, 600, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_complete_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        is_data_count = 0


            if is_data_count > 3:
                is_data = True

            QTest.qWait(500)


        return is_data

    except Exception as e:
        print(e)

