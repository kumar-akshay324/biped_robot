import Tkinter as tk
import random
import math
from common import *
from angle_calc import *

xstart = [[0 for x in range(8)] for y in range(2)]
xend = [[0 for x in range(8)] for y in range(2)]
ystart = [[0 for x in range(8)] for y in range(2)]
yend = [[0 for x in range(8)] for y in range(2)]
flag=0

def modify_coords(iteration,step_size):
	xstart[0][0] =  450
	ystart[0][0] = 100
	xstart[1][0] =  450
	ystart[1][0] = 100
	total_angle = [0.0,0.0]
	for i in range(2):
		for j in range(6):
			if(i==1 and j==3):
				func=0
			else:
				func=0
			total_angle[i]+=angles_start[i][j]+step_function(angles_end[i][j],iteration,step_size,func)
			target_servo(iteration,step_size,i,j)
			xend[i][j] = xstart[i][j] + int(length_const[j]*math.cos(math.radians(mean_pos[i][j] +total_angle[i])))
			yend[i][j] = ystart[i][j] - int(length_const[j]*math.sin(math.radians(mean_pos[i][j] +total_angle[i])))
			xstart[i][j+1] = xend[i][j]
			ystart[i][j+1] = yend[i][j]
	print ""
	xstart[0][7]=xstart[0][6]
	ystart[0][7]=ystart[0][6]
	xstart[1][7]=xstart[1][6]
	ystart[1][7]=ystart[1][6]

	
	
	xend[0][6]=	xstart[0][6] + int(length_const[6]*math.cos(math.radians(total_angle[0])))
	yend[0][6]=	ystart[0][6] - int(length_const[6]*math.sin(math.radians(total_angle[0])))
	
	xend[0][7]=	xstart[0][7] + int(length_const[7]*math.cos(math.radians(total_angle[0]+180.0)))
	yend[0][7]=	ystart[0][7] - int(length_const[7]*math.sin(math.radians(total_angle[0]+180.0)))
		
	xend[1][6]=	xstart[1][6] + int(length_const[6]*math.cos(math.radians(total_angle[1])))
	yend[1][6]=	ystart[1][6] - int(length_const[6]*math.sin(math.radians(total_angle[1])))
	
	xend[1][7]=	xstart[1][7] + int(length_const[7]*math.cos(math.radians(total_angle[1]+180.0)))
	yend[1][7]=	ystart[1][7] - int(length_const[7]*math.sin(math.radians(total_angle[1]+180.0)))
	
	delta_y =500-max(yend[0][6],yend[0][7],yend[1][6],yend[1][7])
	delta_x =450-xstart[0][6]
	for i in range(2):
		for j in range(8):
			yend[i][j]=yend[i][j]+delta_y
			ystart[i][j]=ystart[i][j]+delta_y
			xend[i][j]=xend[i][j]+delta_x
			xstart[i][j]=xstart[i][j]+delta_x

def init_coords():
	straight_start()
	modify_coords(1,1)

root = tk.Tk()
canvas = tk.Canvas(root,height=600, width=900)
canvas.pack()
tilt_text=canvas.create_text(100,100,fill="darkblue",font="Times 20 italic bold",text=str(counter))
def create_lines(canvas):
	global xstart,xend,ystart,yend
	line_obj = []
	init_coords()
	for i in range(2):
		for j in range(8):
			x1 = xstart[i][j]	
			y1 = ystart[i][j]
			x2 = xend[i][j]
			y2 = yend[i][j]
			if(i==0):
				color="blue"
			else:
				color="red"
			line = canvas.create_line(x1, y1, x2, y2, width=5, fill=color)
			line_obj.append( [line,i,j] )
	update_angles_start()
	return line_obj

def moves_lines(canvas, line_objs,iteration,step_size):
	modify_coords(iteration,step_size)
	for line, i,j in line_objs:
		x1 = xstart[i][j]
		y1 = ystart[i][j]
		x2 = xend[i][j]
		y2 = yend[i][j]
		canvas.coords(line, x1, y1, x2, y2)
		if((i==1 and j==4)or(i==1 and j==2)):
			canvas.create_oval(x1, y1, x1-1, y1-1, fill="green")
#		print canvas.coords(line)
	if(iteration < step_size):
		global speed
		iteration+=1
		root.after(speed, moves_lines, canvas, line_objs,iteration,step_size)
	else:
		global flag
		flag=0
		trigger_servo_once(step_size)
		update_angles_start()

def move_right(event):
	global line_objs,flag,speed
	if(flag==0):
		flag=1
		bent_knee_start()
		root.after(speed, moves_lines, canvas, line_objs,1,20)
	pass

def move_left(event):
	global tilt,bend,line_objs,flag,speed
	if(flag==0):
		flag=1
		bend=-50.0
		double_support_end(RIGHT)
		root.after(speed, moves_lines, canvas, line_objs,1,20)

def move_up(event):
	global line_objs,flag,speed
	if(flag==0):
		flag=1		
		stable(LEFT)
		root.after(speed, moves_lines, canvas, line_objs,1,10)

def move_down(event):
	global line_objs,flag,speed
	if(flag==0):
		flag=1		
		straight_start()
		root.after(speed, moves_lines, canvas, line_objs,1,15)

def next_step(event):
	global line_objs,counter,flag,speed,tilt
	canvas.itemconfig(tilt_text,text=str(tilt))
	if(flag==0):
		flag=1
		if(counter==0):		
			double_support_start(RIGHT)
		elif(counter==1):
			single_support_up(RIGHT)
		elif(counter==2):
			double_support_end(RIGHT)
		elif(counter==3):
			stable(RIGHT)
		elif(counter==4):
			double_support_start(LEFT)
		elif(counter==5):
			single_support_up(LEFT)
		elif(counter==6):
			double_support_end(LEFT)
		elif(counter==7):
			stable(LEFT)
		counter=(counter+1)%8
		root.after(speed, moves_lines, canvas, line_objs,1,12)

root.bind('<Right>', move_right)
root.bind('<Left>', move_left)
root.bind('<Up>', move_up)
root.bind('<Down>', move_down)
root.bind('<Return>', next_step)
line_objs = create_lines(canvas)
print xstart
print ystart
print xend
print yend
root.mainloop() 
