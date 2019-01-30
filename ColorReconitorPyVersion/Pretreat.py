'''
Author: Alex Beng
Date: 2019.01.29->
'''

# 采样 rect 顺序
# rect_0---rect_1---rect_2
# |          |        |
# |          |        |
# rect_3---rect_4---rect_5
# |          |        |
# |          |        |
# rect_6---rect_7---rect_8

import numpy as np
import cv2
import configparser



class Pretreat:
    def __init__(self, raw_four_images, config):
        self.raw_four_images = raw_four_images  # raw images
        self.SetParams(config)      # get points from config objuect
        return 
    
    def CutImage(self):
        # do 透视变换
        # self.perspectived_imgs = []
        # for i in range()
        # self.perspectived_ul = cv2.warpPerspective(self.raw_four_images[0], self.trans_mat_ul, (self.perspectived_widht, self.perspectived_widht))
        # self.perspectived_ur = cv2.warpPerspective(self.raw_four_images[0], self.trans_mat_ur, (self.perspectived_widht, self.perspectived_widht))
        # self.perspectived_dl = cv2.warpPerspective(self.raw_four_images[1], self.trans_mat_dl, (self.perspectived_widht, self.perspectived_widht))
        # self.perspectived_dr = cv2.warpPerspective(self.raw_four_images[1], self.trans_mat_dr, (self.perspectived_widht, self.perspectived_widht))
        # self.perspectived_truned_ur = cv2.warpPerspective(self.raw_four_images[2], self.trans_mat_ur, (self.perspectived_widht, self.perspectived_widht))
        # self.perspectived_truned_dl = cv2.warpPerspective(self.raw_four_images[3], self.trans_mat_dl, (self.perspectived_widht, self.perspectived_widht))
        return 
    
    def GetSampleRectAvg(self):
        # sum the scalar and get avg
        self.sample_rects = []
        for i in range(9):
            row_idx = i/3
            col_idx = i%3

        # return them
        return 

    # params related
    # store & read can be done by the module :-)
    def SetParams(self, params):
        # set the trans'matrix
        self.trans_mats = []
        for i in range(4):
            self.trans_mats.append(np.eye(3))
            section = 'tran_mat_' + str(i)
            for j in range(9):
                key = 'element_' + str(j)
                self.trans_mats[i][int(j/3)][int(j%3)] = float(params[section][key])

        # set perspectived size
        self.perspectived_widht  = params['perspectived_size']['width']
        return 

if __name__ == "__main__":
    # test set params
    config = configparser.ConfigParser()
    config.read("../BackupSource/pretreat_config.ini")
    print(config.sections())
    _ = 0
    t_233 = Pretreat(_, config)
    print(t_233.trans_mats[0])
    print(t_233.trans_mats[1])
    print(t_233.trans_mats[2])
    print(t_233.trans_mats[3])
