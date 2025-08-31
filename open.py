import cv2 as cv

img = cv.imread('cat.jpg')

cv.imshow('cat', img)

cv.waitKey(0)