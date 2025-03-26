import time
# import os
import sys

from PyQt5.QtTest import *
import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("_stop_please")
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\18\\18_close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 30, 960, 770, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("18_close_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(1)



    except Exception as e:
        print(e)
        return 0



