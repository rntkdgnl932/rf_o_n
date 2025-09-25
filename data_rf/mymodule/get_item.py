import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import macro_out
    from massenger import line_to_me
    from boonhae_collection import boonhae_go_memorychip

    try:
        print("get_item_start")
        get_event(cla)
        get_promotion(cla)

        get_sangjum_sohwan(cla)

        get_post(cla)
        get_upjuk(cla)

        get_memorychip(cla)

        # 메모리칩 분해하기
        boonhae_go_memorychip(cla)

        # 길드 추가하기기
        guild_start(cla)

        # 재료제작하기
        jaelyo_jejak(cla)


    except Exception as e:
        print(e)



def get_sangjum_sohwan(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos
    from action import menu_open_pure

    try:



        print("get_sangjum_sohwan")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\cash_sangjum.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : cash_sangjum")
                for i in range(7):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\rober_one.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(510, 100, 960, 160, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\credit_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 140, 70, 200, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("credit_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            click_pos_2(280, 95, cla)
                    QTest.qWait(500)

                # 받기
                get_sangjum_sohwan_start(cla)
                # 오른쪽 드래그
                for i in range(7):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\right_drag_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 100, 930, 160, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        drag_pos(830, 200, 160, 200, cla)
                        time.sleep(1)
                    QTest.qWait(500)
                # 다시 받기
                get_sangjum_sohwan_start(cla)

                # 나가기
                print("끝")
                is_get = True

                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\cash_sangjum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 60, cla)
                    else:
                        break
                    time.sleep(0.5)
            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\cash_sangjum.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\sangjum.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_sangjum")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


    except Exception as e:
        print(e)


def get_sangjum_sohwan_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_reg
    from action import menu_open_pure
    from tuto import tuto_skip

    try:



        print("get_sangjum_sohwan_start")
        is_get = False
        is_get_count = 0
        is_get_count_2 = 1
        while is_get is False:
            is_get_count += 1
            print("is_get_count", is_get_count)
            if is_get_count > 60:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_3.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(670, 320, 730, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("close_3", imgs_)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\max.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(570, 560, 650, 610, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("max", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\buy_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 670, 570, 720, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("buy_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    time.sleep(1)

                    for i in range(15):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\cash_sangjum.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\skip\\skip_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(700, 30, 960, 200, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("skip_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\all_confirm_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 980, 550, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("all_confirm_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(2)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\confirm.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 980, 620, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("confirm", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)
                        time.sleep(1)

            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\cash_sangjum.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:

                    # 여기에서 좌표값 설정
                    # 130, 140, 300, 180
                    # 330, 140, 500, 180
                    # 530, 140, 700, 180
                    # 730, 140, 900, 180
                    # 130, 315, 300, 355
                    # 330, 315, 500, 355
                    # 530, 315, 700, 355
                    # 730, 315, 900, 355

                    if is_get_count_2 < 5:

                        this_x_1 = (200 * is_get_count_2) - 70
                        this_y_1 = 140

                    else:
                        is_get_count_3 = is_get_count_2 - 4

                        this_x_1 = (200 * is_get_count_3) - 70
                        this_y_1 = 315

                    this_x_2 = this_x_1 + 170
                    this_y_2 = this_y_1 + 40

                    print("point =>", this_x_1, this_y_1, this_x_2, this_y_2)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\not_sold_out.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(this_x_1, this_y_1, this_x_2, this_y_2, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("not_sold_out", imgs_)

                        x_reg = imgs_.x
                        y_reg = imgs_.y

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\can_not_buy_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_reg(x_reg - 30, y_reg, x_reg + 100, y_reg + 100, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("can_not_buy_1", imgs_)
                            is_get_count_2 += 1
                            if is_get_count_2 > 8:
                                is_get = True
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\sangjum_sohwan\\can_not_buy_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_reg(x_reg - 30, y_reg, x_reg + 100, y_reg + 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("can_not_buy_2", imgs_)
                                is_get_count_2 += 1
                                if is_get_count_2 > 8:
                                    is_get = True
                            else:
                                click_pos_reg(x_reg, y_reg + 110, cla)
                                is_get_count_2 = 0





                    else:
                        is_get_count_2 += 1
                        if is_get_count_2 > 8:
                            is_get = True
                else:
                    tuto_skip(cla)
            print("is_get_count_2", is_get_count_2)

            QTest.qWait(500)


    except Exception as e:
        print(e)

def get_post(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import menu_open_pure

    try:



        print("get_post")
        this_point_x = 770
        this_point_y = 1000
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : post")
                for i in range(5):

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post\\get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 110, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("get_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post\\confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 590, 630, 660, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)



                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 60, 450, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("post_point_1", imgs_)
                        click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                    else:
                        break
                    QTest.qWait(500)

                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post\\get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 110, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("get_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post\\confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(470, 590, 630, 660, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(1)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(60, 60, 450, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("post_point_1", imgs_)
                        click_pos_reg(imgs_.x - 50, imgs_.y + 10, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                    else:
                        for c in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\post.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(30, 60, cla)
                            else:
                                is_get = True
                                break
                            time.sleep(1)
                    QTest.qWait(500)

                for c in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(460, 340, cla)
                    QTest.qWait(500)


            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


    except Exception as e:
        print(e)




def get_upjuk(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import menu_open_pure

    try:



        print("get_upjuk")
        this_point_x = 942
        this_point_y = 150
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\upjuk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : upjuk")
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 60, 145, 350, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("post_point_1", imgs_)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                    else:
                        break
                    QTest.qWait(500)

                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(90, 60, 145, 350, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("post_point_1", imgs_)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                        click_pos_2(870, 1020, cla)
                        time.sleep(0.2)
                    else:
                        for c in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\upjuk.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(30, 60, cla)
                            else:
                                is_get = True
                                break
                            time.sleep(1)
                    QTest.qWait(500)





            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\upjuk.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


    except Exception as e:
        print(e)




def get_memorychip(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import menu_open_pure

    try:



        print("get_memorychip")
        this_point_x = 940
        this_point_y = 255
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\memorychip.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : memorychip")


                is_point = False

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(60, 60, 100, 350, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("post_point_1", imgs_)

                    is_point = True

                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                    time.sleep(0.2)

                if is_point == False:
                    is_get = True
                else:
                    # 진입
                    for i in range(5):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\momorychip_hyogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(865, 1000, 960, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("des momorychip_hyogwa", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\post_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(90, 85, 700, 1030, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("des post_point_1", imgs_)
                                click_pos_reg(imgs_.x - 35, imgs_.y + 35, cla)
                                time.sleep(0.2)
                            else:
                                click_pos_2(160, 160, cla)
                        QTest.qWait(500)
                    # 등록하기
                    for i in range(10):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\momorychip_hyogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(865, 1000, 960, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("des momorychip_hyogwa", imgs_)

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\memorychip_clicked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(160, 680, 800, 800, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("des memorychip_clicked", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y - 25, cla)
                                time.sleep(0.2)
                                click_pos_reg(imgs_.x, imgs_.y - 25, cla)
                                time.sleep(2)

                            else:

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\memorychip_clicked2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(160, 680, 800, 800, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("des memorychip_clicked2", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y - 25, cla)
                                    time.sleep(0.2)
                                    click_pos_reg(imgs_.x, imgs_.y - 25, cla)
                                    time.sleep(2)

                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\memorychip_registration_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(160, 680, 800, 800, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("des memorychip_registration_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        time.sleep(2)
                                    else:
                                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\memorychip_registration_btn2.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(160, 680, 800, 800, cla, img, 0.9)
                                        if imgs_ is not None and imgs_ != False:
                                            print("des memorychip_registration_btn2", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                            time.sleep(2)
                                        else:
                                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\momorychip_complete.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 400, 600, 600, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("des momorychip_complete", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(500)
                    # 나가기
                    for i in range(10):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\momorychip_hyogwa.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(865, 1000, 960, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("des momorychip_hyogwa", imgs_)
                            click_pos_2(25, 60, cla)


                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\memorychip.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                break

                        QTest.qWait(500)




            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\memorychip.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1")
                                click_pos_reg(imgs_.x - 20, imgs_.y + 10, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


    except Exception as e:
        print(e)

def jaelyo_jejak(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import menu_open_pure

    try:



        print("jaelyo_jejak")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\jejak.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : jejak")

                is_get = True

                # 재료 클릭하기
                for i in range(3):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\jaelyo_jejak\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 90, 540, 120, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked", imgs_)
                        break
                    else:
                        click_pos_2(495, 95, cla)
                    QTest.qWait(500)

                # 재료 제작하기 (추후 업뎃하기)
                for i in range(5):

                    list = i + 1

                    for t in range(15):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\jaelyo_jejak\\jaelyo_lack_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 70, 570, 120, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jaelyo_lack_notice", imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\jaelyo_jejak\\jejak_result_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(470, 440, 540, 490, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("jejak_result_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\jaelyo_jejak\\right\\" + str(
                                    list) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(680, 140, 840, 180, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(925, 985, cla)
                                    time.sleep(0.5)
                                    click_pos_2(820, 1020, cla)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\jaelyo_jejak\\left\\" + str(
                                        list) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(90, 110, 260, 1020, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("left : str(list)", str(list), imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)


                        QTest.qWait(500)
                    QTest.qWait(500)

                    for t in range(10):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\jaelyo_jejak\\jaelyo_lack_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 70, 570, 120, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jaelyo_lack_notice...wait", imgs_)
                        else:
                            break
                        QTest.qWait(1000)

                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\jejak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("title : jejak...out")
                        click_pos_2(25, 60, cla)
                    else:
                        break
                    time.sleep(1)







            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\jejak.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\jejak.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


    except Exception as e:
        print(e)

def get_event(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos
    from action import menu_open_pure

    # 폴더 내 파일 개수
    folder_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title"
    file_list = os.listdir(folder_path)
    file_count = len(file_list)

    try:



        print("get_event")
        this_point_x = 767
        this_point_y = 45
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 10:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : close_2")
                is_event_point = False
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    is_event_point = True
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_event_point = True

                if is_event_point == True:

                    # 반복문

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("event_point_1", imgs_)


                        y_point = imgs_.y

                        click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                        time.sleep(0.5)

                        # 그림 파악하기

                        for n in range(len(file_list)):

                            pic_num_ready = file_list[n]
                            pic_num = pic_num_ready.split(".")[0]

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(pic_num) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("pic_num", pic_num)
                                is_picture = str(pic_num)
                                get_event_click(cla, is_picture, y_point)
                                break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("event_point_2", imgs_)

                            y_point = imgs_.y

                            click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x - 50, imgs_.y, cla)
                            time.sleep(0.5)

                            # 그림 파악하기

                            for n in range(len(file_list)):

                                pic_num_ready = file_list[n]
                                pic_num = pic_num_ready.split(".")[0]

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(
                                    pic_num) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("pic_num", pic_num)
                                    is_picture = str(pic_num)
                                    get_event_click(cla, is_picture, y_point)
                                    break

                else:

                    is_point = False
                    for i in range(3):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            is_point = True
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                is_point = True
                                break
                            else:
                                drag_pos(770, 700, 770, 400, cla)
                        QTest.qWait(500)
                    if is_point == False:
                        is_get = True

            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1")
                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                            else:
                                break
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


        # 마지막 나가기
        for i in range(5):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)


def get_event_open(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos
    from action import menu_open_pure

    # 폴더 내 파일 개수
    folder_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title"
    file_list = os.listdir(folder_path)
    file_count = len(file_list)

    try:



        print("get_event_open")
        this_point_x = 767
        this_point_y = 45
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 10:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : close_2")

                is_get = True

            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1")
                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                            else:
                                break
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


        # 마지막 나가기
        for i in range(5):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)

def get_promotion(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg
    from action import menu_open_pure

    # 폴더 내 파일 개수
    folder_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title"
    file_list = os.listdir(folder_path)
    file_count = len(file_list)

    try:



        print("get_promotion")
        this_point_x = 810
        this_point_y = 45
        plus_minus = 20

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 10:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : close_2")

                is_event_point = False

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    is_event_point = True
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_event_point = True

                if is_event_point == True:

                    # 반복문

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("event_point_1", imgs_)


                        y_point = imgs_.y

                        click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                        time.sleep(0.5)
                        click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                        time.sleep(0.5)

                        # 그림 파악하기

                        for n in range(len(file_list)):

                            pic_num_ready = file_list[n]
                            pic_num = pic_num_ready.split(".")[0]

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(pic_num) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("pic_num", pic_num)
                                is_picture = str(pic_num)
                                get_event_click(cla, is_picture, y_point)
                                break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 370, 830, 730, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("event_point_2", imgs_)

                            y_point = imgs_.y

                            click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x - 50, imgs_.y + 20, cla)
                            time.sleep(0.5)

                            # 그림 파악하기

                            for n in range(len(file_list)):

                                pic_num_ready = file_list[n]
                                pic_num = pic_num_ready.split(".")[0]

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(
                                    pic_num) + ".PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("pic_num", pic_num)
                                    is_picture = str(pic_num)
                                    get_event_click(cla, is_picture, y_point)
                                    break
                else:
                    is_get = True

            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(this_point_x - plus_minus, this_point_y - plus_minus,
                                              this_point_x + plus_minus, this_point_y + plus_minus, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_point_1")
                                click_pos_reg(imgs_.x - 10, imgs_.y + 10, cla)
                            else:
                                break
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


        # 마지막 나가기
        for i in range(5):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(780, 330, 840, 390, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)

    except Exception as e:
        print(e)

def event_get_reg(cla, y_point):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos, click_pos_2

    try:
        print("event_get_reg", y_point)
        # data => e_in_point_1, allget_point_3

        is_point = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(790, y_point - 20, 830, y_point + 20, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("e_in_point_1", imgs_)
            is_point = True
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_point_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, y_point - 20, 830, y_point + 20, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("event_point_2", imgs_)
                is_point = True

        return is_point
    except Exception as e:
        print(e)
        return 0



def allget_btn_click(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, drag_pos, click_pos_2

    # 폴더 내 파일 개수
    folder_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_allget_btn"
    file_list = os.listdir(folder_path)
    file_count = len(file_list)

    try:
        print("allget_btn_click")
        # data => e_in_point_1, allget_point_3

        for n in range(len(file_list)):

            pic_num_ready = file_list[n]
            pic_num = pic_num_ready.split(".")[0]

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_allget_btn\\" + str(pic_num) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(130, 340, 830, 730, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("event_allget_btn", pic_num)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)
        click_pos_2(640, 420, cla)
    except Exception as e:
        print(e)
        return 0

def get_event_click(cla, is_picture, y_point):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, imgs_set_for
    from tuto import tuto_skip
    from clean_screen import clean_screen_start

    try:

        print("event_get_click", is_picture, y_point)


        ######

        # - : 3 ~ 12

        # 1 : 데일리출석이벤트시즌2(twenty_one) o

        # 2 : 멈추지않는여정,용벙의길(all_get) o

        # 3 : 전설적인보물열쇠패스(all_get) 3

        # 4 : 전설적인유적지조사(twenty_five) 4

        # 5 : 전설적인보물열쇠지원미션(all_get) 5

        # 6 : 0.5년축제스페출출석이벤트(fourteen) 6

        # 7 : 0.5년축제7일미션이벤트(all_get) 7

        # 8 : 0.5년축제스페셜미션이벤트(all_get) 8

        # 9 : 0.5주년축제카운트다운!출석이벤트(seven) o

        # 10 :

        # 11 :

        # 12 :


        # ?? : 전설적인보물열쇠패스(all_get) 3
        # ?? : 전설적인유적지조사(twenty_five) 4
        # ?? : 전설적인보물열쇠지원미션(all_get) 5
        # ?? : 0.5년축제스페출출석이벤트(fourteen) 6
        # ?? : 0.5년축제7일미션이벤트(all_get) 7
        # ?? : 0.5년축제스페셜미션이벤트(all_get) 8
        # ?? :

        if is_picture == "6" or is_picture == "0":
            data = "fourteen"
        elif is_picture == "9":
            data = "seven"
        elif is_picture == "1":
            data = "twenty_one"
        elif is_picture == "0":
            data = "length_five"
        elif is_picture == "4" or is_picture == "0":
            data = "twenty_five"
        elif is_picture == "2" or is_picture == "3" or is_picture == "5" or is_picture == "7" or is_picture == "8":
            data = "all_get"
        elif is_picture == "0" or is_picture == "0":
            data = "all_get_2"
        elif is_picture == "0":
            data = "gyohwan"
        elif is_picture == "0" or is_picture == "0" or is_picture == "0":
            data = "pass"


        if data == "fourteen":
            print("fourteen")





            for c in range(5):
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(is_picture) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_click : pic_num", is_picture)

                    result_point = event_get_reg(cla, y_point)
                    if result_point == True:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(130, 340, 700, 730, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            print("checked", imgs_)


                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(590, 470, 690, 570, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(130, 550, 700, 730, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_for = imgs_set_for(130, 550, 830, 730, cla, img, 0.7)
                                    if imgs_for is not None and imgs_for != False:
                                        if len(imgs_for) > 0:
                                            click_x = imgs_for[len(imgs_for) - 1][0]
                                            click_y = imgs_for[len(imgs_for) - 1][1]
                                            click_pos_reg(click_x + 80, click_y, cla)


                                else:
                                    click_pos_2(200, 595, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_for = imgs_set_for(130, 340, 830, 730, cla, img, 0.7)
                                if imgs_for is not None and imgs_for != False:
                                    print("checked_for", imgs_for)

                                    if len(imgs_for) > 0:
                                        click_x = imgs_for[len(imgs_for) - 1][0]
                                        click_y = imgs_for[len(imgs_for) - 1][1]
                                        click_pos_reg(click_x + 80, click_y, cla)
                        else:
                            click_pos_2(200, 510, cla)
                    else:
                        break
                else:
                    click_pos_2(755, y_point, cla)
                QTest.qWait(200)

        elif data == "seven":
            print("seven")





            for c in range(5):
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(is_picture) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_click : pic_num", is_picture)

                    result_point = event_get_reg(cla, y_point)
                    if result_point == True:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_for = imgs_set_for(130, 340, 700, 730, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            if len(imgs_for) > 0:
                                click_x = imgs_for[len(imgs_for) - 1][0]
                                click_y = imgs_for[len(imgs_for) - 1][1]
                                click_pos_reg(click_x + 80, click_y, cla)
                            else:
                                click_pos_2(200, 550, cla)
                    else:
                        break
                else:
                    click_pos_2(755, y_point, cla)
                QTest.qWait(200)

        elif data == "twenty_one":
            print("twenty_one")





            for c in range(5):

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(is_picture) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_click : pic_num", is_picture)

                    result_point = event_get_reg(cla, y_point)
                    if result_point == True:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(130, 340, 700, 730, cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:

                            print("checked", imgs_)

                            # 먼저 두번째줄 끝에 체크되어있는지

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(590, 515, 690, 610, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(130, 600, 700, 700, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_for = imgs_set_for(130, 600, 830, 700, cla, img, 0.7)
                                    if imgs_for is not None and imgs_for != False:
                                        if len(imgs_for) > 0:
                                            click_x = imgs_for[len(imgs_for) - 1][0]
                                            click_y = imgs_for[len(imgs_for) - 1][1]
                                            click_pos_reg(click_x + 80, click_y, cla)


                                else:
                                    click_pos_2(200, 645, cla)
                            else:

                                # 두번째줄 끝에 체크되어 있지 않다면, 첫번째줄 끝에 체크 되어 있는지지

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(590, 425, 690, 520, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(130, 515, 700, 610, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_for = imgs_set_for(130, 515, 830, 610, cla, img, 0.8)
                                        if imgs_for is not None and imgs_for != False:
                                            if len(imgs_for) > 0:
                                                click_x = imgs_for[len(imgs_for) - 1][0]
                                                click_y = imgs_for[len(imgs_for) - 1][1]
                                                click_pos_reg(click_x + 80, click_y, cla)


                                    else:
                                        click_pos_2(200, 555, cla)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\fourteen\\checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_for = imgs_set_for(130, 340, 830, 730, cla, img, 0.7)
                                    if imgs_for is not None and imgs_for != False:
                                        print("checked_for", imgs_for)

                                        if len(imgs_for) > 0:
                                            click_x = imgs_for[len(imgs_for) - 1][0]
                                            click_y = imgs_for[len(imgs_for) - 1][1]
                                            click_pos_reg(click_x + 80, click_y, cla)



                        else:
                            click_pos_2(200, 465, cla)
                    else:
                        break
                else:
                    click_pos_2(755, y_point, cla)
                QTest.qWait(200)
        elif data == "twenty_five":

            print("twenty_five")

            for i in range(10):
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\twenty_five\\anymore_ticket_notice.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(150, 60, 660, 110, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("anymore_ticket_notice", imgs_)
                    break
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\twenty_five\\bbobgi_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(150, 420, 420, 690, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("bbobgi_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                    else:
                        click_pos_2(290, 560, cla)
                time.sleep(0.5)


        elif data == "length_five":

            print("length_five")

            for c in range(5):
                y_reg = 420 + (65 * c)
                click_pos_2(460, y_reg, cla)
                time.sleep(0.5)
                click_pos_2(460, y_reg, cla)
                time.sleep(0.5)



        elif data == "all_get":

            print("length_five")

            for c in range(5):

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(is_picture) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_click : pic_num", is_picture)

                    result_point = event_get_reg(cla, y_point)
                    if result_point == True:

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 450, 680, 500, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        allget_btn_click(cla)
                    else:
                        break
                else:
                    click_pos_2(755, y_point, cla)
                QTest.qWait(200)

        elif data == "all_get_2":

            print("all_get_2")




            for c in range(5):

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(is_picture) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_click : pic_num", is_picture)

                    result_point = event_get_reg(cla, y_point)
                    if result_point == True:

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 450, 680, 500, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\roulette\\contact_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(130, 340, 830, 730, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("contact_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        allget_btn_click(cla)

                        time.sleep(0.5)

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\all_get_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("all_get_point_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\all_get_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(150, 450, 680, 720, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("all_get_point_2", imgs_)
                            click_pos_reg(imgs_.x + 90, imgs_.y + 10, cla)
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x + 90 + 40, imgs_.y + 10, cla)
                            time.sleep(0.5)


                    else:
                        break
                else:
                    click_pos_2(755, y_point, cla)
                QTest.qWait(200)

        elif data == "gyohwan":

            print("gyohwan")



            y_count = 0
            for c in range(7):

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event_title\\" + str(is_picture) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(120, 340, 830, 730, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("get_event_click : pic_num", is_picture)

                    result_point = event_get_reg(cla, y_point)
                    if result_point == True:

                        for xx in range(10):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\gyohwan\\gyohwan_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 600, 600, 730, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("gyohwan_btn", imgs_)
                                x_reg = imgs_.x
                                y_reg = imgs_.y

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\event\\gyohwan\\max.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(500, 500, 650, 600, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("max", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(1)
                                click_pos_reg(x_reg, y_reg, cla)
                                time.sleep(0.5)
                            else:
                                # 420, 490, 560, 630...70차이
                                y_count += 1
                                y_reg_2 = 350 + (70 * y_count)
                                click_pos_2(580, y_reg_2, cla)
                                time.sleep(0.5)
                            time.sleep(0.5)



                    else:
                        break
                else:
                    click_pos_2(755, y_point, cla)
                QTest.qWait(200)

        elif data == "pass":
            print("pass")
            clean_screen_start(cla)
            get_event_open(cla)

        tuto_skip(cla)
    except Exception as e:
        print(e)



def guild_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, click_pos_reg, drag_pos
    from action import menu_open_pure

    try:



        print("guild_start")

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\guild.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : guild")

                click_pos_2(150, 1015, cla)
                time.sleep(0.5)

                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        click_pos_2(150, 1015, cla)
                    time.sleep(0.5)


                for i in range(7):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\guild\\anymore_donation_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(280, 40, 700, 150, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\guild\\donation_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(280, 560, 380, 610, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\guild\\donation_ready_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(750, 990, 880, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                    QTest.qWait(500)

                for i in range(7):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\guild\\donation_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(280, 560, 380, 610, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("close_2", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    QTest.qWait(500)

                # 받기
                for i in range(7):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\get_item\\guild\\guild_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("guild_point_1", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)
                        click_pos_2(880, 1020, cla)
                        time.sleep(0.5)
                        click_pos_2(880, 1020, cla)
                    else:
                        break
                    QTest.qWait(500)

                # 나가기
                print("끝")
                is_get = True

                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(935, 60, cla)
                    else:
                        break
                    time.sleep(0.5)
            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\guild.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        is_in = True
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\menu\\guild.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_guild")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)


    except Exception as e:
        print(e)