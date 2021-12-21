import numpy as np
import pyautogui
import imutils
import cv2
import time

def generate():
    image = pyautogui.screenshot(region=(0,0, 1920, 1080))


    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    #cv2.imshow("Screenshot", imutils.resize(image, width=600)) #показ фото

    cv2.imwrite("pic.png", image) #сохранение фото

    img = cv2.imread('pic.png')
     
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
     
     
    #Red color rangle  169, 100, 100 , 189, 255, 255
     
     
    lower_range = np.array([110,50,50])
    upper_range = np.array([130,255,255])
     
    mask = cv2.inRange(hsv, lower_range, upper_range)
     
    #cv2.imshow('image', img)
    cv2.imshow('mask', mask)

    #pyautogui.press('esc')
    cv2.waitKey(10)
    
 
    #if key == 27:#if ESC is pressed, exit loop
        #cv2.destroyAllWindows()
       # time.sleep(2)

while True:
    generate()


