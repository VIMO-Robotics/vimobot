#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from std_srvs.srv import *
from vimo_msgs.srv import SetValue, SetValueResponse
from std_srvs.srv import Empty, EmptyResponse
import serial
import sys
import os
import time


class CAMERA_ARM:
	def __init__(self):
		self.node_name = rospy.get_name()
		self.A_cali = 90
		self.B_cali = 90
		self.A_position = 90
		self.B_position = 90
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
		self.move_motor(self.A_position, self.B_position)
		time.sleep(1)
		print "Done!!!"
		self.srv_set_A = rospy.Service("/set_motor_A", SetValue, self.cbSrvSetA)
		self.srv_set_B = rospy.Service("/set_motor_B", SetValue, self.cbSrvSetB)
		self.srv_save = rospy.Service("/save_motor_calibration", Empty, self.cbSrvSaveCalibration)
		self.sub_joy = rospy.Subscriber("/joy", Joy, self.cbJoy, queue_size=1)
		# self.action()

	def cbSrvSetA(self, req):
		self.A_cali = int(req.value)
		rospy.loginfo("[%s] Set motor A degree bias: %s" % (self.node_name, self.A_cali))
		self.move_motor(self.A_position, self.B_position)
		return SetValueResponse()

	def cbSrvSetB(self, req):
		self.B_cali = int(req.value)
		rospy.loginfo("[%s] Set motor B degree bias: %s" % (self.node_name, self.B_cali))
		self.move_motor(self.A_position, self.B_position)
		return SetValueResponse()

	def cbSrvSaveCalibration(self, req):
		self.write_file(self.file_path)
		return EmptyResponse()

	def cbJoy(self, msg):
		if msg.axes[7] == 1:
			self.A_position = self.A_position + 5
		elif msg.axes[7] == -1:
			self.A_position = self.A_position - 5
		elif msg.axes[6] == 1:
			self.B_position = self.B_position + 5
		elif msg.axes[6] == -1:
			self.B_position = self.B_position - 5
		else:
			return
		print(self.A_position, self.B_position)
		self.move_motor(self.A_position, self.B_position)
		time.sleep(0.3)

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

if __name__ == "__main__":
	rospy.init_node("camera_arm", anonymous = False)
	foo = CAMERA_ARM()
	rospy.spin()