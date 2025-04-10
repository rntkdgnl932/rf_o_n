import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def quest_start(cla, data):
    import numpy as np
    import cv2

    from function_game import macro_out, imgs_set_, click_pos_2, drag_pos
    from game_check import out_check, move_check_pure
    from clean_screen import clean_screen_start
    from action import confirm_all, juljun_check, juljun_off
    from dead_die import dead_check
    from tuto import way_check, quest_complete, tuto_skip, quest_on_check

    try:
        print("quest_start", data)
        # 절전모드는 무조건 풀고

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            juljun_off(cla)

        quest_complete(cla)

        dead_check(cla)

        way_check(cla)

        tuto_skip(cla)



        result_quest_on = quest_on_check(cla)
        if result_quest_on == False:

            # 여기에서 메인, 서브, 국가 퀘스트 시작하기
            # 퀘스트_메인, 퀘스트_서브, 퀘스트_국가

            result_confirm = confirm_all(cla)

            if result_confirm == False:



                read_data = data.split("_")

                quest_get(cla, read_data[1])


                for i in range(5):
                    result_confirm = confirm_all(cla)
                    if result_confirm == True:
                        break
                    QTest.qWait(500)
        else:
            result_move = move_check_pure(cla)

            if result_move == True:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\googa_out_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(710, 100, 745, 175, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("googa_out_btn", imgs_)
                    click_pos_2(900, imgs_.y, cla)

                for i in range(3):
                    result_confirm = confirm_all(cla)
                    if result_confirm == True:
                        break
                    QTest.qWait(500)

        quide_quest_check(cla)


    except Exception as e:
        print(e)



def quest_get(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open_pure, confirm_all
    from schedule import myQuest_play_add

    try:
        print("quest_get", data)

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : quest")

                is_get = True

                if data == "메인":
                    click_pos_2(60, 95, cla)
                    time.sleep(0.2)
                    click_pos_2(60, 95, cla)
                elif data == "서브":
                    click_pos_2(170, 95, cla)
                    time.sleep(0.2)
                    click_pos_2(170, 95, cla)
                elif data == "국가":
                    click_pos_2(280, 95, cla)
                    time.sleep(0.2)
                    click_pos_2(280, 95, cla)

                add_data = "퀘스트_" + str(data)

                QTest.qWait(500)


                if data == "국가":

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\quest_giveup.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(640, 995, 790, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("quest_giveup", imgs_)

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\quest_cancle.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 995, 945, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_cancle", imgs_)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\quest_soolock_btn_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 995, 945, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("quest_soolock_btn", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)

                        # 나가기

                        for i in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(935, 55, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\googa_out_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(710, 100, 745, 175, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("googa_out_btn", imgs_)
                                    break
                            QTest.qWait(1000)




                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\googa_out_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(710, 100, 745, 175, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("googa_out_btn", imgs_)
                            click_pos_2(900, imgs_.y, cla)
                    else:
                        is_btn = False
                        for i in range(3):
                            btn = i + 1
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\quest_soolock_btn_" + str(btn) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(790, 995, 945, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("quest_soolock_btn", str(btn), imgs_)
                                is_btn = True
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(1)

                                break

                        for i in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(935, 55, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\googa_out_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(710, 100, 745, 175, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("googa_out_btn", imgs_)
                                    break
                            QTest.qWait(1000)
                        if is_btn == True:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\googa_out_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(710, 100, 745, 175, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("googa_out_btn", imgs_)
                                click_pos_2(900, imgs_.y, cla)
                        else:
                            myQuest_play_add(cla, add_data)
                else:
                    is_btn = False
                    for i in range(3):
                        btn = i + 1
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\quest_soolock_btn_" + str(btn) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(790, 995, 945, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("quest_soolock_btn", str(btn), imgs_)
                            is_btn = True
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(1)

                            break
                    if is_btn == False:
                        myQuest_play_add(cla, add_data)
                    else:
                        if data == "서브":
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                            if imgs_ is not None and imgs_ != False:
                                myQuest_play_add(cla, add_data)

                                for i in range(5):
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(30, 30, 160, 80, cla, img, 0.9)
                                    if imgs_ is not None and imgs_ != False:
                                        click_pos_2(30, 60, cla)
                                    else:
                                        break
                                    time.sleep(1)


            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\quest.PNG"
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
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\menu_quest.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(730, 240, 780, 300, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_quest")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)
    except Exception as e:
        print(e)




def quide_quest_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg
    from clean_screen import clean_screen_start

    try:
        print("quide_quest_check")

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\quest\\guide_click_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(720, 80, 790, 250, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("guide_click_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            QTest.qWait(1000)
            clean_screen_start(cla)
        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\clean_screen\\close_5.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("close_5", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                QTest.qWait(500)


    except Exception as e:
        print(e)

