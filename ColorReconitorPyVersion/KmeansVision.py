import cv2
import numpy as np
from sklearn.cluster import KMeans

class Img2Status:
    def __init__(self, scalars):
        self.scalars = scalars 
        return 
    def cluster(self):
        kmeans_cluster = KMeans(n_clusters=6)
        kmeans_cluster.fit(self.scalars)
        return kmeans_cluster.labels_

if __name__ == "__main__":
    num = 0
    cp = cv2.VideoCapture(num)
    cv2.namedWindow("233")
    while True:
        __, frame = cp.read()
        if __:
            cv2.imshow("233", frame)
            cv2.waitKey(20)
