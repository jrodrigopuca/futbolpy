# futbolpy
código para detectar las transiciones de cámaras en partidos de fútbol

## distancia.ipynb 
prueba de los algoritmos de distancia  (simple y original) aplicado a dos arrays simples que "simulan" tener los valores del canal H.

## video-distancia
obtener la distancia de dos frames del video (frame 1,101). 

## video-frame
uso: para obtener los datos de promedio/varianza de los canales H/V (además guarda las imagenes)

## video-gris
uso: para obtener los datos de promedio/varianza de para el gris de cada frame

## video-histograma
obtener el histograma de un video (usando numpy)

## video-while 
obtener las distancias para cada par de frames

## video-modular
resuelto todo con forma modular:
- capturar frames
- calcular distancias
- usar filtro pasa-altos 
- crear videos por cada transición