import RPi.GPIO as GPIO
import math
import time
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

frequency = 100

# Functions that this library uses

# pwm.set_pwm(channel, on, off) -
# pwm.set_pwm_freq(frequency value) - Between 40 and 1000 for ideal operation of a servo

pwm.set_pwm_freq(frequency)


init_stand_pwm_values = [700, 720, 270, 710, 700, 700, 700, 720, 1100, 620, 680, 650, 0, 0, 0, 0]

channel = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def init_stand():
	for index in range(0,16):
		pwm.set_pwm(channel[index], 0, init_stand_pwm_values[index])
		time.sleep(0.020)


def servostablebend( angle2, final_angle2):
  
        angle1=math.atan((math.sin(angle2*3.14/180))/(0.826+math.cos(angle2*3.14/180)))*180/3.14
        angle3=angle2-angle1
        final_angle1=math.atan((math.sin(final_angle2*3.14/180))/(0.826+math.cos(final_angle2*3.14/180)))*180/3.14
        final_angle3 = final_angle2-final_angle1
        pwm1_i=int(720-(angle1*4.722))
        pwm2_i=int(270+(angle2*4.722))
        pwm3_i=int(710-(angle3*4.722))
        pwm7_i=int(720-(angle1*4.722))
        pwm8_i=int(1100-(angle2*4.722))
        pwm9_i=int(620+(angle3*4.722))
        if(final_angle2 > angle2):
            rate2= 2
        else:
            rate2=-2
        rate3=int(rate2*(final_angle3-angle3)/(final_angle2-angle2))
        rate1=int(rate2*(final_angle1-angle1)/(final_angle2-angle2))
        n=int(((final_angle2-angle2)*4.722)/rate2)
        print(final_angle1 )
        print(final_angle3 )
        
        rate3=rate2/2
        rate1=rate2/2
        print(pwm1_i)
        print(pwm2_i)
        print(pwm3_i)
        for i in range(238):
                if (pwm1_i != 720-238):
                      pwm.set_pwm(1, 0, pwm1_i-rate1)
                      pwm.set_pwm(7, 0, pwm7_i-rate1)
                if (pwm2_i != 270+425):
                      pwm.set_pwm(2, 0, pwm2_i+rate2)
                      pwm.set_pwm(8, 0, pwm8_i-rate2)
                if (pwm3_i != 710-187):       
                      pwm.set_pwm(3, 0, pwm3_i-rate3)
                      pwm.set_pwm(9, 0, pwm9_i+rate3)
                pwm1_i-= rate1
                pwm2_i+=rate2
                pwm3_i-=rate3
                pwm7_i-=rate1
                pwm8_i-=rate2
                pwm9_i+=rate3
        print(pwm1_i)
        print(pwm2_i)
        print(pwm3_i)
init_stand()
time.sleep(2)
servostablebend(0,90)
time.sleep(2)
#servostablebend(90,0)
#stime.sleep(2)
#
