from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

replayBtn = (340, 420)
dinosaur = (172, 420)
box = (230, 418, 256, 450)


def playGame():
    pyautogui.click(replayBtn)
    while True:
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        if a.sum() != 1079:
            pyautogui.keyDown('space')
            time.sleep(0.2)


playGame()