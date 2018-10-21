#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import matplotlib.pyplot as plt
import math
import sys

def rgb2hsi(rgb):
    # separar
    R,G,B= cv2.split(rgb)
    # normalizar
    R =R/255
    G =G/255
    B =B/255
    # cantidad de elementos
    x=R.shape[0]
    y=R.shape[1]
    # crear arrays
    r=np.empty([x,y])
    g=np.empty([x,y])
    b=np.empty([x,y])
    H=np.empty([x,y])
    S=np.empty([x,y])
    I=np.empty([x,y])

    # recorrer
    for i in range(0, x):
        for j in range(0,y):
            # calcular rgb
            divisor=R[i,j]+G[i,j]+B[i,j]
            I[i,j]=divisor/3.0
            if (divisor != 0.0):
                r[i,j]=R[i,j]/divisor
                g[i,j]=G[i,j]/divisor
                b[i,j]=B[i,j]/divisor
                
            # calcular RGB
            if (R[i,j]==G[i,j]) and (G[i,j]==B[i,j]):
                H[i,j]=0
                S[i,j]=0
            else:
                argum=(R[i,j]-G[i,j])*(R[i,j]-G[i,j])+(R[i,j]-B[i,j])*(G[i,j]-B[i,j])
                num=0.5*((R[i,j]-G[i,j]) + (R[i,j]-B[i,j]))
                w=num/math.sqrt(argum)
                if (w>1): w=1
                if (w<-1): w=-1
                    
                H[i,j]=math.acos(w)
                if H[i,j] < 0:
                    print('b')
                    break
                    
                if B[i,j] > G[i,j]:
                    H[i,j]=2*math.pi-H[i,j]
                
                if (r[i,j] <= g[i,j]) & (r[i,j] <= b[i,j]): 
                    S[i,j]=1-3*r[i,j]
                if (g[i,j] <= r[i,j]) & (g[i,j] <= b[i,j]): 
                    S[i,j]=1-3*g[i,j]
                if (b[i,j] <= r[i,j]) & (b[i,j] <= g[i,j]): 
                    S[i,j]=1-3*b[i,j]
                    
    H*=179
    S*=255
    I*=255
    hsi=cv2.merge([H,S,I])
    return hsi

def hsi2rgb(hsi):
    H,S,I = cv2.split(hsi)
    H=H/179
    S=S/255
    I=I/255
    x=H.shape[0]
    y=H.shape[1]
    R=np.empty([x,y])
    G=np.empty([x,y])
    B=np.empty([x,y])
    r=np.empty([x,y])
    g=np.empty([x,y])
    b=np.empty([x,y])

       
    for i in range(0, x):
        for j in range(0,y):
            if (S[i,j] >1): S[i,j]=1
            if (I[i,j] >1): I[i,j]=1
            if (S[i,j] ==0): 
                R[i,j]=I[i,j]
                G[i,j]=I[i,j]
                B[i,j]=I[i,j]
            else:
                ums=(1-S[i,j])/3
                if (H[i,j]>=0) and (H[i,j]<np.radians(120)):
                    b[i,j]=ums
                    r[i,j]= 1/3*(1+(S[i,j]*np.cos(H[i,j])/np.cos(np.radians(60)-H[i,j])))
                    g[i,j]=1-r[i,j]-b[i,j]
                elif (H[i,j]>=np.radians(120)) and (H[i,j]<np.radians(240)):
                    H[i,j]-=np.radians(120)
                    r[i,j]=ums
                    g[i,j]=1/3*(1+(S[i,j]*np.cos(H[i,j])/np.cos(np.radians(60)-H[i,j])))
                    b[i,j]=1-r[i,j]-g[i,j]
                elif (H[i,j]>=np.radians(240)) and (H[i,j]<np.radians(360)):
                    H[i,j]-=np.radians(240)
                    g[i,j]=ums
                    b[i,j]=1/3*(1+(S[i,j]*np.cos(H[i,j])/np.cos(np.radians(60)-H[i,j])))
                    r[i,j]=1-g[i,j]-b[i,j]
                else:
                    print("fuera de rango")
                    break
                if (r[i,j]<0): r[i,j]=0
                if (g[i,j]<0): g[i,j]=0
                if (b[i,j]<0): b[i,j]=0
                R[i,j]=3*I[i,j]*r[i,j]
                G[i,j]=3*I[i,j]*g[i,j]
                B[i,j]=3*I[i,j]*b[i,j]
                if (R[i,j]>1): R[i,j]=1
                if (G[i,j]>1): G[i,j]=1
                if (B[i,j]>1): B[i,j]=1 
    rgb=cv2.merge([R,G,B])*255
    return rgb.astype(np.uint8)

your_path=sys.argv[1]
#your_destiniy_path=sys.argv[2]

frame2 = cv2.imread(your_path)
hsv2= cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv2)
h=np.where((h>=103) & (h<=130),200,h)
nuevo_hsv=cv2.merge([h,s,v])
nuevo_rgb= cv2.cvtColor(nuevo_hsv, cv2.COLOR_HSV2RGB)
nuevo_bgr= cv2.cvtColor(nuevo_rgb, cv2.COLOR_RGB2BGR)


cv2.imwrite(your_path, nuevo_bgr)
