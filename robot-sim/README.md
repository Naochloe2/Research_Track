Python Robotics Simulator
================================

This is a simple, portable robot simulator developed by [Student Robotics](https://studentrobotics.org).
Some of the arenas and the exercises have been modified for the Research Track I course

Installing and running
----------------------

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

## Troubleshooting

When running `python run.py <file>`, you may be presented with an error: `ImportError: No module named 'robot'`. This may be due to a conflict between sr.tools and sr.robot. To resolve, symlink simulator/sr/robot to the location of sr.tools.

On Ubuntu, this can be accomplished by:
* Find the location of srtools: `pip show sr.tools`
* Get the location. In my case this was `/usr/local/lib/python2.7/dist-packages`
* Create symlink: `ln -s path/to/simulator/sr/robot /usr/local/lib/python2.7/dist-packages/sr/`

## Exercise
-----------------------------

To run one or more scripts in the simulator, use `run.py`, passing it the file names. 

I am proposing you three exercises, with an increasing level of difficulty.
The instruction for the three exercises can be found inside the .py files (exercise1.py, exercise2.py, exercise3.py).

When done, you can run the program with:

```bash
$ python run.py assignment.py
```

Pseudocode of the assignment
---------

While True :
	If one_token_is_grabbed_by_the_robot :
		If it_is_the_first_token :
			Function_Put_the_token_in_the_center
		Else :
			Function_Get_distance_and_rotation_to_go_the_first_token
			Function_Go_to_release_the_token
	Else : 
		Function_Get_distance_and_rotation_to_go_an_token
		Function_Go_to_grab_the_token


Different functions :
Function_Put_the_token_in_the_center :
	List_of_matricule_already_took <- matricule_of_this_cube
	Turn_little_bit
	Go_forward_little_bit
	Release_the_cube
	Go_backward_from_the_cube

Function_Get_distance_and_rotation_to_go_an_token :
	Define_Default_distance
	For cube on list_of_cube_robot_can_see :  //looking for the closer cube can be see by the robot
If (distance_from_this_cube_smaller_than_previous_one and cube_matricule_not_in_the_list) :
			Returned_distance <- distance_from_this_cube
			Returned_rotation <- rotation_from_this_cube
			Returned_code <- code_of_this_cube
	If Default_distance :
		Return Default_values
	Else :
		Return_Distance_Rotation_Code_for_the_closer_cube

Function_Go_to_release_the_token :
	If_robot_have_grabbed_cube <- True
	If Default_distance :
		Turn_little_bit
	Elif distance_lower_than_treshold :
		Release_the_cube
		If_robot_have_grabbed_cube <- False
		Go_backward_from_the_cube
		If all_cube_are_token :
			Exit_program
	Elif Orientation_in_the_treshold_range :
		If Close_to_the_goal_point :
			Put_down_velocity
		Else :
			Go_forward
	Elif Orientation_less_than_negative_treshold :
		Go_little_bit_left
	Elif Orientation_more_than_positive_treshold :
		Go_little_bit_right
	Return If_robot_have_grabbed_cube

Function_Go_to_grab_the_token :
If_robot_have_grabbed_cube <- True
	If Default_distance :
		Turn_little_bit
	Elif distance_lower_than_treshold :
		Grab_the_cube and If_robot_have_grabbed_cube <- True
		List_of_matricule_already_took <- matricule_of_this_cube
	Elif Orientation_in_the_treshold_range :
		Go_forward
	Elif Orientation_less_than_negative_treshold :
		Go_little_bit_left
	Elif Orientation_more_than_positive_treshold :
		Go_little_bit_right
	Return If_robot_have_grabbed_cube


