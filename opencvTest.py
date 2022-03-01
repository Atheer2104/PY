

import numpy as np
import cv2

# using our defualt camera to take photos
cap = cv2.VideoCapture(0)

while (True):
    # reading every frame
    ret, frame = cap.read()

    cv2.imshow("frame", frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
