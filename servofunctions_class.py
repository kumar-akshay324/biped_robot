# Declaring a class for all the functions
import Adafruit_PCA9685

import time

pwm = Adafruit_PCA9685.PCA9685()
channel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

class jointfunctions():

	#All the functions that drive the joints                                '
	
# ------------------------------------------------------------------------

	# servo_channel = 2 for right leg 
	# servo_channel = 8 for left leg
 
	def knee_bending(self, servo_channel_k):

		if servo_channel_k == 2:
			print ("Right leg knee pitch movement")
		elif servo_channel_k == 8:
			print ("Left leg knee pitch movement")

	# servo_channel_h = 3 for right leg - PITCH
	# servo_channel_h = 9 for left leg - PITCH

	# servo_channel_h =  4 for right leg - ROLL
	# servo_channel_h =  10 for left leg - ROLL

	# servo_channel_h = 5 for right leg - YAW
	# servo_channel_h = 11 for left leg - YAW

	def hip_bending(self, servo_channel_h):

		if servo_channel_h == 3:
			print ('Right leg hip pitch movement')
		elif servo_channel_h == 9:
			print ('Left leg hip pitch movement')
		elif servo_channel_h == 4:
			print ('Right leg hip roll movement')
		elif servo_channel_h == 10:
			print ('Left leg hip roll movement'	)
		elif servo_channel_h == 5:
			print ('Right leg hip yaw movement')
		elif servo_channel_h == 11:
			print ('Left leg hip yaw movement')

	# servo_channel_a = 1 for right leg - PITCH
	# servo_channel_a = 7  for left leg - PITCH

	# servo_channel_a = 0 for right leg - ROLL
	# servo_channel_a = 6  for left leg - ROLL


	def ankle_bending(self, servo_channel_a):

		if servo_channel_a == 1:
			print (' Right leg ankle pitch movement')
		if servo_channel_a == 7:
			print (' Left leg ankle pitch movement')
		if servo_channel_a == 0:
			print (' Right leg ankle roll movement')
		if servo_channel_a == 6:
			print (' Left leg ankle roll movement')

#-------------------------------------------------------------------------
	# Functions for individual control of all the motors/joints

	# Controls functions for the knee joint -  2 PITCH

	def right_knee_pitch(self, angle_r_k_p, current_angle):

		pwm_start = current_angle * 4.722 + 250
		
		pwm_end = angle_r_k_p * 4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)

	def left_knee_pitch(self, angle_l_k_p, current_angle):

		pwm_start = current_angle * 4.722 + 250
		pwm_end = angle_l_k_p * 4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)


		return int(rang), int(pwm_start)


	# Controls functions for the hip joint -  2 PITCH, 2 ROLL and 2 YAW

	def right_hip_pitch(self, angle_r_h_p, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_r_h_p *4.722 + 250
		rang = abs((pwm_end - pwm_start))

		return int(rang), int(pwm_start)

	def left_hip_pitch(self, angle_l_h_p, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_l_h_p *4.722 + 250
		rang = abs((pwm_end - pwm_start))

		return int(rang), int(pwm_start)



	def right_hip_roll(self, angle_r_h_r, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_r_h_r *4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)



	def left_hip_roll(self, angle_l_h_r, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_l_h_r *4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)



	def right_hip_yaw(self, angle_r_h_y, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_r_h_y *4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)


	def left_hip_yaw(self, angle_l_h_y, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_l_h_y *4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)



	# Controls functions for the ankle joint -  2 PITCH and 2 ROLL

	def right_ankle_pitch(self, angle_r_a_p, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_r_a_p *4.722 + 250
		rang = abs((pwm_end - pwm_start))

		return int(rang), int(pwm_start)



	def left_ankle_pitch(self, angle_l_a_p, current_angle):
 
		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_l_a_p *4.722 + 250
		rang = abs((pwm_end - pwm_start))

		return int(rang), int(pwm_start)

	def right_ankle_roll(self, angle_r_a_r, current_angle):

		pwm_start = current_angle *4.722 + 250
		pwm_end = angle_r_a_r *4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)



	def left_ankle_roll(self, angle_l_a_r, current_angle):

		pwm_start = current_angle*4.722 + 250
		pwm_end = angle_l_a_r *4.722 + 250
		rang = abs((pwm_end - pwm_start)/2)

		return int(rang), int(pwm_start)




