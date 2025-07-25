import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from massenger import line_to_me
    from function_game import imgs_set_, macro_out, click_pos_2
    from game_check import out_check, attack_check
    from action import juljun_check, juljun_on, attack_on, juljun_off, go_random
    from clean_screen import clean_screen_start
    from potion import potion_check
    from schedule import myQuest_play_add

    try:
        print("dungeon_start", data)

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\dungeon.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            dun_in(cla, data)
        else:

            # 던전_바이오슈트
            # 던전_신기
            # 던전_폐기장_8
            # 던전_비밀기지

            read_data = data.split("_")

            is_dun = False

            if read_data[1] == "바이오슈트" or read_data[1] == "신기":
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\ScienceTrainingCenter.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 200, 80, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("ScienceTrainingCenter", imgs_)
                    dun_ing(cla, data)
                    is_dun = True
            elif read_data[1] == "폐기장" or read_data[1] == "비밀기지" or read_data[1] == "채굴장":
                if read_data[1] == "폐기장":
                    dun_name = "pyegijang"

                elif read_data[1] == "비밀기지":
                    dun_name = "secret_base"

                elif read_data[1] == "채굴장":
                    dun_name = "chaegool"

                result_juljun = juljun_check(cla)
                if result_juljun == True:

                    is_dun = False

                    for i in range(10):


                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\" + str(dun_name) + "\\" + str(dun_name) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 515, 900, 555, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            if read_data[1] == "폐기장":
                                print("pyegijang", imgs_)

                            elif read_data[1] == "비밀기지":
                                print("secret_base", imgs_)

                            elif read_data[1] == "채굴장":
                                print("chaegool", imgs_)

                            is_dun = True

                            break

                        QTest.qWait(500)

                    if is_dun == True:

                        result_attack = attack_check(cla)
                        if result_attack == True:
                            potion_check(cla)
                        else:
                            juljun_off(cla)
                            result_random = go_random(cla)
                            if result_random == True:
                                click_pos_2(920, 925, cla)
                                juljun_on(cla)
                            else:
                                is_dun = False
                    else:
                        is_dun = False
                else:
                    result_out = out_check(cla)
                    if result_out == True:
                        juljun_on(cla)
                    else:
                        clean_screen_start(cla)




            if is_dun == False:
                dun_in(cla, data)


    except Exception as e:
        print(e)


