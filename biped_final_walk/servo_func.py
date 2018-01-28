import Adafruit_PCA9685
import time
import math
from common import *
pwm = Adafruit_PCA9685.PCA9685()
channel = [[5, 4, 3, 2, 1, 0],[ 11, 10, 9, 8, 7, 6]]
frequency = 100

# Functions that this library uses

# pwm.set_pwm(channel, on, off) -
# pwm.set_pwm_freq(frequency value) - Between 40 and 1000 for ideal operation of a servo

pwm.set_pwm_freq(frequency)
pwm.set_pwm(15, 0,0)
pwm.set_pwm(14, 0,0)
pwm.set_pwm(13, 0,0)
pwm.set_pwm(12, 0,0)
def map_value(angle,start_angle,end_angle,start_pwm,end_pwm):
	result=angle*1.0
	result=start_pwm+(result*(end_pwm-start_pwm))/(end_angle-start_angle)
	return result
def step_function(angle,iteration,size,func_type):
	if(func_type == 0):
		return (angle*iteration)/size
	elif(func_type == 1):
		return (math.log(1+((iteration*1.0)/size),2))*angle
	elif(func_type == 2):
		return (math.pow(2,(iteration*1.0)/size)/2)*angle
def pwm_calc(angle,leg,servo_num):
	if(angle<=100 and angle>=-100):
		factor=correction[leg][servo_num]
		if (factor>=0):
			angle=angle+factor
		else:
			angle=180-angle+factor
		pwm_value = int(map_value(angle,0,180,pwm_min[leg][servo_num],pwm_max[leg][servo_num]))
		return pwm_value
	else:
		return -1
def move_servo_to(angle,leg,servo_num):
	pwm_value = pwm_calc(angle,leg,servo_num)
	if(pwm_value>=pwm_min[leg][servo_num] and pwm_value<=pwm_max[leg][servo_num] ):
		pwm_end[leg][servo_num]=pwm_value
	else:
		print "cannot move to angle : %d pwm_value %f leg no : %d servo number : %d" %(angle,pwm_value,leg,servo_num)
def update_pwm():
	for i in range(2):
		for j in range(6):
			pwm_start[i][j]=pwm_end[i][j]
	print pwm_start
def target_servo(iteration,step_size,leg,servo_num):
	pwm_value = pwm_start[leg][servo_num] + (((pwm_end[leg][servo_num]-pwm_start[leg][servo_num])*iteration)/step_size)
	print "%d %d %d %d %d" %(iteration,step_size,leg,servo_num,pwm_value)
	target[leg][servo_num] = int(pwm_value)

def trigger_servo():
	for j in range(6):
		for i in range(2):
			pwm.set_pwm(channel[i][j], 0,target[i][j])
			time.sleep(0.02)
	print target
def trigger_servo_once(step_size):
	for k in range(step_size+1):
		for j in range(6):
			for i in range(2):
				pwm_value = pwm_start[i][j] + (((pwm_end[i][j]-pwm_start[i][j])*k)/step_size)
				pwm.set_pwm(channel[i][j], 0,int(pwm_value))
		time.sleep(0.03)

