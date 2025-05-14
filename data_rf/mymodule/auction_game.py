import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:

        result_dia = 0
        result_silver = 0

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)

            result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
            result_text = change_number(result_text)
            result_dia = int_put_(result_text)
            result_dia_num = in_number_check(result_dia)
            print("result_text", result_dia_num, result_dia)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("silver_reg", imgs_)
            result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
            result_text2 = change_number(result_text2)
            result_silver = int_put_(result_text2)
            result_silver_num = in_number_check(result_silver)
            print("result_text2", result_silver_num, result_silver)

        if result_dia_num == True:

            return result_silver, result_dia

    except Exception as e:
        print(e)


def auction_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, click_pos_2
    from boonhae_collection import boonhae_collection_start
    try:
        # 거래소 들어가서
        # 정산 후
        # 아이템 판매 등록 활성화하고
        auction_in(cla)


        # 현재 최저가 판독
        # result_auction_low_num = auction_low_num(cla)
        # 수량 판독
        # result_auction_qun_num = auction_qun_num(cla)

        # 곱하고
        # result = float(result_auction_low_num) * float(result_auction_qun_num)
        # print("result", result)
        # result = int(result)
        # print("result", result)

        # 판매한다.
        auction_sell(cla)

        # 마무리 전 컬렉에 박아버리고, 장비는 분해하고
        boonhae_collection_start(cla)


    except Exception as e:
        print(e)


