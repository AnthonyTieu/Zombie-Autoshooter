import numpy as np
from PIL import ImageGrab
import cv2
import time
import math
from pynput.mouse import Button, Controller

#Courtesy of glitchassassin and starbadger https://github.com/asweigart/pyautogui/issues/116
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

mouse = Controller()
last_time = time.time()
game_coordinates = [750, 375, 1150, 775] #[0, 0, 1920, 1080] #[350, 155, 1550, 1020] #x and y of top-left corner; x and y of bottom-left corner
target_colour = [255, 240, 224]#243 #[255, 240, 224] #[224, 240, 255]

while True:
    gameScreen = np.array(ImageGrab.grab(bbox=game_coordinates))
    gameScreen = cv2.cvtColor(gameScreen, cv2.COLOR_BGR2RGB)

    for y in range (0, 400, 10): #864, 20): #1079, 5):
        for x in range (0, 400, 10): #1199, 20): #1919, 5):
            channels_xy = gameScreen[y, x]
            if all(channels_xy == target_colour):#channels_xy == target_colour: #all(channels_xy == target_colour):
                mouse.position = (x + 750, y + 375)
                mouse.press(Button.left)
                mouse.release(Button.left)
                
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()
    
    cv2.imshow('window', gameScreen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
       cv2.destroyAllWindows()
       break


from pynput.mouse import Button, Controller
mouse = Controller()
gameScreen = cv2.imread('Autoshooter.png')
cv2.namedWindow('window', cv2.WINDOW_NORMAL)
cv2.resizeWindow('window', 1280, 720)
cv2.resizeWindow('window', 800, 580)

    

