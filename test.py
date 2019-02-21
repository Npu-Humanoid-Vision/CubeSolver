import cv2

cp = cv2.VideoCapture(0)

while True:
    _, frame = cp.read()
    cv2.imshow("test", frame)
    key = cv2.waitKey(20)
    if key == 27:
        break

cp.release()
cv2.destoryAllWindows()