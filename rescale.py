import cv2 as cv

def rescaleFrame(frame, scale=0.3):
  width = int(frame.shape[1] * scale)
  height = int(frame.shape[0] * scale)

  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#############  photo  #############

img = cv.imread('cat.jpg')
cv.imshow('cat', img)

resized_image = rescaleFrame(img)
cv.imshow('image', resized_image)

#############  video  #############

capture = cv.VideoCapture('cat.mp4')

while True:
  isTrue, frame = capture.read()

  frame_resized = rescaleFrame(frame)

  cv.imshow('video', frame)
  cv.imshow('video Resized', frame_resized)

  if cv.waitKey(20) & 0xFF == ord('d'):
    break

capture.release()
cv.destroyAllWindows()