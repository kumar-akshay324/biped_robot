# Declaring a class for all the functions

class jointfunctions:
	
	'All the functions that drive the joints                                '
	
	# servo_channel = 2 for right leg 
	# servo_channel = 8 for left leg 

# ------------------------------------------------------------------------

	def knee_bending(self, servo_channel_k):
		
		if self.servo_channel_k == 2:
			print 'Right leg knee pitch movement'
		elif self.servo_channel_k == 8: 
			print 'Left leg knee pitch movement'

	# servo_channel_h = 3 for right leg - PITCH 
	# servo_channel_h = 9 for left leg - PITCH

	# servo_channel_h =  4 for right leg - ROLL 
	# servo_channel_h =  10 for left leg - ROLL

	# servo_channel_h = 5 for right leg - YAW 
	# servo_channel_h = 11 for left leg - YAW

	def hip_bending(self, servo_channel_h):
		
		if self.servo_channel_h == 3:
			print 'Right leg hip pitch movement'
		elif self.servo_channel_h == 9:
			print 'Left leg hip pitch movement'	
		elif self.servo_channel_h == 4:
			print 'Right leg hip roll movement'	
		elif self.servo_channel_h == 10:
			print 'Left leg hip roll movement'	
		elif self.servo_channel_h == 5:
			print 'Right leg hip yaw movement'	
		elif self.servo_channel_h == 11:
			print 'Left leg hip yaw movement'	

	# servo_channel_a = 1 for right leg - PITCH
	# servo_channel_a = 7  for left leg - PITCH

	# servo_channel_a = 0 for right leg - ROLL
	# servo_channel_a = 6  for left leg - ROLL


	def ankle_bending(self, servo_channel_a):
		
		if self.servo_channel_a == 1:
			print ' Right leg ankle pitch movement'
		if self.servo_channel_a == 7:
			print ' Left leg ankle pitch movement'
		if self.servo_channel_a == 0:
			print ' Right leg ankle roll movement'
		if self.servo_channel_a == 6:
			print ' Left leg ankle roll movement'

#-------------------------------------------------------------------------
	# Functions for individual control of all the motors/joints

	# Controls functions for the knee joint -  2 PITCH 

	def right_knee_pitch(self, angle_r_k_p):
		
		pwm_start = current_angle[2] * 2.5 + 150 
		pwm_end = self.angle_r_k_p * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_r_k_p >= current_angle[2]:
			rate = 2 
				
		elif self.angle_r_k_p < current_angle[2]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[2], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[2] = self.angle_r_k_p	

	def left_knee_pitch(self, angle_l_k_p):
		
		pwm_start = current_angle[8] * 2.5 + 150 
		pwm_end = self.angle_l_k_p * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_l_k_p >= current_angle[8]:
			rate = 2 
				
		elif self.angle_l_k_p < current_angle[8]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[8], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[8] = self.angle_l_k_p	
		

	# Controls functions for the hip joint -  2 PITCH, 2 ROLL and 2 YAW 

	def right_hip_pitch(self, angle_r_h_p):
		
		pwm_start = current_angle[3] * 2.5 + 150 
		pwm_end = self.angle_r_h_p * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_r_h_p >= current_angle[3]:
			rate = 2 
				
		elif self.angle_r_h_p < current_angle[3]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[3], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[3] = self.angle_r_h_p	
		
	def left_hip_pitch(self, angle_l_h_p):
		
		pwm_start = current_angle[9] * 2.5 + 150 
		pwm_end = self.angle_l_h_p * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_l_h_p >= current_angle[9]:
			rate = 2 
				
		elif self.angle_l_h_p < current_angle[9]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[9], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[9] = self.angle_l_h_p	

	def right_hip_roll(self, angle_r_h_r):
		
		pwm_start = current_angle[4] * 2.5 + 150 
		pwm_end = self.angle_r_h_r * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_r_h_r >= current_angle[4]:
			rate = 2 
				
		elif self.angle_r_h_r < current_angle[4]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[4], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[4] = self.angle_r_h_r	
		
	def left_hip_roll(self, angle_l_h_r):
		
		pwm_start = current_angle[10] * 2.5 + 150 
		pwm_end = self.angle_l_h_r * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_l_h_r >= current_angle[10]:
			rate = 2 
				
		elif self.angle_l_h_r < current_angle[10]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[10], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[10] = self.angle_l_h_r	

	def right_hip_yaw(self, angle_r_h_y):
		
		pwm_start = current_angle[5] * 2.5 + 150 
		pwm_end = self.angle_r_h_y * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_r_h_y >= current_angle[5]:
			rate = 2 
				
		elif self.angle_r_h_y < current_angle[5]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[5], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[5] = self.angle_r_h_y	
		
	def left_hip_yaw(self, angle_l_h_y):
		
		pwm_start = current_angle[11] * 2.5 + 150 
		pwm_end = self.angle_l_h_y * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_l_h_y >= current_angle[11]:
			rate = 2 
				
		elif self.angle_l_h_y < current_angle[11]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[11], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[11] = self.angle_l_h_y	

	# Controls functions for the ankle joint -  2 PITCH and 2 ROLL  

	def right_ankle_pitch(self, angle_r_a_p):
		
		pwm_start = current_angle[1] * 2.5 + 150 
		pwm_end = self.angle_r_a_p * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_r_a_p >= current_angle[1]:
			rate = 2 
				
		elif self.angle_r_a_p < current_angle[1]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[1], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[1] = self.angle_r_a_p	
		
	def left_ankle_pitch(self, angle_l_a_p):
		
		pwm_start = current_angle[7] * 2.5 + 150 
		pwm_end = self.angle_l_a_p * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_l_a_p >= current_angle[7]:
			rate = 2 
				
		elif self.angle_l_a_p < current_angle[7]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[7], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[7] = self.angle_l_a_p	

	def right_ankle_roll(self, angle_r_a_r):
		
		pwm_start = current_angle[0] * 2.5 + 150 
		pwm_end = self.angle_r_a_r * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_r_a_r >= current_angle[0]:
			rate = 2 
				
		elif self.angle_r_a_r < current_angle[0]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[0], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[0] = self.angle_r_a_r	
		
	def left_ankle_roll(self, angle_l_a_r):
		
		pwm_start = current_angle[6] * 2.5 + 150 
		pwm_end = self.angle_l_a_r * 2.5 + 150
		rang = abs((pwm_end - pwm_start)/2) 
			
		if self.angle_l_a_r >= current_angle[6]:
			rate = 2 
				
		elif self.angle_l_a_r < current_angle[6]:
			rate = -2
			
		for i in range(rang):
				pwm.set_pwm(channel[6], 0, pwm_start + rate)
				pwm_start += rate
				time.sleep(0.020)
		current_angle[6] = self.angle_l_a_r	

