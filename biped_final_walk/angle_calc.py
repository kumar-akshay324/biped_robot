import math
from common import *
from servo_func import *

def left_hip_pitch(angle):
	angles_end[1][2]=angle-angles_start[1][2]
	move_servo_to(angle,1,2)
def right_hip_pitch(angle):
	angles_end[0][2]=angle-angles_start[0][2]
	move_servo_to(angle,0,2)

def left_hip_roll(angle):
#	angles_end[1][1]=angle-angles_start[1][1]
	move_servo_to(angle,1,1)
def right_hip_roll(angle):
#	angles_end[0][1]=angle-angles_start[0][1]
	move_servo_to(angle,0,1)

def left_hip_yaw(angle):
#	angles_end[1][0]=angle-angles_start[1][0]
	move_servo_to(angle,1,0)
def right_hip_yaw(angle):
#	angles_end[0][0]=angle-angles_start[0][0]
	move_servo_to(angle,0,0)
	
def left_knee_pitch(angle):
	angles_end[1][3]=angle-angles_start[1][3]
	move_servo_to(angle,1,3)
def right_knee_pitch(angle):
	angles_end[0][3]=angle-angles_start[0][3]
	move_servo_to(angle,0,3)

def left_ankle_pitch(angle):
	angles_end[1][4]=angle-angles_start[1][4]
	move_servo_to(angle,1,4)
def right_ankle_pitch(angle):
	angles_end[0][4]=angle-angles_start[0][4]
	move_servo_to(angle,0,4)
	
def left_ankle_roll(angle):
#	angles_end[1][5]=angle-angles_start[1][5]
	move_servo_to(angle,1,5)
def right_ankle_roll(angle):
#	angles_end[0][5]=angle-angles_start[0][5]
	move_servo_to(angle,0,5)
	
	
def set_angles(angles):
	left_hip_yaw(angles[1][0])
	right_hip_yaw(angles[0][0])
	left_hip_roll(angles[1][1])
	right_hip_roll(angles[0][1])
	left_hip_pitch(angles[1][2])
	right_hip_pitch(angles[0][2])
	left_knee_pitch(angles[1][3])
	right_knee_pitch(angles[0][3])
	left_ankle_pitch(angles[1][4])
	right_ankle_pitch(angles[0][4])
	left_ankle_roll(angles[1][5])
	right_ankle_roll(angles[0][5])

def straight_start():
	angles=[[-5.0,0.0,0.0,0.0,-5.0,0.0],[5.0,0.0,0.0,0.0,0.0,0.0]]
	set_angles(angles)
def double_support_start(foot):
	if(foot == RIGHT):
		angles=[[-5.0,0.0,-85,90.0,-40.0,-7.0],[5.0,8.0,-40.0-20,100.0,-50.0,7.0]]
	else:
		angles=[[-5.0,5.0,-35.0-20,120.0,-20.0,5.0],[5.0,15.0,-75,70.0,-25.0,10.0]]
	set_angles(angles)
def single_support_up(foot):
	if(foot == RIGHT):
		angles=[[-5.0,-12.0,-45.0+bend,95.0,-50.0,-12.0],[5.0,0.0,-65.0+bend,100.0,-35.0,0.0]]
	else:
		angles=[[-5.0,4.0,-55.0+bend,80.0,-25.0,0.0],[5.0,10.0,-35.0+bend,75.0,-40.0,15.0]]
	set_angles(angles)
def double_support_end(foot):
	if(foot == RIGHT ):
		angles=[[-5.0,0.0,-20.0,70.0,-45.0,-10.0],[5.0,10.0,-45.0,80.0,-50.0,5.0]]
	else:
		angles=[[-5.0,-5.0,-50.0,90.0,-60.0,0.0],[5.0,-5.0,-20.0,70.0,-45.0,0.0]]
	set_angles(angles)		
	
def bent_knee_start():
	alpha = math.degrees(math.atan(length_const[2]/length_const[3]))
	beta = math.degrees(math.atan(length_const[3]/length_const[2]))
	angles=[[-5.0,0.0,-beta-5,90,-alpha,0.0],[5.0,0.0,-beta-5,90,-alpha,0.0]]
	set_angles(angles)
def sideways():
	angles=[[0.0,5.0,0.0,0.0,0.0,-7.0],[0.0,5.0,0.0,0.0,0.0,-7.0]]
	set_angles(angles)
def stable(foot):
	if(foot == RIGHT ):
		angles=[[0.0,0.0,-12.0,75.0,-60.0,0.0],[0.0,5.0,-47.0,80.0,-30.0,0.0]]
	else:
		angles=[[0.0,5.0,-50.0,80.0,-30.0,0.0],[0.0,0.0,-15.0,75.0,-60.0,0.0]]
	set_angles(angles)	
def half_up():
	alpha = math.degrees(math.atan(length_const[2]/length_const[3]))
	beta = math.degrees(math.atan(length_const[3]/length_const[2]))
#	angles=[[0.0,10.0,0.0,0.0,0.0,-10.0],[0.0,20.0,-beta,90.0,-alpha+25.0,-10.0]]
	angles=[[0.0,10.0,-25.0,70.0,-45.0,-15.0],[0.0,15.0,-40.0,90.0,-50.0,-15.0]]
	set_angles(angles)
def update_angles_start():
	for i in range(2):
		for j in range(6):
			angles_start[i][j]=angles_end[i][j]+angles_start[i][j]
	print angles_start
	update_pwm()

