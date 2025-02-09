import numpy as np
import time
from reachy_sdk import ReachySDK
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from time import sleep

# Initialize the Reachy robot
reachy = ReachySDK('localhost')
reachy.turn_on('reachy')


# Function to control fans  
def turn_on_fans():
    reachy.fans.l_shoulder_fan.on()
    reachy.fans.l_elbow_fan.on()
    reachy.fans.l_wrist_fan.on()
    reachy.fans.r_shoulder_fan.on()
    reachy.fans.r_elbow_fan.on()
    reachy.fans.r_wrist_fan.on()
    reachy.fans.l_antenna_fan.on() 
    reachy.fans.r_antenna_fan.on() 
def turn_off_fans():
    reachy.fans.l_shoulder_fan.off()
    reachy.fans.l_elbow_fan.off()
    reachy.fans.l_wrist_fan.off()
    reachy.fans.r_shoulder_fan.off()
    reachy.fans.r_elbow_fan.off()
    reachy.fans.r_wrist_fan.off()
    reachy.fans.l_antenna_fan.off() 
    reachy.fans.r_antenna_fan.off() 



# Function to set the robot in the ready position
def readyPosition():
    pos_r_1 = {
        reachy.r_arm.r_shoulder_pitch: -5,
        reachy.r_arm.r_shoulder_roll: -5,
        reachy.r_arm.r_arm_yaw: -2,
        reachy.r_arm.r_elbow_pitch: -80,
        reachy.r_arm.r_forearm_yaw: -7,
        reachy.r_arm.r_wrist_pitch: -4,
        reachy.r_arm.r_wrist_roll: 49,
    }
    pos_l_1 = {
    reachy.l_arm.l_shoulder_pitch: -2,
    reachy.l_arm.l_shoulder_roll: 1,
    reachy.l_arm.l_arm_yaw: -1,
    reachy.l_arm.l_elbow_pitch: -80,
    reachy.l_arm.l_forearm_yaw: -3,
    reachy.l_arm.l_wrist_pitch: -7,
    reachy.l_arm.l_wrist_roll: -20,
    }
    goto(
            goal_positions=pos_r_1,
            duration=2.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    goto(
            goal_positions=pos_l_1,
            duration=2.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    sleep(1)

# Function to open the right gripper
def gripper_open():
    pos_r = {
        reachy.r_arm.r_gripper: -20,
    }
    goto(
            goal_positions=pos_r,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    pos_l = {
        reachy.l_arm.l_gripper: -20,
    }
    goto(
            goal_positions=pos_l,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to close the right gripper
def gripper_close():
    pos = {
        reachy.r_arm.r_gripper: 10,
    }
    goto(
            goal_positions=pos,
            duration=1.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm above the pick position
def above_pick_position():
    pos = {
        reachy.r_arm.r_shoulder_pitch: 32,
        reachy.r_arm.r_shoulder_roll: -33,
        reachy.r_arm.r_arm_yaw: -61,
        reachy.r_arm.r_elbow_pitch: -90,
        reachy.r_arm.r_forearm_yaw: -42,
        reachy.r_arm.r_wrist_pitch: 13,
        reachy.r_arm.r_wrist_roll: 42,
    }
    goto(
            goal_positions=pos,
            duration=3.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm into the pick position
def down_to_pick():
    pos_1 = {
        reachy.r_arm.r_shoulder_pitch: -1,
        reachy.r_arm.r_shoulder_roll: -17,
        reachy.r_arm.r_arm_yaw: -70,
        reachy.r_arm.r_elbow_pitch: -85,
        reachy.r_arm.r_forearm_yaw: -3,
        reachy.r_arm.r_wrist_pitch: 12,
        reachy.r_arm.r_wrist_roll: 65,
    }
    goto(
            goal_positions=pos_1,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    pos_2 = {
        reachy.r_arm.r_shoulder_pitch: -18,
        reachy.r_arm.r_shoulder_roll: -31,
        reachy.r_arm.r_arm_yaw: -57,
        reachy.r_arm.r_elbow_pitch: -54,
        reachy.r_arm.r_forearm_yaw: -4,
        reachy.r_arm.r_wrist_pitch: 0,
        reachy.r_arm.r_wrist_roll: 57,
    }
    goto(
            goal_positions=pos_2,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm up again above the pick position
def going_up_pick():
    pos_2 = {
        reachy.r_arm.r_shoulder_pitch: -11,
        reachy.r_arm.r_shoulder_roll: -31,
        reachy.r_arm.r_arm_yaw: -57,
        reachy.r_arm.r_elbow_pitch: -82,
        reachy.r_arm.r_forearm_yaw: -7,
        reachy.r_arm.r_wrist_pitch: 23,
        reachy.r_arm.r_wrist_roll: 42,
    }
    goto(
            goal_positions=pos_2,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm above the place position
def going_to_place():
    pos= {
        reachy.r_arm.r_shoulder_pitch: -45,
        reachy.r_arm.r_shoulder_roll: -31,
        reachy.r_arm.r_arm_yaw: 60,
        reachy.r_arm.r_elbow_pitch: -103,
        reachy.r_arm.r_forearm_yaw: -49,
        reachy.r_arm.r_wrist_pitch: 9,
        reachy.r_arm.r_wrist_roll: 9,
    }
    goto(
            goal_positions=pos,
            duration=3.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm into the place position
def placing_object():
    pos_1 = {
        reachy.r_arm.r_shoulder_pitch: -15,
        reachy.r_arm.r_shoulder_roll: -6,
        reachy.r_arm.r_arm_yaw: 26,
        reachy.r_arm.r_elbow_pitch: -93,
        reachy.r_arm.r_forearm_yaw: -14,
        reachy.r_arm.r_wrist_pitch: 16,
        reachy.r_arm.r_wrist_roll: 52,
    }
    goto(
            goal_positions=pos_1,
            duration=3.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    pos_2 = {
        reachy.r_arm.r_shoulder_pitch: -14,
        reachy.r_arm.r_shoulder_roll: -11,
        reachy.r_arm.r_arm_yaw: 37,
        reachy.r_arm.r_elbow_pitch: -77,
        reachy.r_arm.r_forearm_yaw: -12,
        reachy.r_arm.r_wrist_pitch: -9,
        reachy.r_arm.r_wrist_roll: 51,
    }
    goto(
            goal_positions=pos_2,
            duration=3.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm above the place position again
def going_up_place():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -14,
        reachy.r_arm.r_shoulder_roll: -11,
        reachy.r_arm.r_arm_yaw: 37,
        reachy.r_arm.r_elbow_pitch: -90,
        reachy.r_arm.r_forearm_yaw: -12,
        reachy.r_arm.r_wrist_pitch: -9,
        reachy.r_arm.r_wrist_roll: 51,
    }
    goto(
            goal_positions=pos,
            duration=3.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the antennas to make it look like Reachy is happy
def happy_gesture():
    reachy.head.l_antenna.speed_limit = 130
    reachy.head.r_antenna.speed_limit = 130
    for _ in range(3):
        reachy.head.l_antenna.goal_position = 100.0
        reachy.head.r_antenna.goal_position = -100.0

        time.sleep(0.5)

        reachy.head.l_antenna.goal_position = -100.0
        reachy.head.r_antenna.goal_position = 100.0

        time.sleep(0.5)

    reachy.head.l_antenna.goal_position = 0.0
    reachy.head.r_antenna.goal_position = 0.0

# Function to move the left arm to wave goodbye
def wave_goodbye():
    reachy.turn_on('r_arm')

    left_arm_destination = {
        reachy.l_arm.l_shoulder_pitch: -20,
        reachy.l_arm.l_shoulder_roll: 20,
        reachy.l_arm.l_arm_yaw: 30,
        reachy.l_arm.l_elbow_pitch: -120,
        reachy.l_arm.l_forearm_yaw: 60,
        reachy.l_arm.l_wrist_pitch: 0,
        reachy.l_arm.l_wrist_roll: 20,
        reachy.l_arm.l_gripper: 69
        }

    goto(
            goal_positions=left_arm_destination,
            duration=3.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    for _ in range(3):
        reachy.l_arm.l_wrist_roll.goal_position = 20
        time.sleep(0.5)

        reachy.l_arm.l_wrist_roll.goal_position = -20
        time.sleep(0.5)


#Functions
turn_on_fans()
sleep(5)
gripper_open()
readyPosition()
above_pick_position()
down_to_pick()
gripper_close()
going_up_pick()
going_to_place()
placing_object()
gripper_open()
going_up_place()
readyPosition()
happy_gesture()
wave_goodbye()
readyPosition()

sleep(7)

try:
    reachy.r_arm.r_gripper.compliant = False
except AttributeError:
    print('Reachy has no right arm.')

try:
    reachy.l_arm.l_gripper.compliant = False
except AttributeError:
    print('Reachy has no left arm.')

reachy.r_arm.r_gripper.goal_position = 0
reachy.l_arm.l_gripper.goal_position = 0

########

reachy.turn_off_smoothly('reachy')