def auction_in(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open

    try:
        print("auction_in")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 10:
                is_action = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)

                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\auction_point_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 60, 340, 100, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("auction_point_1", imgs_)

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\jungsan_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 990, 940, 1040, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("jungsan_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    else:
                        click_pos_2(280, 95, cla)
                        time.sleep(0.5)
                else:
                    is_action = True


            else:

                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_auction", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)
                            time.sleep(0.3)
                    QTest.qWait(500)

            QTest.qWait(1000)

    except Exception as e:
        print(e)


def auction_sell(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open, confirm_all

    try:
        print("auction_sell")

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 10:
                is_action = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 30, 200, 90, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("auction", imgs_)
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\sell_status_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 990, 80, 1040, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:


                    for i in range(10):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\recall_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(500, 140, 610, 440, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("recall_btn", imgs_)
                            click_pos_2(510, 1015, cla)
                            time.sleep(0.5)
                        else:
                            is_action = True
                            # 팔아버리자
                            auction_sell_item(cla)
                            break
                        QTest.qWait(500)




                else:
                    click_pos_2(170, 95, cla)
                    time.sleep(0.5)


            else:
                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(30, 30, 200, 90, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 30, 960, 1040, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_auction", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)
                            time.sleep(0.3)
                    QTest.qWait(500)
            QTest.qWait(1000)

    except Exception as e:
        print(e)


def auction_sell_item(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_for, click_pos_reg, imgs_set_, int_put_, change_number
    from action import menu_open, confirm_all

    my_item = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\list"
    file_list = os.listdir(my_item)

    try:
        print("auction_sell_item")

        # y값 정하기
        y_reg = 1000
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\e.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 130, 940, 1000, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            y_reg = imgs_.y

        # 아이템 리스트 정리
        for i in range(len(file_list)):
            result_file_list = file_list[i].split(".")
            read_data = result_file_list[0]
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\list\\" + str(read_data) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 130, 940, y_reg, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_x = imgs_.x
                click_y = imgs_.y

                result_full = auction_sell_item_start(cla, click_x, click_y)
                if result_full == True:
                    break
                QTest.qWait(1000)



    except Exception as e:
        print(e)

def auction_sell_item_start(cla, click_x, click_y):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action import menu_open, confirm_all, cancle_all

    try:
        print("auction_sell_item_start", click_x, click_y)

        is_full = False

        is_action = False
        is_action_count = 0

        while is_action is False:
            is_action_count += 1
            if is_action_count > 10:
                is_action = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_information_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(400, 360, 550, 410, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("enroll_information_title", imgs_)
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\ten.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(480, 610, 540, 640, cla, img, 0.99)
                if imgs_ is not None and imgs_ != False:
                    print("ten", imgs_)
                    # 닫기

                    for i in range(5):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_information_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 360, 550, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_2(715, 385, cla)
                        else:
                            break
                        QTest.qWait(500)

                else:
                    print("가격 읽어오고 팔자")

                    for i in range(5):
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\clicked_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(355, 570, 480, 620, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("clicked_1", imgs_)
                            break
                        else:
                            click_pos_2(500, 600, cla)
                        QTest.qWait(500)

                    result_qun = auction_qun_num(cla, 605, 640)

                    print("==========================================================================")

                    result_low = auction_low_num(cla)

                    result_ = int(result_low * result_qun)
                    if result_ > 10:
                        print("==========================================================================")

                        sell_click(cla, result_)
                    else:
                        # 닫기

                        for i in range(5):
                            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_information_title.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(400, 360, 550, 410, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_2(715, 385, cla)
                            else:
                                break
                            QTest.qWait(500)
                is_action = True

            else:
                click_pos_reg(click_x, click_y, cla)
                time.sleep(0.2)
                click_pos_reg(click_x, click_y, cla)
                for i in range(10):
                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\can_not_enroll_item_notice.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 60, 640, 120, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("can_not_enroll_item_notice", imgs_)
                        is_action = True
                        break
                    time.sleep(0.1)

            QTest.qWait(1000)
        return is_full
    except Exception as e:
        print(e)


def auction_low_num(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, imgs_set_reg, in_number_check, int_put_, change_number

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:

        x_1 = 430 + plus
        x_2 = 535 + plus

        y_1 = 465
        y_2 = 490

        x_reg = 0
        end_reg = x_2

        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\dia_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_reg(360, 460, 535, 500, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            x_1 = imgs_.x
            x_reg = x_1


        is_point = False
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\point_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("point", imgs_)
            is_point = True
            x_reg = imgs_.x


        # 맨 앞 숫자 위치 파악하기
        print("맨 앞 숫자 위치 파악하기", x_reg)

        result_min = 0
        list_x = []
        for i in range(10):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("x_1", i, imgs_)
                list_x.append(imgs_.x)
                print("list_x", list_x)
                result_min = min(list_x)
        print("result_min", result_min)

        x_1 = result_min - 7
        x_2 = x_1 + 13

        print("################")
        print("x_1", x_1)
        print("x_2", x_2)
        print("################")



        # 소수점 이전
        num = False
        num_count = 9
        result_num = ""
        while num is False:
            # print("x_1...", x_1, num_count)
            # print("num_count...", num_count)
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\low_price_num\\" + str(
                num_count) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("is num...", str(num_count), imgs_)
                #
                if str(num_count) == "4":
                    x_1 = imgs_.x + 2  # - 1

                elif str(num_count) == "1":
                    x_1 = imgs_.x + 1

                else:
                    x_1 = imgs_.x

                x_2 = x_1 + 13

                if is_point == True:
                    if imgs_.x > x_reg:
                        num = True
                    else:
                        result_num += str(num_count)
                else:
                    result_num += str(num_count)
                # print("result_num...", result_num)
                num_count = 9
            else:
                num_count -= 1
                if num_count < 0:
                    num = True

        print("result_num", result_num)

        # 소수점 이후
        if is_point == True:

            x_1 = x_reg
            x_2 = x_1 + 10

            result_num += "."

            print("result_num(point)", result_num)

            num = False
            num_count = 9
            while num is False:
                # print("x_1...", x_1, num_count)
                # print("x_2...", x_2, num_count)
                # print("num_count...", num_count)
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\low_price_num\\" + str(
                    num_count) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    print("is num...", str(num_count), imgs_)
                    #
                    if str(num_count) == "4":
                        x_1 = imgs_.x + 2  # - 1

                    elif str(num_count) == "1":
                        x_1 = imgs_.x + 1

                    else:
                        x_1 = imgs_.x

                    x_2 = x_1 + 13

                    if is_point == True:
                        if imgs_.x > end_reg:
                            num = True
                        else:
                            result_num += str(num_count)
                    else:
                        result_num += str(num_count)
                    print("result_num...", result_num)
                    num_count = 9
                else:
                    num_count -= 1
                    if num_count < 0:
                        num = True
        print("result_num", result_num)
        result_num = float(result_num)
        print("result_num int", result_num)
        return result_num
    except Exception as e:
        print(e)


def auction_qun_num(cla, y_point_1, y_point_2):
    import numpy as np
    import cv2

    from function_game import imgs_set_, imgs_set_reg, in_number_check, int_put_, change_number

    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    try:



        x_1 = 575 + plus
        x_2 = 700 + plus

        # y_1 = 665
        # y_2 = 700

        y_1 = y_point_1
        y_2 = y_point_2

        end_reg = x_2

        is_point = False
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\point_rest.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
        if imgs_ is not None and imgs_ != False:
            print("point_rest", imgs_)
            is_point = True
            x_reg = imgs_.x


        # 맨 앞 숫자 위치 파악하기
        print("맨 앞 숫자 위치 파악하기", x_1)

        result_min = 0
        list_x = []
        for i in range(10):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("x_1", i, imgs_)
                list_x.append(imgs_.x)
                print("list_x", list_x)
                result_min = min(list_x)
        print("result_min", result_min)

        # 맨 앞 숫자 위치 파악하기
        print("맨 끝 숫자 위치 파악하기", x_2)

        result_max = 0
        list_x = []
        for i in range(10):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("x_1", i, imgs_)
                list_x.append(imgs_.x)
                print("list_x", list_x)
                result_max = max(list_x)
        print("result_max", result_max)

        x_1 = result_min - 7
        x_2 = x_1 + 19

        print("################")
        print("x_1", x_1)
        print("x_2", x_2)
        print("################")

        # 파악
        # 소수점 이전
        num = False
        num_count = 9
        result_num = ""
        while num is False:
            # print("x_1...", x_1, num_count)
            # print("num_count...", num_count)
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\qun_price_num\\" + str(
                num_count) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
            if imgs_ is not None and imgs_ != False:
                print("is num...", str(num_count), imgs_)
                #
                if str(num_count) == "4":
                    x_1 = imgs_.x + 2  # - 1

                elif str(num_count) == "1":
                    x_1 = imgs_.x + 1

                else:
                    x_1 = imgs_.x

                x_2 = x_1 + 19

                if is_point == True:
                    if imgs_.x > x_reg:
                        num = True
                    else:
                        result_num += str(num_count)
                else:
                    result_num += str(num_count)
                # print("result_num...", result_num)
                num_count = 9
            else:
                num_count -= 1
                if num_count < 0:
                    num = True

        print("result_num", result_num)


        # 천 단위 이후

        if is_point == True:

            x_1 = x_reg
            x_2 = x_1 + 15

            num = False
            num_count = 9
            while num is False:
                # print("x_1...", x_1, num_count)
                # print("num_count...", num_count)
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\qun_price_num\\" + str(
                    num_count) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_reg(x_1, y_1, x_2, y_2, cla, img, 0.95)
                if imgs_ is not None and imgs_ != False:
                    print("is num...", str(num_count), imgs_)
                    #
                    if str(num_count) == "4":
                        x_1 = imgs_.x + 2  # - 1

                    elif str(num_count) == "1":
                        x_1 = imgs_.x + 1

                    else:
                        x_1 = imgs_.x

                    x_2 = x_1 + 19

                    if imgs_.x > end_reg:
                        num = True
                    else:
                        result_num += str(num_count)
                    # print("result_num...", result_num)
                    num_count = 9
                else:
                    num_count -= 1
                    if num_count < 0:
                        num = True

            print("result_num", result_num)


        print("result_num", result_num)
        result_num = float(result_num)
        print("result_num int", result_num)

        return result_num
    except Exception as e:
        print(e)



def sell_click(cla, result_price):
    import numpy as np
    import cv2
    import os

    from function_game import click_pos_2, text_check_get_num, change_number_float, imgs_set_, click_pos_reg
    from action import confirm_all, cancle_all

    try:
        print("sell_click", result_price)

        for i in range(5):
            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\clicked_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(355, 600, 480, 650, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("clicked_1", imgs_)
                break
            else:
                click_pos_2(500, 625, cla)
            QTest.qWait(500)



        anymore_sell = False

        for i in range(5):



            result_price_str = str(result_price)
            for n in range(len(result_price_str)):

                # 기준값
                num_x = 580  # 50
                num_y = 435  # 35

                print(n + 1, result_price_str[n])
                if int(result_price_str[n]) == 2 or int(result_price_str[n]) == 5 or int(
                        result_price_str[n]) == 8 or int(result_price_str[n]) == 0:
                    num_x = 640
                elif int(result_price_str[n]) == 3 or int(result_price_str[n]) == 6 or int(
                        result_price_str[n]) == 9:
                    num_x = 700

                if int(result_price_str[n]) == 4 or int(result_price_str[n]) == 5 or int(
                        result_price_str[n]) == 6:
                    num_y = 475
                elif int(result_price_str[n]) == 7 or int(result_price_str[n]) == 8 or int(
                        result_price_str[n]) == 9:
                    num_y = 510
                elif int(result_price_str[n]) == 0:
                    num_y = 550
                click_pos_2(num_x, num_y, cla)
                time.sleep(0.3)

            # 클릭한거랑 계산된거랑 비교해서 같으면 확인
            QTest.qWait(200)
            result_many_ = auction_qun_num(cla, 605, 640)

            if result_price == result_many_:
                print("오케이!!!!!!!!", result_price, result_many_)
                for n in range(5):

                    full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_confirm_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(450, 410, 520, 460, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("enroll_confirm_title", imgs_)
                        confirm_all(cla)
                    else:
                        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_information_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(400, 360, 550, 410, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("enroll_information title", imgs_)
                            confirm_all(cla)
                        else:
                            break
                    QTest.qWait(500)
                break
            else:
                print("다시 누르자")
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\num_enroll_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 320, 530, 380, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("num_enroll_title", imgs_)
                    click_pos_2(395, 640, cla)

            QTest.qWait(500)


        # 마지막 확인
        for i in range(4):

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_confirm_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(450, 410, 520, 460, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("enroll_confirm_title", imgs_)
                confirm_all(cla)
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_information_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 360, 550, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("enroll_information title", imgs_)
                    confirm_all(cla)
                else:
                    break
            time.sleep(0.5)

        # 마지막 나가기
        for i in range(7):

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_confirm_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 310, 540, 360, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("enroll_confirm_title", imgs_)
                cancle_all(cla)
            else:
                full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\auction\\enroll_information_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(400, 360, 550, 410, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("enroll_information title", imgs_)
                    click_pos_2(540, 690, cla)
                else:
                    break
            time.sleep(0.5)

        return anymore_sell

    except Exception as e:
        print(e)
        return 0

