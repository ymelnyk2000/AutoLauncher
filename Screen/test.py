from pynput.mouse import Button, Controller
import cv2
import numpy as np
import PIL
import time
from PIL import ImageGrab

def test():
    time.sleep(4)
    image = PIL.ImageGrab.grab()
    image.save('image.jpg')

    template = cv2.imread('cleanplot.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    pos_list = np.where(res > 0.67)

    for i in range(1, len(pos_list[0])):
        cv2.circle(img, (pos_list[1][i]+5, pos_list[0][i]+5), 4, (0, 255, 0), -1)
        cv2.imwrite("image1.jpg", img)

    print(pos_list)

def main():
    test()

if __name__ == "__main__":
    main()