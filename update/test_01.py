# Test code to actuate multiple motors from RPi using the PCA9685 pwm generator module

import RPi.GPIO as GPIO
import math
from servofunctions_class import *
import Adafruit_PCA9685
pwm = Adafruit_PCA9685.PCA9685()

motion = jointfunctions()

# Minimum and maximum pwm values
# servo_min = 250
# servo_max = 1100

frequency = 100

# Functions that this library uses

# pwm.set_pwm(channel, on, off) - 
# pwm.set_pwm_freq(frequency value) - Between 40 and 1000 for ideal operation of a servo 

pwm.set_pwm_freq(frequency)


init_stand_pwm_values = [700, 720, 270, 710, 700, 700, 700, 720, 1100, 620, 680, 650, 0, 0, 0, 0]
current_angle = [90, 90, 0, 90, 90, 90, 90, 90, 180, 90, 90, 90, 0, 0, 0, 0]

channel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def init_stand():
	for index in range(0,16):
		pwm.set_pwm(channel[index], 0, init_stand_pwm_values[index])
		time.sleep(0.020)
		
# Link lengths for the biped
# Lan = Ankle Length
# Lsh = Shin Length
# Lth = Thigh Length 
# Lab = Foot length division 1
# Laf = Foot length division 2
# Following the convention in the research paper by Huang

Lth = 106
Lsh = 86
Lan = 73
Lab = Laf = 50 




#----------------------------------------------------------------------

# Squats for the robot - Depending upon link lengths

def knee_motion(k,direction):
	knee_angle_rad = (math.pi * k)/180
	p_rad = math.pi/2 - math.atan((Lth - Lsh*math.cos(knee_angle_rad))/Lsh*math.sin(knee_angle_rad))
	p = p_rad * 180 /math.pi

	q_rad = math.pi/2 - (knee_angle_rad - (math.pi/2 - p_rad))
	q = q_rad * 180/math.pi
	#print(p)
	#print(q)

	# Angle(in radians) p for the thigh motor - PITCH
	# Angle(in radians) q or the ankle motor - PITCH 
	# central_angle(in radians) for the knee bend

	data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	rate = [ 0, 0, 0, 0, 0, 0]

	# data[0] to data[5] store the individual ranges
	# data[6] to data[11] store the individual pwm_start values

	data[0], data[6] = motion.right_knee_pitch(k, current_angle[2])
	data[1], data[7] = motion.left_knee_pitch(180-k, current_angle[8])
	data[2], data[8] = motion.right_hip_pitch(p, current_angle[3])
	data[3], data[9] = motion.left_hip_pitch(90+(90-p), current_angle[9])
	data[4], data[10] = motion.right_ankle_pitch(q, current_angle[1])
	data[5], data[11] = motion.left_ankle_pitch(q, current_angle[7])
	# Setting one arbitrary value to maximum and finding out the maximum range of the pwm values
	max_range = data[0]

	# Extract the range of pwm values to be travelled by each of the joints in order to reach the desired angles

	for i in range(0,6):
		if (data[i] >= max_range):
			max_range = data[i]

	# The loop shall run for the maximum range with a rate of 2 - For lower ranges, the rate shall be smaller to match the number of iterations of the higher value

	for i in range(0,6):
		rate[i] =  2 * data[i] / max_range
	if direction<0:
		for i in range(0,6):
			rate[i]=-rate[i]
	# Motion start Notification
	motion.knee_bending(2)
	motion.knee_bending(8)

	motion.hip_bending(3)
	motion.hip_bending(9)

	motion.ankle_bending(1)
	motion.ankle_bending(7)

	# Motion start
	#print(data[6])
	#print(data[7])
	#print(data[8])
	#print(data[9])
	#print(data[10])
	#print(data[11])
	for i in range(int(max_range)):

		# Right Knee bending
 		pwm.set_pwm(channel[2], 0, int(data[6] + rate[0]))
		#print(data[6]  + rate[0])
		data[6]  += rate[0]

 		# Left Knee bending
 		pwm.set_pwm(channel[8], 0, int(data[7] - rate[1]))
		#print(data[7]  - rate[1])
		data[7]  -= rate[1]

 		# Right Hip bending
 		pwm.set_pwm(channel[3], 0, int(data[8] - rate[2]))
		#print(data[8]  - rate[2])
		data[8]  -= rate[2]

 		# Left Hip bending
 		pwm.set_pwm(channel[9], 0, int(data[9] + rate[3]))
		#print(data[9]  + rate[3])
		data[9]  += rate[3]

 		# Right Ankle bending
 		pwm.set_pwm(channel[1], 0, int(data[10] - rate[4]))
		#print(data[10]  - rate[4])
		data[10]  -= rate[4]

 		# Left Ankle bending
 		pwm.set_pwm(channel[7], 0, int(data[11] - rate[5]))
		#print(data[11]  - rate[5])
		data[11]  -= rate[5]

		# Updation of the current angular postion
		
		current_angle[2] = k
		current_angle[8] = 180-k
		current_angle[3] = p
		current_angle[9] = 90+(90-p)
		current_angle[1] = q
		current_angle[7] = q
