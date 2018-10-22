import cv2
import os
import sys

# Arguments
#dir_path = directorio donde se encuentran los frames
#ext = estencion de los frames
#output = nombre del archivo  ruta_de_archivo/"output.mp4"
#inicio= primer frame desde el que se reconstruye el video
#fin= ultimo frame hasta el que se construye el video




def rebuild(dir_path,ext,output,inicio,fin):
	try:
		mylistdir=os.listdir(dir_path)
		mylistdir.sort()
		mylistdir.pop(0)

		images = []
		for f in mylistdir:
		    if f.endswith(ext):
		        images.append(f)

# Determine the width and height from the first image
		image_path = os.path.join(dir_path, images[0])
		frame = cv2.imread(image_path)
		cv2.imshow('video',frame)
		height, width, channels = frame.shape

# Define the codec and create VideoWriter object
		fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use lower case
		out = cv2.VideoWriter(output, fourcc, 20.0, (width, height))

		for x in xrange(inicio,fin):

		    image_path = dir_path+images[x]
		    frame = cv2.imread(image_path)

		    out.write(frame) # Write out frame to video

		    cv2.imshow('video',frame)
		    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
		        break

# Release everything if job is finished
		out.release()
		cv2.destroyAllWindows()
		return True
	except:
		return False

your_origin_path=str(sys.argv[1])
your_extension=str(sys.argv[2])
your_destiny_path=str(sys.argv[3])
your_init=int(sys.argv[4])
your_end=int(sys.argv[5])


#your_origin_path="/home/stark28/python_projects/paralelo-proc-img/img-tafirol/"
#your_extension=".jpg"
#your_destiny_path="/home/stark28/python_projects/paralelo-proc-img/img-tafirol/output.mp4"
#your_init=1
#your_end=329


print(your_origin_path)
print(your_extension)
print(your_destiny_path)
print(your_init)
print(your_end)


rebuild(your_origin_path,your_extension,your_destiny_path,your_init,your_end)
