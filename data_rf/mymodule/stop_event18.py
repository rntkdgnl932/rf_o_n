import time
# import os
import sys

from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, macro_out
    from massenger import line_to_me

    try:
        print("_stop_please")

        event_18 = False
        event_18_count = 0

        while event_18 is False:
            event_18_count += 1
            if event_18_count > 100:
                why = "event_18에서 오류인듯"
                line_to_me(cla, why)
                macro_out(cla)

            event_18 = True

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\18\\anymore_today_look_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 1040, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("anymore_today_look_btn", imgs_)
                event_18 = False
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\18\\18_close_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 30, 960, 770, cla, img, 0.7)
            if imgs_ is not None and imgs_ != False:
                print("18_close_1", imgs_)
                event_18 = False
                click_pos_reg(imgs_.x, imgs_.y, cla)
                time.sleep(0.5)

            time.sleep(1)



    except Exception as e:
        print(e)
        return 0



