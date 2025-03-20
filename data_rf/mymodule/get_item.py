import sys
import os
import time
import requests

import variable as v_
from PyQt5.QtTest import *
sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):
    import numpy as np
    import cv2
    import pyautogui
    import random

    from function_game import macro_out
    from massenger import line_to_me

    try:
        print("get_item_start")
        full_path = "c:\\my_games\\rf_o_n\\data_rf\\imgs\\game_check\\fix_notice_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(330, 500, 440, 540, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("fix_notice_1", imgs_)
            why = "점검 중...."
            line_to_me(cla, why)
            macro_out(cla)

    except Exception as e:
        print(e)
