import cv2
import configparser
import numpy as np

# by using config[section][key] = value to change the value won't affect other params :-)
# tested by Alex Beng

if __name__ == "__main__":
    config = configparser.ConfigParser()

    # config["233"] = {'244': '1',
    #                  '255': '2'}
    # with open("../BackupSource/test.ini", "w") as r:
    #     config.write(r)
    

    # config.read("../BackupSource/test.ini")
    # config["233"]["244"] = '2'
    # print(config["233"]["255"])

    # with open("../BackupSource/test.ini", "w") as r:
    #     config.write(r)

    # test_np = np.array([[0, 1, 1], [2, 3, 3]], dtype="float64")
    # test_np[0][1] /= 2
    # print(test_np)

    img = cv2.imread("../BackupSource/1_UL.jpg")
    rows,cols,ch = img.shape

    pts1 = np.float32([[0,0],[cols,0],[0,rows],[cols,rows]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)
    print(M)

    dst = cv2.warpPerspective(img,M,(400,400))

    cv2.imshow("233", dst)
    cv2.waitKey()