def dun_ing(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import macro_out, click_pos_reg, click_pos_2, imgs_set_
    from schedule import myQuest_play_add
    from game_check import loading_check

    try:
        print("dun_ing", data)




        # 던전_바이오슈트
        # 던전_신기
        # 던전_폐기장
        # 던전_비밀기지

        read_data = data.split("_")

        is_dun = True
        is_dun_count = 0
        while is_dun is True:


            if read_data[1] == "바이오슈트" or read_data[1] == "신기":
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\ScienceTrainingCenter.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 200, 80, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("ScienceTrainingCenter", imgs_)

                    is_dun_count = 0




                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\next_stage_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(440, 930, 650, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("next_stage_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\stage_failed_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(100, 300, 700, 900, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("stage_failed_notice", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\stage_failed_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 300, 700, 900, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("stage_failed_notice", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    loading_check(cla)
                                time.sleep(0.3)

                            is_dun = False

                            # 소탕해버리깅
                            dun_in_sotang(cla, data)

                        else:

                            is_dun_count += 1
                            if is_dun_count > 3:
                                is_dun = False

            QTest.qWait(1000)




    except Exception as e:
        print(e)

def dun_in(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import drag_pos, click_pos_reg, click_pos_2, imgs_set_
    from action import menu_open, go_random, juljun_on
    from game_check import loading_check, out_check
    from schedule import myQuest_play_add
    from clean_screen import clean_screen_start
    from potion import potion_buy

    try:
        print("dun_in", data)

        # 던전_바이오슈트
        # 던전_신기
        # 던전_폐기장_8
        # 던전_비밀기지

        dir_path = "C:\\my_games"
        file_path = dir_path + "\\line\\line.txt"

        isLine = False
        while isLine is False:
            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_ = file.read()
                if read_ == "":
                    print("empty")
                    line_data = "ccocco:뿌에에에에에엥"
                    with open(file_path, "w", encoding='utf-8-sig') as file:
                        file.write(line_data)
                else:
                    isLine = True
                    print("read_", read_)
            else:
                line_data = "ccocco:메롱메롱"
                with open(file_path, "w", encoding='utf-8-sig') as file:
                    file.write(line_data)

        read_result = read_.split(":")

        if read_result[0] == "suko":
            potion_buy(cla)


        read_data = data.split("_")

        is_dun = True
        is_dun_count = 0
        while is_dun is True:
            is_dun_count += 1
            if is_dun_count > 10:
                is_dun = False

            if read_data[1] == "바이오슈트" or read_data[1] == "신기":

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\ScienceTrainingCenter.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 30, 200, 80, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("ScienceTrainingCenter", imgs_)
                    is_dun = False
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("dungeon", imgs_)
                        if read_data[1] == "바이오슈트":
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\zero_1.PNG"
                        elif read_data[1] == "신기":
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\singi\\zero_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        if read_data[1] == "바이오슈트":
                            imgs_ = imgs_set_(360, 400, 435, 450, cla, img, 0.85)
                        elif read_data[1] == "신기":
                            imgs_ = imgs_set_(815, 400, 880, 450, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("zero_1", imgs_)
                            myQuest_play_add(cla, data)
                            is_dun = False


                        else:
                            click_pos_2(60, 95, cla)
                            time.sleep(0.5)

                            if read_data[1] == "바이오슈트":
                                click_pos_2(255, 735, cla)
                            elif read_data[1] == "신기":
                                click_pos_2(735, 735, cla)

                            for i in range(10):
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\ticket_lack_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 40, 800, 160, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("ticket_lack_notice", imgs_)
                                    myQuest_play_add(cla, data)
                                    is_dun = False
                                    break
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\singi\\not_complete_notice.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(300, 40, 800, 160, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_complete_notice", imgs_)
                                        myQuest_play_add(cla, data)
                                        is_dun = False
                                        break

                                time.sleep(0.1)

                            loading_check(cla)
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\menu_dun.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)
            elif read_data[1] == "폐기장" or read_data[1] == "비밀기지" or read_data[1] == "채굴장":

                # 던전_바이오슈트
                # 던전_신기
                # 던전_폐기장_8
                # 던전_비밀기지_3
                # 던전_채굴장_3

                # read_data = data.split("_")

                y_reg = 1
                step = str(read_data[2])

                if read_data[1] == "폐기장":
                    dun_name = "pyegijang"

                elif read_data[1] == "비밀기지":
                    dun_name = "secret_base"
                    if int(read_data[2]) > 2:
                        step = "3"
                elif read_data[1] == "채굴장":
                    dun_name = "chaegool"
                    if int(read_data[2]) > 2:
                        step = "3"


                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\" + str(dun_name) + "\\title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 380, 560, 430, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    if read_data[1] == "폐기장":
                        print("title : pyegijang", imgs_)
                    elif read_data[1] == "비밀기지":
                        print("title : secret_base", imgs_)
                    elif read_data[1] == "채굴장":
                        print("title : chaegool", imgs_)



                    # read_data[2]

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\pyegijang\\num\\" + str(step) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(250, 430, 325, 680, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("step", str(step), imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.2)
                        click_pos_2(660, 660, cla)
                        is_dun = False
                    else:
                        if read_data[1] == "폐기장":
                            if int(read_data[2]) < 5:
                                drag_pos(290, 460, 290, 660, cla)
                            else:
                                drag_pos(290, 660, 290, 460, cla)


                    if is_dun == False:
                        for i in range(30):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\same_spot.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 480, 525, 525, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                clean_screen_start(cla)
                                result_random = go_random(cla)
                                if result_random == True:
                                    click_pos_2(920, 925, cla)
                                    juljun_on(cla)
                                    break
                                else:
                                    break
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\pyegijang\\time_lack_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(270, 60, 630, 130, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("time_lack_notice", imgs_)
                                    myQuest_play_add(cla, data)
                                    is_dun = False
                                    break
                                else:
                                    result_out = out_check(cla)
                                    if result_out == True:
                                        result_random = go_random(cla)
                                        if result_random == True:
                                            click_pos_2(920, 925, cla)
                                            juljun_on(cla)
                                            break
                                        else:
                                            break
                                    else:
                                        loading_check(cla)
                            QTest.qWait(300)



                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\" + str(dun_name) + "\\clicked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(200, 130, 500, 200, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("clicked", imgs_)

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\pyegijang\\zero.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(850, 900, 915, 970, cla, img, 0.99)
                        if imgs_ is not None and imgs_ != False:
                            print("zero", imgs_)
                            myQuest_play_add(cla, data)
                            is_dun = False
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\pyegijang\\dun_in_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(770, 990, 950, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("dun_in_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                myQuest_play_add(cla, data)
                                is_dun = False
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\dungeon.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("dungeon", imgs_)
                            click_pos_2(280, 95, cla)
                            time.sleep(0.5)
                            if read_data[1] == "폐기장":
                                click_pos_2(100, 155, cla)
                            elif read_data[1] == "비밀기지":
                                click_pos_2(100, 220, cla)
                            elif read_data[1] == "채굴장":
                                click_pos_2(100, 285, cla)
                            time.sleep(0.5)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\menu_dun.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                menu_open(cla)
            QTest.qWait(1000)




    except Exception as e:
        print(e)




def dun_in_sotang(cla, data):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import drag_pos, click_pos_reg, click_pos_2, imgs_set_
    from action import menu_open, go_random, juljun_on, confirm_all
    from game_check import loading_check, out_check
    from schedule import myQuest_play_add
    from clean_screen import clean_screen_start

    try:
        print("dun_in", data)

        # 던전_바이오슈트
        # 던전_신기
        # 던전_폐기장_8
        # 던전_비밀기지

        read_data = data.split("_")

        is_dun = True
        is_dun_count = 0
        while is_dun is True:
            is_dun_count += 1
            if is_dun_count > 10:
                is_dun = False


            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\ScienceTrainingCenter.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(50, 30, 200, 80, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("ScienceTrainingCenter", imgs_)
                is_dun = False
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\dungeon.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(30, 30, 200, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dungeon", imgs_)
                    if read_data[1] == "바이오슈트":
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\zero_1.PNG"
                    elif read_data[1] == "신기":
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\singi\\zero_1.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    if read_data[1] == "바이오슈트":
                        imgs_ = imgs_set_(360, 400, 435, 450, cla, img, 0.85)
                    elif read_data[1] == "신기":
                        imgs_ = imgs_set_(815, 400, 880, 450, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("zero_1", imgs_)
                        myQuest_play_add(cla, data)
                        is_dun = False


                    else:
                        click_pos_2(60, 95, cla)
                        time.sleep(0.5)

                        for i in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\sotang_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 360, 515, 410, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("sotang_title 1", imgs_)
                                break
                            else:
                                if read_data[1] == "바이오슈트":
                                    click_pos_2(135, 735, cla)
                                elif read_data[1] == "신기":
                                    click_pos_2(600, 735, cla)
                            time.sleep(0.5)

                        # 소탕
                        for i in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\sotang_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 360, 515, 410, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("sotang_title 2", imgs_)
                                confirm_all(cla)
                            else:
                                break
                            time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\bio_suit\\ticket_lack_notice.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(300, 40, 800, 160, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("ticket_lack_notice", imgs_)
                                myQuest_play_add(cla, data)
                                is_dun = False
                                break
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\singi\\not_complete_notice.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(300, 40, 800, 160, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("not_complete_notice", imgs_)
                                    myQuest_play_add(cla, data)
                                    is_dun = False
                                    break
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\get_sotang.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(470, 430, 570, 490, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("get_sotang", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        myQuest_play_add(cla, data)
                                        is_dun = False
                                        break

                            time.sleep(0.1)
                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dungeon\\menu_dun.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        menu_open(cla)

            QTest.qWait(1000)




    except Exception as e:
        print(e)
