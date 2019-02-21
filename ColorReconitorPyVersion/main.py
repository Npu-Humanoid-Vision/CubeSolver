import cv2
import glob
import numpy as np
from Pretreat import *

if __name__ == "__main__":
    # test set params
    config = configparser.ConfigParser()
    config.read("../BackupSource/pretreat_config.ini")

    pic_path = "../BackupSource/*.jpg"
    pic_paths = [i for i in glob.glob(pic_path)]
    pics = []
    for i in pic_paths:
        img = cv2.imread(i)
        print(i)

        pics.append(img)

        cv2.imshow("233", img)
        cv2.waitKey(0)
    pp = Pretreat(pics, config)
    pp.CutImage()
    for i in pp.perspectived_imgs:
        cv2.imshow("233", i)
        cv2.waitKey()
    pp.GetSampleRectAvg()
    result = pp.sample_scalars
    for i in result:
        (b, g, r) = i
        # print("%f\t%f\t%f"%(b, g, r))