import serial
import sys

COM_PORT = "/dev/ttyACM0"
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)

try:
	while True:
		command = raw_input("Enter: ").lower()
		print "Input: ", command
except KeyboardInterrupt:
	ser.close()
	print "Exit!"