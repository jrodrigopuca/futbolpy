# coding: utf-8
import cv2
import numpy as np
import sys

#defino el video
your_path=sys.argv[1]
your_destiniy_path=sys.argv[2]
vidcap = cv2.VideoCapture(your_path)

#calculo la cantidad de frames
total_frames = str(int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT)))
#los nombres de las imagenes deben tener las misma cantidad de caracteres ej 000.jpg, 001.jpg, 025.jpg, 712.jpg
length= len(total_frames)
nombre=""
success,image = vidcap.read()
count = 1

try:
    while success:
        nombre=str(count)
#se la el formato al nombre
        #while (len(nombre) != length):
        #    nombre="0"+nombre
#Se le defina la ruta completa :v
        cv2.imwrite(your_destiniy_path+nombre+".jpg", image)
        success,image = vidcap.read()
        count += 1
    print(0)
except ValueError:
    print(-1)
