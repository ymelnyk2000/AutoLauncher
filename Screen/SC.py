from pynput.mouse import Button, Controller
import cv2
import numpy as np
import PIL
import time
from PIL import ImageGrab

def EnlargeScreen():
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('fs.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

    pos_list = np.where(res > 0.9)

    mouse = Controller()

    mouse.position = (pos_list[1][0], pos_list[0][0])

    mouse.click(Button.left)

def ZoomOut():
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('zoom.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)

    pos_list = np.where(res > 0.9)

    mouse = Controller()

    mouse.position = (pos_list[1][0], pos_list[0][0])

    mouse.click(Button.left)
    time.sleep(1)
    mouse.click(Button.left)
    time.sleep(1)
    mouse.click(Button.left)

def ClickOnBrigade():
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('br.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos_list = np.where(res > 0.9)

    mouse = Controller()
    mouse.position = (pos_list[1][0], pos_list[0][0])
    time.sleep(2)
    mouse.click(Button.left)

def GatherCrops():
    ClickOnBrigade()
    time.sleep(1)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('crops.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos_list = np.where(res > 0.9)

    mouse = Controller()
    mouse.position = (pos_list[1][0], pos_list[0][0])
    time.sleep(1)
    mouse.click(Button.left)

def Dig():
    ClickOnBrigade()
    time.sleep(1)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('dig.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos_list = np.where(res > 0.9)

    mouse = Controller()
    mouse.position = (pos_list[1][0], pos_list[0][0])
    time.sleep(1)
    mouse.click(Button.left)

def Dirt():
    time.sleep(2)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('dirt.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos_list = np.where(res > 0.7)

    for i in range(1, len(pos_list[0])):
        cv2.circle(img, (pos_list[1][i], pos_list[0][i]), 4, (0, 255, 0), -1)
        cv2.imwrite("image1.jpg", img)

    if(len(pos_list) > 2):
        return True
    else:
        return False

def PageThree():
    time.sleep(2)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('three.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    pos_list = np.where(res > 0.9)
    mouse = Controller()

    mouse.position = (pos_list[1][0], pos_list[0][0])
    mouse.click(Button.left)

def CheckPage(name):
    time.sleep(2)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    pos_list = np.where(res > 0.9)
    print(len(pos_list[0]))
    if(len(pos_list[0]) > 0):
        return True
    else:
        return False

def PickGarlic():
    ClickOnBrigade()
    time.sleep(1)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('plant.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    pos_list = np.where(res > 0.9)

    mouse = Controller()

    mouse.position = (pos_list[1][0], pos_list[0][0])
    time.sleep(1)
    mouse.click(Button.left)

    if(not CheckPage('already3.png')):
        PageThree()

    time.sleep(1)

    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('garlic.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    pos_list = np.where(res > 0.9)

    mouse.position = (pos_list[1][0], pos_list[0][0])
    mouse.move(0, 195)
    mouse.click(Button.left)


def PlantGarlic():
    if(Dirt()):
        Dig()
    time.sleep(2)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    time.sleep(2)
  #  PickGarlic()
    time.sleep(2)

    template = cv2.imread('cleanplot.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos_list = np.where(res > 0.67)

    mouse = Controller()

    for i in range(1, len(pos_list[0])):
        time.sleep(0.1)
        mouse.position = (pos_list[1][i]+5, pos_list[0][i]+5)
        time.sleep(0.1)
        mouse.click(Button.left)


def main():
    time.sleep(2)
    EnlargeScreen()
    time.sleep(2)
    ZoomOut()
    time.sleep(2)
    PlantGarlic()

if __name__ == "__main__":
    main()