from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (340, 376)
    dinosaur = (172, 420)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')

def imageGrab():
    box = (223, 418, 256, 450)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def playGame():
    restartGame()
    while True:
        if imageGrab() != 1303:
            pressSpace()
            print('Jump...Jump...')
            time.sleep(0.2)
        print('Run... ')

playGame()

