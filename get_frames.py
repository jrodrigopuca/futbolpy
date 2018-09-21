# coding: utf-8


import cv2
import numpy as np

#defino el video
your_path=""
vidcap = cv2.VideoCapture(your_path)

#calculo la cantidad de frames
total_frames = str(int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
#los nombres de las imagenes deben tener las misma cantidad de caracteres ej 000.jpg, 001.jpg, 025.jpg, 712.jpg
length= len(total_frames)
nombre=""
success,image = vidcap.read()
count = 1

while success:
  nombre=str(count)
#se la el formato al nombre
  while (len(nombre) != length):
    nombre="0"+nombre
#Se le defina la ruta completa :v
  cv2.imwrite("/home/stark28/Imágenes/frames/"+nombre+".jpg", image)
  success,image = vidcap.read()
  count += 1
print(length)
