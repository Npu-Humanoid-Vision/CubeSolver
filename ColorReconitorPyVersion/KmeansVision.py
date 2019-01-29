import cv2
import numpy

class Img2Status:
    def __init__(self, images, up_anchor_points, down_anchor_points):
        self.images             = images
        self.up_anchor_points   = up_anchor_points
        self.down_anchor_points = down_anchor_points
        return 
    def seg_image(image)

if __name__ == "__main__":
    num = 0
    cp = cv2.VideoCapture(num)
    cv2.namedWindow("233")
    while True:
        __, frame = cp.read()
        if __:
            cv2.imshow("233", frame)
            cv2.waitKey(20)
