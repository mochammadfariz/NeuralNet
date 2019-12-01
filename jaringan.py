import cv2

citra = cv2.imread('citrawarna/baboon.png')
hasil = citra.copy()

thick = 20
hitam = 0

jumBaris = hasil.shape[0]
jumKolom = hasil.shape[1]

# bingkai di atas
for baris in range(thick):
  for kolom in range(jumKolom):
    hasil [baris,kolom] = hitam

# bingkai di bawah
for baris in range(jumBaris-thick-1,jumBaris):
  for kolom in range(jumKolom):
    hasil[baris,kolom ] = hitam

#bingkai di kiri
for baris in range(thick,jumBaris-thick-1):
  for kolom in range(thick):
    hasil[baris,kolom] = hitam

#bingkai dikanan
for baris in range(thick,jumBaris-thick-1):
  for kolom in range(jumKolom-thick-1,jumKolom):
    hasil[baris,kolom]=hitam

cv2.imshow('gambar asal',citra)
cv2.imshow('gambar hasil',hasil)
cv2.waitKey(0)
cv2.destroyAllWindows()