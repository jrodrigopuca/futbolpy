import cv2
import numpy as np 
import matplotlib.pyplot as plt
import math

# video con 152 frames en total
video= cv2.VideoCapture('360.mp4')
fps=video.get(cv2.CAP_PROP_FPS) # => 25 fps

size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))) # size => (640,360)

# codecs => http://www.fourcc.org/codecs.php
codec =cv2.VideoWriter_fourcc(*'XVID')
NuevoVideo= cv2.VideoWriter('nuevo.avi',codec,fps,size)

# recorriendo
success, frame = video.read()
i=0
while success:
	NuevoVideo.write(frame)
	i+=1
	nombre='img-original/'+str(i)+'.jpg'
	print(nombre)
	cv2.imwrite(nombre, frame)
	success, frame = video.read()

