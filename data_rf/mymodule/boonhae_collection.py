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
        boonhae_go(cla)


    except Exception as e:
        print(e)


def collection_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg, click_pos_2, macro_out
    from action import menu_open_pure, confirm_all, cancle_all
    from massenger import line_to_me

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

                is_cancle = False

                # 콜렉....
                for i in range(20):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\collection_point_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(100, 100, 140, 500, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:

                        y_point = imgs_.y

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

                                if y_point < 245:

                                    why = "레어이상 등록하려 한다."
                                    line_to_me(cla, why)
                                    # macro_out(cla)
                                    cancle_all(cla)
                                    is_cancle = True
                                    break
                                else:
                                    result_confirm = confirm_all(cla)
                                    if result_confirm == True:
                                        time.sleep(0.5)
                                        click_pos_2(60, 275, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\more_grade_jangbi_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 400, 800, 860, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:
                                    print("more_grade_jangbi_notice", imgs_)

                                    if y_point < 245:

                                        why = "나보다 높은 등급을 등록하려 한다."
                                        line_to_me(cla, why)
                                        # macro_out(cla)
                                        cancle_all(cla)
                                        is_cancle = True
                                        break
                                    else:
                                        result_confirm = confirm_all(cla)
                                        if result_confirm == True:
                                            time.sleep(0.5)
                                            click_pos_2(60, 275, cla)

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
                if is_cancle == False:
                    # 장비만 업글해서 콜렉하기
                    collection_go(cla)

                    # 마지막으로 한번 더 확인하기
                    # 콜렉....
                    for i in range(20):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\collection_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 100, 140, 500, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:

                            y_point = imgs_.y

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

                                    if y_point < 245:

                                        why = "레어이상 등록하려 한다."
                                        line_to_me(cla, why)
                                        # macro_out(cla)
                                        cancle_all(cla)
                                        break
                                    else:
                                        result_confirm = confirm_all(cla)
                                        if result_confirm == True:
                                            time.sleep(0.5)
                                            click_pos_2(60, 275, cla)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\more_grade_jangbi_notice.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 400, 800, 860, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        print("more_grade_jangbi_notice", imgs_)

                                        if y_point < 245:

                                            why = "나보다 높은 등급을 등록하려 한다."
                                            line_to_me(cla, why)
                                            # macro_out(cla)
                                            cancle_all(cla)
                                            break
                                        else:
                                            result_confirm = confirm_all(cla)
                                            if result_confirm == True:
                                                time.sleep(0.5)
                                                click_pos_2(60, 275, cla)

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
            if is_get_count > 10:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\collection.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : collection", imgs_)
                click_pos_2(70, 130, cla)
                time.sleep(0.5)
                click_pos_2(60, 240, cla)
                QTest.qWait(1000)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\plus_5.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 100, 700, 1020, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:

                    for i in range(20):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\jaelyo_lack_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 60, 610, 110, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jaelyo_lack_notice", imgs_)
                            is_get = True
                            click_pos_2(30, 60, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\anymore_item_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(360, 60, 610, 110, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("anymore_item_notice", imgs_)
                                break
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\ganghwa_aim_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(360, 60, 610, 110, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("ganghwa_aim_notice", imgs_)
                                    click_pos_2(30, 60, cla)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\ganghwa_aim_notice_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(360, 60, 610, 110, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("ganghwa_aim_notice_2", imgs_)
                                        click_pos_2(30, 60, cla)
                                        is_get = True
                                        break

                                    else:
                                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\jangbi_ganghwa.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.95)
                                        if imgs_ is not None and imgs_ != False:
                                            print("title : jangbi_ganghwa", imgs_)
                                            click_pos_2(420, 1020, cla)
                                        else:
                                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\ilgwal_registration.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(810, 990, 940, 1040, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("ilgwal_registration", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)


                                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\plus_5.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 100, 700, 1020, cla, img, 0.95)
                                            if imgs_ is not None and imgs_ != False:
                                                print("plus_5", imgs_)
                                                click_pos_reg(imgs_.x - 15, imgs_.y - 15, cla)

                                                time.sleep(0.5)

                                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\upgrade_btn.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(900, 280, 960, 330, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("upgrade_btn", imgs_)
                                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                                    QTest.qWait(1000)



                        QTest.qWait(500)

                else:
                    is_get = True


            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\jangbi_ganghwa.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(30, 60, cla)
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

def boonhae_go(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open_pure
    from game_check import out_check
    from clean_screen import clean_screen_start

    try:
        print("boonhae_go")

        is_data = False
        is_data_count = 0

        while is_data is False:
            is_data_count += 1
            if is_data_count > 7:
                is_data = True



            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(540, 60, 620, 110, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("boonhae_title", imgs_)



                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\boonhae_complete.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 480, 540, 540, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("boonhae_complete", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        break
                    else:

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\common_clicked.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 200, 610, 345, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("common_clicked", imgs_)

                            click_pos_2(645, 245, cla)
                            time.sleep(0.5)

                            click_pos_2(870, 1020, cla)
                            is_data = True
                            break
                        else:
                            print("안보야")
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\boonhae_collection\\rare_on_clicked.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 200, 610, 345, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                print("rare_on_clicked", imgs_)
                                click_pos_2(530, 270, cla)
                                time.sleep(0.5)

                            click_pos_2(530, 245, cla)
                            time.sleep(0.5)
                            click_pos_2(530, 310, cla)
                            time.sleep(0.5)
                    time.sleep(0.5)
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\bag_open\\is_bag.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(850, 950, 960, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("is_bag", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        click_pos_2(885, 55, cla)
                    else:
                        clean_screen_start(cla)
            QTest.qWait(1000)

    except Exception as e:
        print(e)