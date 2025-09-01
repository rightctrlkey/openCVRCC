# photos

# import cv2 as cv

# img = cv.imread('cat.jpg')

# cv.imshow('cat', img)

# cv.waitKey(0)

# videos

import cv2 as cv

capture = cv.VideoCapture('cat.mp4')

while True:
  isTrue, frame = capture.read()
  cv.imshow('video', frame)

  if cv.waitKey(20) & 0xFF == ord('d'):
    break

capture.release()
cv.destroyAllWindows()

