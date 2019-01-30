import cv2
import glob
import numpy as np

if __name__ == "__main__":

    pic_path = "D:\\AlexBeng\\CubeSolver\\BackupSource\\*.jpg"
    pic_paths = [i for i in glob.glob(pic_path)]
    cv2.namedWindow("233")
    t = np.ndarray([3,])
    for i in pic_paths:
        img = cv2.imread(i)
        # print(type(img[0, 0]))
        # print(img[0,0].shape)
        t += img[0, 0]
        print(img[0,0])
        roi = img[0:100, 0:100]
        cv2.imshow("244", roi)
        print(np.sum(roi, axis=1))
        # print(t.shape)
        cv2.imshow("233", img)
        cv2.waitKey()
    print(t)
    print(t/2)