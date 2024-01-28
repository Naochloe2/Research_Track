#! /usr/bin/env python

import rospy
import actionlib
from geometry_msgs.msg import Point, Pose, Twist
import assignment_2_2023.msg
from nav_msg.msg import Odometry

def update_state(msg):

	position = msg.pose.pose.position # get the position from the msg
	velocity = msg.twist.twist.linear # get the twist from the msg
		
	state = Param_robot() # implement a custom message from Param_robot structure
		
	# give msg's parameter to the custom message
	state.x = position.x
	state.y = position.y
	state.vel_x = velocity.x
	state.vel_z = velocity.z
		
	# publish the custom message
	state_pub.publish(state)
		
def action_client_node():

	rospy.init_node('action_client_node')
	# Creates the SimpleActionClient, passing the type of the action to the constructor.
	client = actionlib.SimpleActionClient('action_client',assignment_2_2023.msg.PlanningAction)

	# Waits until the action server has started up and started
	# listening for goals.
	client.wait_for_server()
	pub = rospy.Publisher('/robot_position', Param_robot)
		
	# subscribe to the odometry topic to receive updates on the robot's position and velocity
	odom_subscriber = rospy.Subscriber("/odom", Odometry, update_state)
	
	while not rospy.is_shutdown():
	
		goal = PlanningActionGoal()
		
		set_x = float(input("Please enter the desired X position : "))
		set_y = float(input("Please enter the desired Y position : "))
		
		goal.target_pose.pose.position.x = set_x
		goal.target_pose.pose.position.y = set_y
		
		# Sends the goal to the action server.
    		client.send_goal(goal)
    		client.wait_for_result()
    		result = client.get_result()
    		
    		rate = rospy.Rate(1)
    		
    		if result:
            		rospy.loginfo("Target reached successfully!")
        	else:
            		rospy.loginfo("Target cancellation requested.")
    		
		c_input = input("Please type 'cancel' to cancel the goal: ")
        	if (c_input == "cancel"):
            		print("Goal has been cancelled")
            		client.cancel_goal()
        	else:
            		continue


    # Waits for the server to finish performing the action.
    client.wait_for_result()

    # Prints out the result of executing the action
    return client.get_result()  # A FibonacciResult

if __name__ == '__main__':
	action_client_node()
	while not rospy.is_shutdown():
		rate.sleep()

