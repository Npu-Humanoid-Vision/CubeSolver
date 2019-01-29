import cv2
import glob
import numpy

if __name__ == "__main__":

    pic_path = "D:\\AlexBeng\\CubeSolver\\BackupSource\\*"
    pic_paths = [i for i in glob.glob(pic_path)]
    cv2.namedWindow("233")
    for i in pic_paths:
        print(i)
        img = cv2.imread(i)
        print(img.shape)
        cv2.imshow("233", img)
        cv2.waitKey()