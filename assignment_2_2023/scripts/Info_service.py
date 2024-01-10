#! /usr/bin/env python

import rospy
import math
from assignment_2_2023.msg import Param_robot
from assignment_2_2023.srv import Last_target

def DistanceAndSpeedService_node():
	rospy.Subscriber('/robot_position', Param_robot, callBack)
	
def callBack(msg):
	
	goal = assignment_2_2023.msg.Planning()
	# take the target position
	target_x = rospy.get_param("Last_target_x")
	target_y = rospy.get_param("Last_target_y")
	
	#create the service
	srv = rospy.Service('get_distance_and_speed', Info_service, Get_distance_speed)
	
	#calculate the distance and average speed to the target position
        srv.distance = math.dist([target_x, target_y], [msg.x, msg.y])
	srv.average_speed = math.sqrt(msg.vel_x**2 + msg.vel_y**2)

if __name__ == '__main__':
	rospy.init_node('DistanceAndSpeedService_node')
	DistanceAndSpeedService_node()
	rospy.spin()
