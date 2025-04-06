import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




dir_path = "C:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder)
file_path1 = dir_path + "\\jadong\\gyucjunji.txt"

if os.path.isfile(file_path1) == True:
    with open(file_path1, "r", encoding='utf-8-sig') as file:
        read_gyucjunji = file.read().splitlines()

def gyucjunji_check(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from massenger import line_to_me
    from function_game import imgs_set_, macro_out, click_pos_2
    from game_check import out_check, attack_check
    from action import juljun_check, juljun_on, attack_on, juljun_off
    from clean_screen import clean_screen_start
    from jadong import jadong_mode
    from dead_die import dead_check

    try:
        print("gyucjunji_check", data)

        # read_gyucjunji
        # 12_벨라토_[45/46]갈리오침식지
        # 18_아크레시아_[78/79]사우라콜로니
        # 11_코라_[61/62]누메러스고원

        # 자동_[45/46]갈리오침식지

        ###############################

        read_data = data.split("_")

        # read_data[1] => 맵 이름

        ###################################

        result_data_ready = "none"

        scan_data = read_gyucjunji

        for r in range(len(scan_data)):
            compare_data = scan_data[r].split("_")
            if compare_data[2] == read_data[1]:
                result_data_ready = scan_data[r]
                break

        # 2_아크레시아_[45]제국군통제지역
        # 2_벨라토_[45]연방군통제지역
        # 2_코라_[45]동맹군통제지역
        # 9_중립_[50]교전구역뱀의등뼈

        # 격전지_[50]교전구역뱀의등뼈

        if result_data_ready == "none":
            print("와 없노")
            why = "해당맵 못 찾음"
            line_to_me(cla, why)
            macro_out(cla)
        else:
            result_data = result_data_ready.split("_")
            print("result_data_ready", result_data_ready)
            # result_data[0] => 맵 숫자, 최종클릭위치
            # result_data[1] => 타이틀맵
            # result_data[2] => 맵 이름

            if result_data[1] == "벨라토":
                title_map = "bellato"
            elif result_data[1] == "아크레시아":
                title_map = "acrecia"
            elif result_data[1] == "코라":
                title_map = "kora"
            elif result_data[1] == "중립":
                title_map = "joonglib"


            des_map = result_data[0]

            result_juljun = juljun_check(cla)
            if result_juljun == True:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\juljun_map\\" + str(title_map) + "\\" + str(des_map) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 510, 900, 555, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("this map", str(title_map), str(des_map), imgs_)
                    result_attack = attack_check(cla)
                    if result_attack == True:
                        # potion_check(cla)
                        jadong_mode(cla)
                    else:
                        juljun_off(cla)
                        click_pos_2(920, 925, cla)
                        juljun_on(cla)
                else:
                    gyucjunji_in_ready(cla, data)
                    gyucjunji_in(cla, data)
                    gyucjunji_jadong_in(cla, data)
            else:

                dead_check(cla)

                result_out = out_check(cla)
                if result_out == True:
                    juljun_on(cla)
                else:
                    clean_screen_start(cla)


    except Exception as e:
        print(e)


def gyucjunji_jadong_in(cla, data):
    import numpy as np
    import cv2

    from function_game import macro_out, click_pos_reg, click_pos_2, imgs_set_
    from massenger import line_to_me
    from game_check import move_check, out_check
    from clean_screen import clean_screen_start
    from action import attack_on, juljun_on




    try:
        print("gyucjunji_jadong_in", data)

        # 2_아크레시아_[45]제국군통제지역
        # 2_벨라토_[45]연방군통제지역
        # 2_코라_[45]동맹군통제지역
        # 9_중립_[50]교전구역뱀의등뼈

        # 격전지_[50]교전구역뱀의등뼈

        ###############################

        read_data = data.split("_")

        # read_data[1] => 맵 이름

        ###################################

        result_data_ready = "none"

        scan_data = read_gyucjunji

        for r in range(len(scan_data)):
            compare_data = scan_data[r].split("_")
            if compare_data[2] == read_data[1]:
                result_data_ready = scan_data[r]
                break

        if result_data_ready == "none":
            print("와 없노")
            why = "해당맵 못 찾음"
            line_to_me(cla, why)
            macro_out(cla)
        else:
            result_data = result_data_ready.split("_")
            print("result_data_ready", result_data_ready)
            # result_data[0] => 맵 숫자, 최종클릭위치
            # result_data[1] => 타이틀맵
            # result_data[2] => 맵 이름

            # 385, 410, 435, 460

            if result_data[1] == "벨라토":
                title_map = "bellato"
                y_plus = 235 - 25
            elif result_data[1] == "아크레시아":
                title_map = "acrecia"
                y_plus = 210 - 25
            elif result_data[1] == "코라":
                title_map = "kora"
                y_plus = 260 - 25
            elif result_data[1] == "중립":
                title_map = "joonglib"
                y_plus = 160 - 25

            y_reg = y_plus + (25 * int(result_data[0]))

            is_data = True
            is_data_count = 0
            while is_data is True:
                is_data_count += 1
                if is_data_count > 7:
                    is_data = False

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\worldmap_house.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 200, 60, 270, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("worldmap_house", imgs_)

                    is_data = False

                    # 큰 타이틀 열기

                    for i in range(5):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\title_map\\" + str(title_map) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 100, 200, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("title_map", str(title_map), imgs_)
                            break
                        else:
                            click_pos_2(35, 200, cla)
                        QTest.qWait(1000)

                    # 세부 타이틀 열기

                    for i in range(5):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\title_map_open\\" + str(title_map) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 100, 200, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("title_map_open", str(title_map), imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\title_map\\" + str(
                                title_map) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 100, 200, 1040, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(1000)

                    # 즉시이동 활성화하기

                    for i in range(5):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\immediately_move_btn_1_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(200, 110, 740, 940, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("immediately_move_btn_1_1", str(title_map), imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\immediately_move_btn_1_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(200, 110, 740, 940, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("immediately_move_btn_1_2", str(title_map), imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                break
                            else:
                                click_pos_2(100, y_reg, cla)
                        QTest.qWait(1000)

                    # 즉시이동 활성화하기2

                    for i in range(5):

                        result_out = out_check(cla)
                        if result_out == True:
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\immediately_move_btn_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(480, 605, 605, 650, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("immediately_move_btn_2", str(title_map), imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\immediately_move_btn_1_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(200, 110, 740, 940, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("immediately_move_btn_1_1", str(title_map), imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\immediately_move_btn_1_2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(200, 110, 740, 940, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("immediately_move_btn_1_2", str(title_map), imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(1000)

                    # 공격만...
                    attack_on(cla)


                    # 공격하고 절전모드하기
                    juljun_on(cla)

                else:
                    result_out = out_check(cla)
                    if result_out == True:

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\jabhwa_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(24, 52, cla)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\guild_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(24, 52, cla)
                            else:
                                click_pos_2(110, 100, cla)
                    else:
                        clean_screen_start(cla)
                QTest.qWait(1000)




    except Exception as e:
        print(e)

def gyucjunji_in(cla, data):
    import numpy as np
    import cv2

    from function_game import click_pos_reg, imgs_set_
    from action import menu_open, confirm_all
    from game_check import loading_check, out_check, move_check, move_check_pure

    try:
        print("gyucjunji_in", data)

        # 격전지_45, 50, 55
        # 격전지_60

        read_data = data.split("_")

        is_dun = True
        is_dun_count = 0
        while is_dun is True:
            is_dun_count += 1
            if is_dun_count > 10:
                is_dun = False


            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\gyucjunji.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("gyucjunji", imgs_)

                # 격전지_45, 50, 55
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\enter_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 710, 400, 755, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("enter_btn", imgs_)

                    click_pos_reg(imgs_.x, imgs_.y, cla)

                    for i in range(10):
                        result_out = out_check(cla)
                        if result_out == True:
                            is_dun = False
                            break
                        else:
                            loading_check(cla)
                        time.sleep(0.5)


            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\gyucjunji_des_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 295, 550, 355, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("gyucjunji_des_title", imgs_)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_6.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:
                        print("close_6", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\gyucjunji_participation_request_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(400, 380, 550, 430, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        confirm_all(cla)

                        for i in range(10):
                            result_move = move_check_pure(cla)
                            if result_move == True:
                                move_check(cla)
                                break
                            else:
                                loading_check(cla)
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\gyucjunji.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                break
                            time.sleep(0.5)

                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\menu_gyucjunji.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 290, 880, 360, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\arrive_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 60, 620, 120, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("arrive_notice", imgs_)
                                    is_dun = False
                                    break
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\gyucjunji_participation_request_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(400, 380, 550, 430, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                time.sleep(0.1)


                        else:
                            menu_open(cla)
            QTest.qWait(1000)




    except Exception as e:
        print(e)



def gyucjunji_in_ready(cla, data):
    import numpy as np
    import cv2

    from function_game import click_pos_reg, click_pos_2, imgs_set_
    from action import menu_open, confirm_all
    try:
        print("gyucjunji_in_ready", data)

        # 격전지_45
        # 격전지_60

        read_data = data.split("_")

        is_dun = True
        is_dun_count = 0
        while is_dun is True:
            is_dun_count += 1
            if is_dun_count > 10:
                is_dun = False


            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\national_card.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("national_card", imgs_)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\clicked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(225, 90, 330, 120, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("clicked", imgs_)


                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\clicked_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 995, 745, 1035, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked_2", imgs_)



                        for i in range(10):

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\ganghwa_end_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(820, 995, 940, 1035, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("ganghwa_end_btn", imgs_)
                                is_dun_count = 0
                                time.sleep(3)
                            else:

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\lack_item_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(350, 60, 700, 130, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("lack_item_notice", imgs_)
                                    is_dun = False
                                    break
                                else:
                                    click_pos_2(865, 1015, cla)
                            QTest.qWait(200)

                    else:
                        click_pos_2(755, 1015, cla)


                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\id_card_wearing_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 990, 540, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("id_card_wearing_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\wearing_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(410, 990, 540, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("wearing_btn", imgs_)
                            click_pos_2(880, 1020, cla)

            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\no_have_id_card.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 500, 600, 550, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    confirm_all(cla)

                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\gyucjunji\\menu_national_card.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(810, 125, 880, 195, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        menu_open(cla)
            QTest.qWait(1000)




    except Exception as e:
        print(e)
