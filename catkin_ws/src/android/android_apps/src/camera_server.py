import socket
import cv2
import base64
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(3,320) # width
capture.set(4,240) # height

UDP_IP = "192.168.50.93"
CLIENT_IP = "192.168.50.104"
#CLIENT_IP = "192.168.50.22"
UDP_PORT = 5002
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind((UDP_IP, UDP_PORT))


ret, frame = capture.read()

encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]

while ret:
	result, imgencode = cv2.imencode('.jpg', frame, encode_param)
	stringData = base64.b64encode(imgencode)
	# data = np.array(imgencode)
	# stringData = data.tostring()

	#s.sendto( str(len(stringData)).ljust(16), (CLIENT_IP, UDP_PORT));
	try:
		s.sendto( stringData, (CLIENT_IP, UDP_PORT) );
	except:
		print('--')
		continue

	ret, frame = capture.read()
	# decimg=cv2.imdecode(data,1)
	# cv2.imshow('SERVER2',decimg)
	# cv2.waitKey(30)

s.close()
# cv2.destroyAllWindows()