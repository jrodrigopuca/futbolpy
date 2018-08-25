
# coding: utf-8

# In[51]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

video_path = "360.mp4"
p_frame_thresh = 300000 # You may need to adjust this threshold

cap = cv2.VideoCapture(video_path)
# Read the first frame.
ret, prev_frame = cap.read()
alto,ancho,canales=prev_frame.shape

def bata(a, b):
    """ Bhattacharyya distance between distributions (lists of floats). """
    if not len(a) == len(b):
        raise ValueError("a and b must be of the same size")
    return -math.log(sum((math.sqrt(u * w) for u, w in zip(a, b))))

i=0
while ret:
    ret, curr_frame = cap.read()


    if ret:
        diff = cv2.absdiff(curr_frame, prev_frame)
        non_zero_count = np.count_nonzero(diff)
        if non_zero_count > p_frame_thresh:
            i=i+1
            #vector=np.asarray([])
            if i<300:
                #cv2.imwrite(str(i)+".jpg",curr_frame)
                
                
               
                gris_c=cv2.cvtColor(curr_frame,cv2.COLOR_BGR2HSV)
                gris_p=cv2.cvtColor(prev_frame,cv2.COLOR_BGR2HSV)
                
                for j in range(alto):
                    for k in range(ancho):
                        h,s,v=curr_frame[j,k]
                        print (h)
                
                #x = bata(gris_c[0],gris_p[0])
                #print(x)
                
                
                #elVar=np.var(curr_frame)
                #print(elVar)
                
                elPromedio=np.average(gris)
                print(elPromedio)
                
                #hist, bins = np.histogram(curr_frame,bins=256)
                #plt.plot(bins[:-1],hist,c='blue')
            #plt.plot(vector[::1],np.linespace(0,len(vector)))
        prev_frame = curr_frame

