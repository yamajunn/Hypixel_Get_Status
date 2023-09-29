import cv2
import numpy as np

def osero():
    height = 97
    width = height
    blank = np.zeros((height, width, 3))
    for i in range(width):
        blank[i] = [40, 80, 40]
        for j in range(1):
            blank[i][j] = [0,0,0]
            blank[i][j+12] = [0,0,0]
            blank[i][j+24] = [0,0,0]
            blank[i][j+36] = [0,0,0]
            blank[i][j+48] = [0,0,0]
            blank[i][j+60] = [0,0,0]
            blank[i][j+72] = [0,0,0]
            blank[i][j+84] = [0,0,0]
            blank[i][j+96] = [0,0,0]
    cv2.imwrite('osero.png',blank)
osero()