import cv2

citra = cv2.imread('citrawarna/baboon.png',-1)
if not citra is None:
  cv2.imshow('gambar babon',citra)
  cv2.waitKey(0)