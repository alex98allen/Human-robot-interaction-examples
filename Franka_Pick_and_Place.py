try:
    import moveit_commander
    import moveit_msgs.msg
except:
    print('Moveit not installed')

import rospy
import actionlib
import franka_gripper.msg
import actionlib
from time import sleep
import sys

try:
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
except:
    print('MoveIt Planning Group not active')

rospy.init_node('franka_assembly')

# Initialize the Franka robot
group_name = "panda_arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
eef_group_name = "panda_hand"
eef_move_group = moveit_commander.MoveGroupCommander(eef_group_name)

# Setting the speed of the movement
move_group.set_max_acceleration_scaling_factor(0.1)
move_group.set_max_velocity_scaling_factor(0.1)

# Function to close the gripper
def grasp_command():
    client = actionlib.SimpleActionClient(
        "franka_gripper/grasp", franka_gripper.msg.GraspAction)
    client.wait_for_server()
    gripper_epsilon = franka_gripper.msg.GraspEpsilon(
        inner=0.005, outer=0.005)
    client.send_goal(franka_gripper.msg.GraspGoal(
        speed=0.1, width=20.0/1000.0, force=5, epsilon=gripper_epsilon))  # 0.034948.
    client.wait_for_result()
    print(client.get_result())
    print(type(client.get_result()))

# Function to open the gripper
def open_grip():
    client = actionlib.SimpleActionClient(
        "franka_gripper/move", franka_gripper.msg.MoveAction)
    client.wait_for_server()
    client.send_goal(franka_gripper.msg.MoveGoal(speed=0.05, width=0.2))
    client.wait_for_result()
    print(client.get_result())

# Function to move the arm to joint positions
def go_to_joint_goal(joint_state):
    move_group.go(joint_state[:7], wait=True)
    move_group.stop()

# Joint positions of the ready position
ready = [-7.788183204829693e-05, -0.7854296623794605, -1.4358479157090186e-05, -2.356237240261658,
         3.12776209320873e-05, 1.5707363268876005, 0.7853860057788679, 9.827688250225037e-05, 9.827688250225037e-05]

# Joint positions for above the pick position
above_pick_position = [-0.053320971533935335, -0.020245540716081756, 0.47899546549341565, -1.6464334741093873, 
                   0.026943165351747567, 1.585940416243104, 1.2069441789567135]

# Joint positions of the pick position
pick_position = [0.009797359894226526, 0.31019777229684514, 0.42956664248429405, -2.2681867385964876, 
                    -0.1831604888110718, 2.49835005136073, 1.3561957221796308]

# Joint positions for above the place position
above_place_position = [-0.34645665765125955, -0.012386778074294114, -0.4345626179855282, -1.678184077604218, 
                    -0.00014057591050598006, 1.6404980996276244, 0.07597843157953577]

# Joint positions of the place position
place_position = [-0.39853195698091176, 0.32930628588264926, -0.37529983133075817, -2.2289822771117844, 
                     0.2083980953320626, 2.4985187486412936, -0.06966509632223894]


#Functions
go_to_joint_goal(ready)
open_grip()
go_to_joint_goal(above_pick_position)
go_to_joint_goal(pick_position)
grasp_command()
go_to_joint_goal(above_pick_position)
go_to_joint_goal(ready) # Intermediate step makes the movement safer
go_to_joint_goal(above_place_position)
go_to_joint_goal(place_position)
open_grip()
go_to_joint_goal(above_place_position)
go_to_joint_goal(ready)
