from __future__ import print_function

import time
from sr.robot import *

a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
d_th_final = 0.5
""" float: Threshold for the control of the linear distance"""

R = Robot()
""" instance of the class Robot"""

matricule = []
"""list of marker already put on the arena zone """

grabbed = False

def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def find_token():
    """
    Function to find the closest token

    Returns:
	dist (float): distance of the closest token (-1 if no token is detected)
	rot_y (float): angle between the robot and the token (-1 if no token is detected)
    """
    dist=100
    for token in R.see():
        if (token.dist < dist) and (token.info.code not in matricule):
            dist=token.dist
	    rot_y=token.rot_y
	    code = token.info.code
	    print("I find a token")
    if dist==100:
    	print("don't find a token")
	return -1, -1, -1
    else:
   	return dist, rot_y, code

def find_center_token():

    dist=100
    for token in R.see():
        if token.info.code == code1:
		dist=token.dist
		rot_y=token.rot_y
    if dist==100:
	return -1, -1
    else:
   	return dist, rot_y

def cube_to_center():
	matricule.append(code1)
	turn(-20, 0.5)
        drive(40, 5)
        R.release()
        grabbed = False
        print("Put it on the arena!") 
        drive(-20, 2)
        turn(10, 1)
        
def go_to_grab(dist, rot_y, code):
	grabbed = False
	if dist==-1:
		turn(20, 0.5)
        	print("I am looking for a token!!")

	elif dist <d_th: 
		print("Found it!")
        	grabbed = R.grab() # if we are close to the token, we grab it.
        	print("Gotcha!")
        	matricule.append(code)
        
    	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
        	#print("Ah, here we are!.")
        	drive(20, 0.5)
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
        	#print("Left a bit...")
        	turn(-2, 0.5)
    	elif rot_y > a_th:
        	# print("Right a bit...")
        	turn(+2, 0.5)
        return grabbed
        	
def go_to_release(dist, rot_y, code):
	grabbed = True
	if dist==-1:
		turn(20, 0.5)
        	print("I am looking for the first token !!")

	elif dist <d_th_final: 
		print("Found final position!")
		R.release()
		print("Put it on the arena!")
		grabbed = False
		drive(-30, 2)
		turn(15, 1)
		print("Go back little bit !")
		if len(matricule) == 7:
			print("I am done my job")
			exit()
        
    	elif -a_th<= rot_y <= a_th: # if the robot is well aligned with the token, we go forward
		# print("Ah, here we are!.")
		if dist < (d_th_final+0.3):
			print("I am already next")
			drive(10, 0.25)
		else:
			print("Go to the central token")
			drive(20, 0.5)
		
    	elif rot_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
		# print("Left a bit...")
		turn(-2, 0.5)
    	elif rot_y > a_th:
		# print("Right a bit...")
		turn(+2, 0.5)
	return grabbed

dist1, rot_y1, code1 = find_token() # we are keeping the number of the first token
print(code1)
first = 1

while 1:
	if grabbed :
		if first == 1:
			print("research for the first token")
			cube_to_center()
			grabbed = False
			first = 0
			print("first token OK")
		else :
			dist, rot_y = find_center_token()  # we look for the first token placed in the center
			grabbed = go_to_release(dist, rot_y, code1)
	else :
		dist, rot_y, code = find_token()  # we look for markers
		grabbed = go_to_grab(dist, rot_y, code)

