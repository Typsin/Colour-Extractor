import cv2
import numpy as np
import matplotlib.pyplot as plt

# load the image
image = cv2.imread('colour_test_img.png')
cv2.imshow('Orignal', image)
rgb_ver = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
hsv_ver = cv2.cvtColor(rgb_ver, cv2.COLOR_RGB2HSV)

Red_L = np.array([0, 150, 50])
Red_U = np.array([0, 255, 255])
mask = cv2.inRange(hsv_ver, Red_L, Red_U)
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('red', res)

GreenL = np.array([45, 150, 50])
GreenU = np.array([65, 255, 255])
mask = cv2.inRange(hsv_ver, GreenL, GreenU)
res = cv2.bitwise_and(rgb_ver, rgb_ver, mask=mask)
cv2.imshow('Green', res)

BlueL = np.array([95, 150, 0])
BlueU = np.array([125, 255, 255])
mask = cv2.inRange(hsv_ver, BlueL, BlueU)
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Blue', res)

YellowL = np.array([25,150, 50])
YellowU = np.array([35, 255, 255])
mask = cv2.inRange(hsv_ver, YellowL, YellowU)
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('yellow', res)

CyanL = np.array([85,150, 0])
CyanU = np.array([95, 255, 255])
mask = cv2.inRange(hsv_ver, CyanL, CyanU)
res = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('Cyan', res)

MenL = np.array([145,150, 0])
MenU = np.array([155, 255, 255])
mask = cv2.inRange(hsv_ver, MenL, MenU)
res = cv2.bitwise_and(rgb_ver, rgb_ver, mask=mask)
cv2.imshow('Magenta', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
