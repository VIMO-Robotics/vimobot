#!/usr/bin/env python

import RPi.GPIO as GPIO
import Adafruit_PCA9685
import time
import rospy
from motor_control.msg import motor_pwm


class pwm_control(object):
	def __init__(self):
		GPIO.setmode(GPIO.BCM)
		self.A1_l = 4
		self.A2_l = 17
		GPIO.setup(self.A1_l, GPIO.OUT)
		GPIO.setup(self.A2_l, GPIO.OUT)

		self.pwm = Adafruit_PCA9685.PCA9685()
		self.pwm.set_pwm_freq(60)

		image_sub = rospy.Subscriber('/vimo_velocity_controller/pwm', motor_pwm, self.pwm_callback)

	def pwm_callback(self, pwm_msg):
		pwm_l = 4096 / 255 * pwm_msg.pwm_l
		pwm_r = 4096 / 255 * pwm_msg.pwm_r
		print "pwm_l: {}".format(pwm_l)
		if (pwm_l == 0):
			GPIO.output(self.A1_l, GPIO.LOW)
			GPIO.output(self.A2_l, GPIO.LOW)
		elif(pwm_l > 0):
			GPIO.output(self.A1_l, GPIO.HIGH)
			GPIO.output(self.A2_l, GPIO.LOW)
		elif(pwm_l < 0):
			pwm_l = -pwm_l
			GPIO.output(self.A1_l, GPIO.LOW)
			GPIO.output(self.A2_l, GPIO.HIGH)

		self.pwm.set_pwm(3, 0, 4096 / 255 * pwm_l)
		

	def onShutdown(self):
		self.pwm.set_pwm(3, 0, 0)
		rospy.loginfo("Shutdown.")

if __name__ == '__main__': 
	rospy.init_node('pwm_control',anonymous=False)
	pwm_control = pwm_control()
	rospy.on_shutdown(pwm_control.onShutdown)
	rospy.spin()
		
