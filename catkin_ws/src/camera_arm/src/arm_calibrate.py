#!/usr/bin/python
import serial
import sys
import os
import time

class CAMERA_ARM:
	def __init__(self):
		self.A_cali = 90
		self.B_cali = 90
		self.COM_PORT = "/dev/ttyACM0"
		self.BAUD_RATES = 9600
		self.file_path = "../config/camera_arm_config.txt"
		if os.path.isfile(self.file_path):
			self.init_param(self.file_path)
		else:
			print "# No calibration file!!!"
			print "# Write default parameters into calibration file."
			self.write_file(self.file_path)
		self.ser = serial.Serial(self.COM_PORT, self.BAUD_RATES)
		print "Initialize camera position..."
		time.sleep(3)
		self.move_motor(90, 90)
		time.sleep(1)
		print "Done!!!"
		self.action()

	def action(self):
		try:
			while True:
				a = raw_input("Enter A: ").lower()
				b = raw_input("Enter B: ").lower()
				self.move_motor(a, b)
		except KeyboardInterrupt:
			self.ser.close()
			print "Exit!"
		self.ser.close()

	def init_param(self, file_path):
		file = open(file_path, "r")
		cali_data = []
		for f in file:
			cali_data.append(f.split()[0])
		file.close()
		for data in cali_data:
			d = data.split(":")
			if len(d) != 2:	# wrong content
				continue
			key = d[0]
			value = d[1]
			if key == "A_cali":
				self.A_cali = int(value)
			elif key == "B_cali":
				self.B_cali = int(value)
			elif key == "COM_PORT":
				self.COM_PORT = value
			elif key == "BAUD_RATES":
				self.BAUD_RATES = int(value)

	def move_motor(self, a, b):
		a_pos = int(a) - (90 - self.A_cali)
		b_pos = int(b) - (90 - self.B_cali)
		command = "#a"+ str(a_pos) + "#b" + str(b_pos) + "&"
		self.ser.write(command+'\n')

	def calibrate(self, file_path):
		self.write_file(file_path)

	def write_file(self, file_path):
		file = open(file_path, "w")
		file.write("COM_PORT:" + str(self.COM_PORT) + '\n')
		file.write("BAUD_RATES:" + str(self.BAUD_RATES) + '\n')
		file.write("A_cali:" + str(self.A_cali) + '\n')
		file.write("B_cali:" + str(self.B_cali))
		file.close()

foo = CAMERA_ARM()