#----------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------
# Function to turn to either sides for the robot - Yaw motion via the hip motors and partially using the roll joints at the ankle and the hip. 

# Sequence of actions for right turn - Left leg hip roll tilts the complete body a little towards the left in order to lift the right leg in 
# air just for a fraction of time. Then the right leg yaw turns the complete right leg a little to initiate body turning towards the right. Then after
# this yaw movement, the left leg roll comes back to original postion. Now, the right leg yaw tilts a little to the right to lift the left leg in air for
# some time. Then the left leg yaw turns the towards right so as to align the left leg parallel to the right leg. This process is repeated in case the bot 
# needs to turn more. 
# The same is supposed to be done but in opposite sequence for the left turn - Start with left leg and then the right leg

	
def turn_left_right_(angle_c, direction):

	central_angle_rad = (math.pi * angle_c)/180
	
	
	# central_angle_rad(in radians)  for the hip motor - YAW - from the central axis - Angular Position to be turned upto
	# q_angle(in radians) for the hip motor - ROLL

	# Only 4 motors involved - 2 HIP ROLL and 2 HIP YAW 
	

	data = [0, 0, 0, 0, 0, 0, 0, 0]

	# data[0] to data[3] store the individual ranges
	# data[4] to data[7] store the individual pwm_start values

	data[0], data[4] = motion.right_hip_yaw(angle_c, current_angle[5])
	data[1], data[5] = motion.left_hip_yaw(angle_c, current_angle[11])

	data[2], data[6] = motion.right_hip_roll(70, current_angle[4])
	data[3], data[7] = motion.left_hip_roll(70, current_angle[10])


	# Motion start Notification
	motion.hip_bending(5)
	motion.hip_bending(11)

	motion.hip_bending(4)
	motion.hip_bending(10)

 	# Motion start

 	# For right turn 
 	# Right Hip Roll(10 deg) >> Left hip yaw(Given Angle) >> Right Hip Roll to original(Central angle) >> 
 	# Left Hip Roll(10 deg) >> Right Hip Yaw(Given Angle) >> Left Hip Roll to original(Central angle)

 	# For left turn 
 	# Left Hip Roll(10 deg) >> Right Hip Yaw(Given Angle) >> Left Hip Roll to original(Central angle) >>
 	# Right Hip Roll(10 deg) >> Left hip yaw(Given Angle) >> Right Hip Roll to original(Central angle)  


	if direction == 'right':

 		# Right Hip Roll
 		pwm.set_pwm(channel[4], 0, int(data[6] - data[2]))
		time.sleep(.3)	

 		# Left Hip Yaw
 		pwm.set_pwm(channel[11], 0, int(data[5] + data[1]))
		time.sleep(.3)

 		# Right Hip Roll
 		pwm.set_pwm(channel[4], 0, int(data[6]))
		time.sleep(.3)

 		# Left Hip Roll
 		pwm.set_pwm(channel[10], 0, int(data[7] - data[3]))
 		time.sleep(.3)
		
 		# Right Hip Yaw
 		pwm.set_pwm(channel[5], 0, int(data[4] + data[0]))
                time.sleep(.3)

                # Left Hip Roll
 		pwm.set_pwm(channel[10], 0, int(data[7]))
                time.sleep(.3)
                
	elif direction == 'left':

 		# Left Hip Roll
 		pwm.set_pwm(channel[10], 0, int(data[7] - data[3]))
		time.sleep(0.30)
		
 		# Right Hip Yaw
 		pwm.set_pwm(channel[5], 0, int(data[4] - data[0]))
		time.sleep(0.30)
		
 		# Left Hip Roll
 		pwm.set_pwm(channel[10], 0, int(data[7]))
                time.sleep(0.20)

 		# Right Hip Roll
 		pwm.set_pwm(channel[4], 0, int(data[6] - data[2]))
		time.sleep(0.20)	

 		# Left Hip Yaw
 		pwm.set_pwm(channel[11], 0, int(data[5] - data[1]))
		time.sleep(0.20)

 		# Right Hip Roll
 		pwm.set_pwm(channel[4], 0, int(data[6]))
		time.sleep(0.20)


		# Updation of the current angular postion
		
		current_angle[5] = angle_c
		current_angle[11] = angle_c 	# To be decided based upon the inital configuration

		# current_angle[4] & current_angle[10] -  These values remain unchanged because of the rolling forward and then returning to original position process
		  
#---------------------------------------------------------------------- 	
 	
	
init_stand()
time.sleep(1)
#knee_motion(90,1)
#time.sleep(1)
#knee.motion(0,-1)
#time.sleep(1)
#turn_left_right_(15,'right')
#time.sleep(1)
#turn_left_right_(15,'left')
#time.sleep(1)
for i in range(0,16):
        print(current_angle[i])
        
print("---------------------------------------------------------")



