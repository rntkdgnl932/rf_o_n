import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def mission_start(cla, data):
    import numpy as np
    import cv2

    from function_game import macro_out, imgs_set_, click_pos_2, drag_pos
    from game_check import out_check, move_check_pure
    from quest import quide_quest_check
    from action import confirm_all, juljun_check, juljun_off
    from dead_die import dead_check
    from tuto import way_check, quest_complete, quest_on_check

    try:
        print("mission_start")
        # 절전모드는 무조건 풀고

        result_juljun = juljun_check(cla)
        if result_juljun == True:
            juljun_off(cla)

        quest_complete(cla)

        result_dead = dead_check(cla)

        if result_dead == False:


            result_quest_on = quest_on_check(cla)
            if result_quest_on == False:

                # 여기에서
                # 일일미션 (이것으로 주간 및 월간 전부 받기)

                result_confirm = confirm_all(cla)

                if result_confirm == False:

                    if v_.daily_mission_ready == True:
                        mission_get(cla, data)
                        v_.daily_mission_ready = False
                    else:
                        mission_get_des(cla, "daily", data)


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



def mission_get(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action import menu_open_pure



    try:
        print("mission_get", data)

        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : mission")

                is_get = True

                # step 1 : 월간미션 받기

                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\month_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(705, 105, 755, 135, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("month_mission")

                        mission_get_des(cla, "month", data)

                        break
                    else:
                        click_pos_2(280, 95, cla)
                    QTest.qWait(500)




                # step 2 : 주간미션 받기
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\week_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(705, 105, 755, 135, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("week_mission")

                        mission_get_des(cla, "week", data)

                        break
                    else:
                        click_pos_2(170, 95, cla)
                    QTest.qWait(500)

                # step 3 : 일일미션 받기
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\daily_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(705, 105, 755, 135, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("daily_mission")

                        mission_get_des(cla, "daily", data)


                        break
                    else:
                        click_pos_2(60, 95, cla)
                    QTest.qWait(500)

                # 다 받았으면 일일미션 진행하기


            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\mission.PNG"
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
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\menu_mission.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_mission")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)
    except Exception as e:
        print(e)


def mission_get_des(cla, data, chapter):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action import menu_open_pure, confirm_all
    from schedule import myQuest_play_add
    from clean_screen import clean_screen_start

    try:
        print("mission_get_des", data)

        my_list = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\" + str(data)
        file_list = os.listdir(my_list)

        if "_" in chapter:

            ready_chapter = chapter.split("_")
            is_chapter = ready_chapter[1]

        else:

            is_chapter = "4"


        is_get = False
        is_get_count = 0
        while is_get is False:
            is_get_count += 1
            if is_get_count > 7:
                is_get = True
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 160, 100, cla, img, 0.9)
            if imgs_ is not None and imgs_ != False:
                print("title : mission")




                # step
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\" + str(data) + "_mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(705, 105, 755, 135, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("mission", str(data))
                        break
                    else:
                        if data == "month":
                            click_pos_2(280, 95, cla)
                        elif data == "week":
                            click_pos_2(170, 95, cla)
                        elif data == "daily":
                            click_pos_2(60, 95, cla)
                    QTest.qWait(500)

                # 완료하기(각 챕터들 보기)

                # chapter_lock
                # 165, 215, 265, 315, 365, 415

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\chapter_lock.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(50, 135, 110, 600, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("chapter_lock", imgs_)

                    for i in range(6):
                        lock_reg = 165 + 25 + (50 * i)

                        print("lock_reg", lock_reg)

                        if imgs_.y < lock_reg:
                            is_lock = str(i)
                            break

                else:
                    is_lock = "6"

                print("is_lock", is_lock)

                if is_lock == "0":
                    is_get = True
                    myQuest_play_add(cla, chapter)
                else:
                    print("111111111")
                    for i in range(10):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\mission_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(110, 130, 160, 600, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_point_1", imgs_)
                            click_pos_reg(imgs_.x - 30, imgs_.y + 5, cla)
                            QTest.qWait(500)

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\complete_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(600, 160, 730, 860, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("complete_1", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                            click_pos_2(900, 1015, cla)
                            time.sleep(0.5)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            break
                        QTest.qWait(200)



                    # 미션 받기

                    # 미션 받기전 챕터 선택하기

                    # 일일미션_4 ~ 9

                    # 165, 215, 265, 315, 365, 415
                    # 4....5....6....7....8....9

                    click_y = (int(is_chapter) * 50) - 35

                    click_pos_2(75, click_y, cla)

                    for m in range(5):

                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\not_complete_quest_notice.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(450, 70, 620, 120, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("not_complete_quest_notice", imgs_)

                            is_get = True
                            myQuest_play_add(cla, chapter)

                            break

                        QTest.qWait(100)
                    print("2222222222222", is_get)
                    if is_get == False:
                        print("333333333333333")
                        for m in range(10):

                            is_list = False

                            for i in range(len(file_list)):

                                y_reg = 150
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\soolock_mission_checked1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_for(40, 150, 270, 860, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("soolock_mission_checked1", imgs_)

                                    if len(imgs_) > 0:
                                        y_reg = imgs_[len(imgs_) - 1][1] + 30
                                        print("y_reg", y_reg)

                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\soolock_mission_checked2.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_for(40, 150, 270, 860, cla, img, 0.75)
                                    if imgs_ is not None and imgs_ != False:
                                        print("soolock_mission_checked2", imgs_)

                                        if len(imgs_) > 0:
                                            y_reg_prepare = imgs_[len(imgs_) - 1][1] + 30
                                            if y_reg < y_reg_prepare:
                                                y_reg = y_reg_prepare
                                            print("y_reg...", y_reg)

                                this_list = file_list[len(file_list) - 1 - i]

                                print("4444444444", this_list)

                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\" + str(data) + "\\" + str(this_list)

                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, y_reg, 600, 860, cla, img, 0.9)
                                if imgs_ is not None and imgs_ != False:

                                    print("this_list", str(this_list), imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)

                                    is_list = True

                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\soolock_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(830, 990, 940, 1040, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("soolock_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        for a in range(10):
                                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\anymore_misson_notice.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(400, 70, 670, 120, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("anymore_misson_notice", imgs_)
                                                is_get = True
                                                break
                                            else:
                                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\anymore_misson_notice_2.PNG"
                                                img_array = np.fromfile(full_path, np.uint8)
                                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                imgs_ = imgs_set_(400, 70, 670, 120, cla, img, 0.85)
                                                if imgs_ is not None and imgs_ != False:
                                                    print("anymore_misson_notice_2", imgs_)
                                                    is_get = True
                                                    break
                                                else:
                                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\chogwa_1.PNG"
                                                    img_array = np.fromfile(full_path, np.uint8)
                                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                                    imgs_ = imgs_set_(400, 70, 670, 120, cla, img, 0.85)
                                                    if imgs_ is not None and imgs_ != False:
                                                        print("chogwa_1", imgs_)
                                                        is_get = True
                                                        break
                                            time.sleep(0.1)
                                if is_get == True:
                                    break
                            if is_get == True:
                                break
                        # 갱신하기
                        if is_list == False:
                            click_pos_2(650, 1020, cla)

                        # 일일미션 실행하기
                        if is_get == True and data == "daily":
                            for i in range(10):
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\complete_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(600, 160, 730, 860, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("complete_1", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    click_pos_2(900, 1015, cla)
                                    time.sleep(0.5)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    break
                                QTest.qWait(200)


                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\soolock_mission_checked1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(40, 150, 270, 860, cla, img, 0.75)
                            if imgs_ is not None and imgs_ != False:
                                print("soolock_mission_checked1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                QTest.qWait(200)
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\jinhang_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(830, 990, 940, 1040, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("jinhang_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_get = True
                                else:
                                    clean_screen_start(cla)


                                    for i in range(5):
                                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\exit_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            print("exit_btn", imgs_)
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            click_pos_2(25, 175, cla)
                                        QTest.qWait(1000)

                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\soolock_mission_checked2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(40, 150, 270, 860, cla, img, 0.75)
                                if imgs_ is not None and imgs_ != False:
                                    print("soolock_mission_checked2", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    time.sleep(0.5)
                                    QTest.qWait(200)
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\jinhang_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(830, 990, 940, 1040, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("jinhang_btn", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        is_get = True
                                    else:
                                        clean_screen_start(cla)

                                        for i in range(5):
                                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\exit_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("exit_btn", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                click_pos_2(25, 175, cla)
                                            QTest.qWait(1000)

                                else:
                                    myQuest_play_add(cla, chapter)

            else:

                is_in = False
                for i in range(5):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\mission.PNG"
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
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\mission\\menu_mission.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_mission")
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open_pure(cla)
                    time.sleep(1)
                if is_in == False:
                    is_get = True
            time.sleep(1)
    except Exception as e:
        print(e)




