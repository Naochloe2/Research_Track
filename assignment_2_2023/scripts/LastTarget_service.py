#! /usr/bin/env python

import rospy
from assignment_2_2023.action import Planning
from assignment_2_2023.srv import Last_target

class LastTarget_service_node():

	def __init__(self, name):
		rospy.Service('get_last_target', Last_target, get_last_target)
		
	def get_last_target(x, y):
		return x, y

if __name__ == "__main__":
    rospy.init_node('LastTarget_service_node')
    LastTarget_service_node()
    rospy.spin()
