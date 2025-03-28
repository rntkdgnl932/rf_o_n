import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from schedule import myQuest_play_add, myQuest_play_check
    from function_game import imgs_set_, macro_out
    from massenger import line_to_me

    try:
        print("dead_check")

        is_data = False

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 30, 750, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)
            is_data = True

        else:
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_notice.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(330, 60, 700, 540, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("dead_notice", imgs_)
                is_data = True
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_notice2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 60, 700, 540, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dead_notice", imgs_)
                    is_data = True

        if is_data == True:

            result_schedule = myQuest_play_check(cla, "check")
            print("result_schedule", result_schedule)
            character_id = result_schedule[0][1]
            result_schedule_ = result_schedule[0][2]

            v_.dead_count += 1
            if v_.dead_count > 4:
                why = "하루 5번 죽었다"
                line_to_me(cla, why)
                macro_out(cla)


            if "튜토육성" in result_schedule_:
                myQuest_play_add(cla, result_schedule_)

            dead_recovery(cla)


    except Exception as e:
        print(e)


def dead_recovery(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import macro_out, click_pos_reg, click_pos_2
    from function_game import imgs_set_
    from potion import potion_buy

    try:
        print("dead_recovery")

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(650, 30, 750, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)


            is_penalty = True
            is_penalty_count = 0
            while is_penalty is True:
                is_penalty_count += 1
                if is_penalty_count > 7:
                    is_penalty = False

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_penalty_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 340, 530, 380, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dead_penalty_title", imgs_)

                    # 경험치부터
                    click_pos_2(415, 395, cla)
                    time.sleep(0.5)

                    for i in range(10):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\recovery_item_ready.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(440, 545, 525, 585, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(550, 620, cla)
                        else:
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\fix_item.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(460, 560, 660, 660, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(550, 620, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_penalty_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 340, 530, 380, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\anymore_exp.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(380, 500, 570, 570, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        break
                                    else:
                                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\recovery_item.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(575, 690, 630, 735, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            click_pos_2(480, 710, cla)
                                else:
                                    break
                        QTest.qWait(1000)

                    # 장비
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_penalty_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 340, 530, 380, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(555, 395, cla)
                        time.sleep(0.5)

                        for i in range(10):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\recovery_item_ready.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(440, 545, 525, 585, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(550, 620, cla)
                            else:
                                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\fix_item.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(460, 560, 660, 660, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    click_pos_2(550, 620, cla)
                                else:
                                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\dead_penalty_title.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(420, 340, 530, 380, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\anymore_exp.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(380, 500, 570, 570, cla, img, 0.85)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        else:
                                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\recovery_item.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(575, 690, 630, 735, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                            else:
                                                click_pos_2(480, 710, cla)
                                    else:
                                        break
                            QTest.qWait(1000)

                else:
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\dead_die\\boohwal_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(650, 30, 750, 80, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                QTest.qWait(1000)



    except Exception as e:
        print(e)
