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
        self.perspectived_imgs = []
        for i in range(4):# 后两张要特别处理
            if i < 2:
                t_idx = 0
            else:
                t_idx = 1
            self.perspectived_imgs.append(
                cv2.warpPerspective(self.raw_four_images[t_idx],
                                    self.trans_mats[i],
                                    (self.perspectived_width, self.perspectived_width)
                )
            )
        self.perspectived_imgs.append(
            cv2.warpPerspective(self.raw_four_images[2],
                                self.trans_mats[1],
                                (self.perspectived_width, self.perspectived_width)
            )
        )
        self.perspectived_imgs.append(
            cv2.warpPerspective(self.raw_four_images[3],
                                self.trans_mats[2],
                                (self.perspectived_width, self.perspectived_width)
            )
        )
        return 
    
    def GetSampleRectAvg(self):
        # sum the scalar and get avg
        self.sample_scalars = [] 
        for j in range(6):
            for i in range(9):
                t_sum = np.ndarray([3,], dtype='float64')
                rect_cols = 100*(i/3) + 40
                rect_rows = 100*(i%3) + 40
                for row_i in range(20):
                    for col_i in range(20):
                        t_sum += self.perspectived_imgs[j][rect_rows+row_i, rect_cols+col_i]
                t_sum /= 400
                self.sample_scalars.append(t_sum)
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
        self.perspectived_width = params['perspectived_size']['width']
        return 

if __name__ == "__main__":
    # test set params
    config = configparser.ConfigParser()
    config.read("../BackupSource/pretreat_config.ini")

    # import glob
    # pic_path = "D:\\AlexBeng\\CubeSolver\\BackupSource\\*.jpg"
    # pic_paths = [i for i in glob.glob(pic_path)]
    # pics = []
    # for i in pic_paths:
    #     pics.append(cv2.imread(i))
    _ = []
    t_233 = Pretreat(_, config)
    print(t_233.trans_mats[0])
    print(t_233.trans_mats[1])
    print(t_233.trans_mats[2])
    print(t_233.trans_mats[3])
    t_233.CutImage()
    for i in range(6):
        cv2.imshow("233", t_233.perspectived_imgs[i])
        cv2.waitKey()
