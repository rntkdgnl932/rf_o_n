import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

dir_path = "C:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder)
file_path1 = dir_path + "\\jadong\\bellato.txt"
file_path2 = dir_path + "\\jadong\\acrecia.txt"
file_path3 = dir_path + "\\jadong\\kora.txt"

if os.path.isfile(file_path1) == True:
    with open(file_path1, "r", encoding='utf-8-sig') as file:
        read_bellato = file.read().splitlines()

    with open(file_path2, "r", encoding='utf-8-sig') as file:
        read_acrecia = file.read().splitlines()

    with open(file_path3, "r", encoding='utf-8-sig') as file:
        read_kora = file.read().splitlines()

def jadong_check(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from massenger import line_to_me
    from function_game import imgs_set_, macro_out, click_pos_2
    from game_check import out_check, attack_check
    from action import juljun_check, juljun_on, attack_on, juljun_off
    from clean_screen import clean_screen_start
    from potion import potion_check
    from dead_die import dead_check

    try:
        print("jadong_check", data)

        # read_bellato, read_acrecia, read_kora
        # 12_벨라토_[45/46]갈리오침식지
        # 18_아크레시아_[78/79]사우라콜로니
        # 11_코라_[61/62]누메러스고원

        # 자동_[45/46]갈리오침식지

        ###############################

        read_data = data.split("_")

        # read_data[1] => 맵 이름

        ###################################

        result_data_ready = "none"

        for i in range(3):
            if i == 0:
                scan_data = read_bellato
            elif i == 1:
                scan_data = read_acrecia
            elif i == 2:
                scan_data = read_kora

            for r in range(len(scan_data)):
                compare_data = scan_data[r].split("_")
                if compare_data[2] == read_data[1]:
                    result_data_ready = scan_data[r]
                    break
            if result_data_ready != "none":
                break

        # read_bellato, read_acrecia, read_kora
        # 12_벨라토_[45/46]갈리오침식지
        # 18_아크레시아_[78/79]사우라콜로니
        # 11_코라_[61/62]누메러스고원

        # 자동_[45/46]갈리오침식지

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

            des_map = result_data[0]

            result_juljun = juljun_check(cla)
            if result_juljun == True:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\juljun_map\\" + str(title_map) + "\\" + str(des_map) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 510, 900, 555, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("this map", str(title_map), str(des_map), imgs_)
                    result_attack = attack_check(cla)
                    if result_attack == True:
                        # potion_check(cla)
                        jadong_mode(cla, title_map, des_map)
                    else:
                        juljun_off(cla)
                        click_pos_2(920, 925, cla)
                        juljun_on(cla)
                else:
                    jadong_in(cla, data)
            else:

                dead_check(cla)

                result_out = out_check(cla)
                if result_out == True:
                    juljun_on(cla)
                else:
                    clean_screen_start(cla)


    except Exception as e:
        print(e)


def jadong_in(cla, data):
    import numpy as np
    import cv2

    from function_game import macro_out, click_pos_reg, click_pos_2, imgs_set_
    from massenger import line_to_me
    from game_check import move_check, out_check
    from clean_screen import clean_screen_start
    from action import attack_on, juljun_on




    try:
        print("jadong_in", data)

        # read_bellato, read_acrecia, read_kora
        # 12_벨라토_[45/46]갈리오침식지
        # 18_아크레시아_[78/79]사우라콜로니
        # 11_코라_[61/62]누메러스고원

        # 자동_[45/46]갈리오침식지

        ###############################

        read_data = data.split("_")

        # read_data[1] => 맵 이름

        ###################################

        result_data_ready = "none"

        for i in range(3):
            if i == 0:
                scan_data = read_bellato
            elif i == 1:
                scan_data = read_acrecia
            elif i == 2:
                scan_data = read_kora

            for r in range(len(scan_data)):
                compare_data = scan_data[r].split("_")
                if compare_data[2] == read_data[1]:
                    result_data_ready = scan_data[r]
                    break
            if result_data_ready != "none":
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
                y_plus = 335 - 25
            elif result_data[1] == "아크레시아":
                title_map = "acrecia"
                y_plus = 380 - 25
            elif result_data[1] == "코라":
                title_map = "kora"
                y_plus = 360 - 25

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
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\title_map\\" + str(title_map) + ".PNG"
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
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\title_map_open\\" + str(title_map) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 100, 200, 1040, cla, img, 0.9)
                        if imgs_ is not None and imgs_ != False:
                            print("title_map_open", str(title_map), imgs_)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\title_map\\" + str(
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




def jadong_mode(cla, title_map, des_map):
    import numpy as np
    import cv2

    from function_game import click_pos_reg, imgs_set_, click_pos_2, macro_out, drag_pos
    from potion import potion_buy
    from massenger import line_to_me



    try:
        print("jadong_mode")
        # * 0.2
        # 300 => 1분
        # 30 => 6초
        count = 30

        jadong_mode = True

        jadong_mode_count = 0

        while jadong_mode is True:

            jadong_mode_count += 1

            minute = jadong_mode_count // count

            if jadong_mode_count % count == 0:
                print("자동전투 감지중", str(minute), "분")

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\check\\game_title_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 960, 1030, v_.now_cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:


                click_ready = False
                potion_need = False
                jangsigan = False




                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_maul\\maul_move_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(630, 980, 675, 1030, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("maul_move_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    click_ready = True

                else:

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\juljun_map\\" + str(
                        title_map) + "\\" + str(des_map) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 510, 900, 555, cla, img, 0.9)
                    if imgs_ is not None and imgs_ != False:

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\juljun_zero.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(250, 970, 305, 1035, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("juljun_zero", imgs_)
                            potion_need = True
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\juljun_zero_2.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(250, 970, 305, 1035, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("juljun_zero_2", imgs_)
                                potion_need = True
                    else:

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\check\\game_start_ready_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 50, 960, 1030, v_.now_cla, img, 0.7)
                        if imgs_ is not None and imgs_ != False:
                            print("잠시 조작중....")
                            time.sleep(10)

                        else:

                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\juljun_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 80, 580, 130, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:

                                is_map_in = False

                                for i in range(5):
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\juljun_map\\" + str(
                                        title_map) + "\\" + str(des_map) + ".PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(700, 510, 900, 555, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        is_map_in = True
                                        jadong_mode = False
                                        break
                                    time.sleep(0.2)

                                if is_map_in == False:
                                    why = "자동전투 중 꺼짐 : 사냥터가 아니다."

                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\jangsigan_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(330, 500, 500, 700, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("jangsigan_1", imgs_)

                                    click_pos_2(480, 620, cla)

                                    why = "자동전투 중 꺼짐 장시간"

                                    jangsigan = True

                                    time.sleep(1)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\re_join_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(330, 500, 500, 700, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("re_join_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)

                                        why = "자동전투 중 꺼짐 재접속"

                                        jadong_mode = False

                            line_to_me(cla, why)
                if click_ready == True:
                    print("click_ready")
                    for i in range(30):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\jabhwa_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_btn", imgs_)
                            jadong_mode = False
                            potion_buy(cla)
                            break

                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_maul\\maul_move_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(630, 980, 675, 1030, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(200)

                if potion_need == True:
                    print("potion_need")

                    for i in range(30):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\potion\\jabhwa_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 40, 190, 210, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("jabhwa_btn", imgs_)
                            jadong_mode = False
                            potion_buy(cla)
                            break
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\juljun\\juljun_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(350, 80, 580, 130, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                drag_pos(480, 520, 860, 520, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\action\\go_maul\\maul_move_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(630, 980, 675, 1030, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                        QTest.qWait(300)
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\jadong\\jadong_2.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(25, 75, 61, 110, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("jadong_2", imgs_)

                        jadong_mode = False

                        potion_buy(cla)



                if jangsigan == True:
                    jadong_mode = False

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\jangsigan_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(330, 500, 500, 600, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("jangsigan_1", imgs_)

                        click_pos_2(480, 620, cla)





            else:
                why = "자동전투 중 꺼짐, 프로그램 off"
                line_to_me(cla, why)
                macro_out(cla)
            QTest.qWait(200)



    except Exception as e:
        print(e)

