import cv2
import numpy as np

def status_image():
    height = 800
    width = (height // 20) * 17
    blank = np.zeros((height, width, 3))
    blank += 50

    line_height = height // 6
    line_width = width // 3

    for i in range(width):
        for j in range(5):
            blank[0+j][i] = [200,200,200]
            blank[height-1-j][i] = [200,200,200]
            blank[line_height*2-j][i] = [200,200,200]
            blank[line_height*3-j][i] = [200,200,200]
            blank[line_height*4-j][i] = [200,200,200]
            blank[line_height*5-j][i] = [200,200,200]

    for i in range(height):
        for j in range(5):
            blank[i][0+j] = [200,200,200]
            blank[i][width-1-j] = [200,200,200]
            if i > line_height*2:
                blank[i][line_width-2+j] = [200,200,200]
                blank[i][line_width*2-2+j] = [200,200,200]

    cv2.putText(blank, "Level :", (line_width,line_height+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (200,200,200), thickness=2)

    cv2.putText(blank, "Coins :", (line_width*2+20,50), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)
    cv2.putText(blank, "Loot Chests :", (line_width*2+20,80), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)
    cv2.putText(blank, "Iron :", (line_width*2+20,110), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)
    cv2.putText(blank, "Gold :", (line_width*2+20,140), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)
    cv2.putText(blank, "Diamonds :", (line_width*2+20,170), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)
    cv2.putText(blank, "Emeralds :", (line_width*2+20,200), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)
    cv2.putText(blank, "Winstreak :", (line_width*2+20,230), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.6, color = (200,200,200), thickness=2)

    cv2.putText(blank, "Wins", (line_width//2-35,line_height*2+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,200,0), thickness=2)
    cv2.putText(blank, "Final Kills", (line_width//2-70,line_height*3+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,200,0), thickness=2)
    cv2.putText(blank, "Kills", (line_width//2-35,line_height*4+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,200,0), thickness=2)
    cv2.putText(blank, "Beds Broken", (line_width//2-98,line_height*5+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,200,0), thickness=2)

    cv2.putText(blank, "Losses", (line_width*2-165,line_height*2+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,0,200), thickness=2)
    cv2.putText(blank, "Final Deaths", (line_width*2-208,line_height*3+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,0,200), thickness=2)
    cv2.putText(blank, "Deaths", (line_width*2-165,line_height*4+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,0,200), thickness=2)
    cv2.putText(blank, "Beds Lost", (line_width*2-190,line_height*5+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,0,200), thickness=2)

    cv2.putText(blank, "WLR", (line_width*3-150,line_height*2+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,150,200), thickness=2)
    cv2.putText(blank, "FKDR", (line_width*3-155,line_height*3+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,150,200), thickness=2)
    cv2.putText(blank, "KDR", (line_width*3-150,line_height*4+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,150,200), thickness=2)
    cv2.putText(blank, "BBLR", (line_width*3-155,line_height*5+30), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1.0, color = (0,150,200), thickness=2)

    
    cv2.imwrite('blank.png',blank)
    # return blank
status_image()