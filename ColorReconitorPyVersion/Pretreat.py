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
        # resize
        return 
    
    def GetSampleRectAvg(self):
        # sum the scalar and get avg
        # return them
        return 

    # params related
    # store & read can be done by the module :-)
    def SetParams(self, params):
        # set the trans'matrix
        self.trans_mat_ul = np.eye(3)
        self.trans_mat_ur = np.eye(3)
        self.trans_mat_dl = np.eye(3)
        self.trans_mat_dr = np.eye(3)
        for i in range(9):
            self.trans_mat_ul[i/3][i%3] = params['trans_mat_ul']['element_%d'%i]
            self.trans_mat_ur[i/3][i%3] = params['trans_mat_ur']['element_%d'%i]
            self.trans_mat_dl[i/3][i%3] = params['trans_mat_dl']['element_%d'%i]
            self.trans_mat_dr[i/3][i%3] = params['trans_mat_dr']['element_%d'%i]
        # set the rects
        self.rect_0_point_0 = (params['rect_0']['x_0'], params['rect_0']['y_0'])
        self.rect_0_point_1 = (params['rect_0']['x_1'], params['rect_0']['y_1'])

        self.rect_1_point_0 = (params['rect_1']['x_0'], params['rect_1']['y_0'])
        self.rect_1_point_1 = (params['rect_1']['x_1'], params['rect_1']['y_1'])

        self.rect_2_point_0 = (params['rect_2']['x_0'], params['rect_2']['y_0'])
        self.rect_2_point_1 = (params['rect_2']['x_1'], params['rect_2']['y_1'])

        self.rect_3_point_0 = (params['rect_3']['x_0'], params['rect_3']['y_0'])
        self.rect_3_point_1 = (params['rect_3']['x_1'], params['rect_3']['y_1'])

        self.rect_4_point_0 = (params['rect_4']['x_0'], params['rect_4']['y_0'])
        self.rect_4_point_1 = (params['rect_4']['x_1'], params['rect_4']['y_1'])

        self.rect_5_point_0 = (params['rect_5']['x_0'], params['rect_5']['y_0'])
        self.rect_5_point_1 = (params['rect_5']['x_1'], params['rect_5']['y_1'])

        self.rect_6_point_0 = (params['rect_6']['x_0'], params['rect_6']['y_0'])
        self.rect_6_point_1 = (params['rect_6']['x_1'], params['rect_6']['y_1'])

        self.rect_7_point_0 = (params['rect_7']['x_0'], params['rect_7']['y_0'])
        self.rect_7_point_1 = (params['rect_7']['x_1'], params['rect_7']['y_1'])

        self.rect_8_point_0 = (params['rect_8']['x_0'], params['rect_8']['y_0'])
        self.rect_8_point_1 = (params['rect_8']['x_1'], params['rect_8']['y_1'])
        return 

if __name__ == "__main__":
     