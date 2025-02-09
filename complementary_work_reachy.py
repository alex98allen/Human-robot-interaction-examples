import numpy as np
import time
from reachy_sdk import ReachySDK
from playsound import playsound 
from reachy_sdk.trajectory import goto
from reachy_sdk.trajectory.interpolation import InterpolationMode
from time import sleep
import cv2 as cv

# Initialize the Reachy robot
reachy = ReachySDK('localhost')
reachy.turn_on('reachy')
reachy.turn_on('head')

# Function to find the dominant color in the captured image
def ColourFinder(debug,reachy):
    print("ColourFinder(",debug,") called")
    print("_"*33)
    try:
        if debug:
            print("Getting Image from camera")
            print("_"*33)
        time.sleep(2) # Waits for the camera to be on target
        image = reachy.right_camera.last_frame #Captures last frame.
        dimensions = image.shape
        h = dimensions[0]
        w = dimensions[1]
        center_x = w/2
        center_y = h/2    
        try:
            if debug:# Opens picture as a new window for verification
                print("Opening captured photo (Close window to continue)")
                time.sleep(1)
                cv.imshow('Original', image)
                cv.waitKey(0)
                cv.destroyAllWindows()
            try:
                if debug:
                    print("_"*33)
                    print("Checking image size:\n")
                    print("Pixel count X-Axis:",image.shape[0])
                    print("Pixel count Y-Axis:",image.shape[1])
                    print("Colour channel count:",image.shape[2])
                    print("Center of X:",center_x)
                    print("Center of Y:",center_y)
                # Extract color values from the center of the image
                bgr = image[int(center_y), int(center_x)]
                rgb = [bgr[2], bgr[1], bgr[0]]
            
                print("Color at coordinates x:",center_x,"y:",center_y," is:\nRed: ",rgb[0],", Green: ",rgb[1],", Blue: ",rgb[2],"\n\n\n")
                return rgb
            except:
                print("Failed to gather pixel, colour or resolution information\n\n\n")
                return (-1,-1,-1)
        except:
            print("Failed to open captured photo\n\n\n")
            return (-1,-1,-1)
    except:
        print("Failed to gather image.\n\n\n")
        return (-1,-1,-1)

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

# Function to open the right gripper
def gripper_open_r():
    pos_r = {
        reachy.r_arm.r_gripper: -15,
    }
    goto(
            goal_positions=pos_r,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to open the left gripper
def gripper_open_l():
    pos_l = {
        reachy.l_arm.l_gripper: 20,
    }
    goto(
            goal_positions=pos_l,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to close the right gripper
def gripper_close_r():
    pos = {
        reachy.r_arm.r_gripper: 10,
    }
    goto(
            goal_positions=pos,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to close the left gripper
def gripper_close_l():
    pos = {
        reachy.l_arm.l_gripper: -1,
    }
    goto(
            goal_positions=pos,
            duration=0.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to set the robot in the ready position
def ready_position():
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
    reachy.l_arm.l_shoulder_pitch: 12,
    reachy.l_arm.l_shoulder_roll: 6,
    reachy.l_arm.l_arm_yaw: 11,
    reachy.l_arm.l_elbow_pitch: -85,
    reachy.l_arm.l_forearm_yaw: 8,
    reachy.l_arm.l_wrist_pitch: -12,
    reachy.l_arm.l_wrist_roll: -32,
    }
    goto(
            goal_positions=pos_r_1,
            duration=2,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

    goto(
            goal_positions=pos_l_1,
            duration=2,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    sleep(1)

# Function to move the left arm to ready position in two steps after picking up color (position 1)
def ready_position_l_1():
    pos_l_1 = {
        reachy.l_arm.l_shoulder_pitch:-20,
        reachy.l_arm.l_shoulder_roll: 78,
        reachy.l_arm.l_arm_yaw: -33,
        reachy.l_arm.l_elbow_pitch: -92,
        reachy.l_arm.l_forearm_yaw: -3,
        reachy.l_arm.l_wrist_pitch: 7,
        reachy.l_arm.l_wrist_roll: -64,
        }
    goto(
                goal_positions=pos_l_1,
                duration=2,
                interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

# Function to move the left arm to ready position in two steps after picking up color (position 2)
def ready_position_l_2():
    pos_l_1 = {
        reachy.l_arm.l_shoulder_pitch: 12,
        reachy.l_arm.l_shoulder_roll: 6,
        reachy.l_arm.l_arm_yaw: 11,
        reachy.l_arm.l_elbow_pitch: -85,
        reachy.l_arm.l_forearm_yaw: 8,
        reachy.l_arm.l_wrist_pitch: -12,
        reachy.l_arm.l_wrist_roll: -32,
        }
    goto(
                goal_positions=pos_l_1,
                duration=2,
                interpolation_mode=InterpolationMode.MINIMUM_JERK
        )

# Function to move the right arm above the brush before picking it up
def above_pick_position():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -106,
        reachy.r_arm.r_shoulder_roll: -57,
        reachy.r_arm.r_arm_yaw: 127,
        reachy.r_arm.r_elbow_pitch: -35,
        reachy.r_arm.r_forearm_yaw: -15,
        reachy.r_arm.r_wrist_pitch: -30,
        reachy.r_arm.r_wrist_roll: 53,
    }
    goto(
            goal_positions=pos,
            duration=2,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to lower the right arm to pick up the brush
def down_to_pick():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -74,
        reachy.r_arm.r_shoulder_roll: -42,
        reachy.r_arm.r_arm_yaw: 103,
        reachy.r_arm.r_elbow_pitch: -9,
        reachy.r_arm.r_forearm_yaw: -6,
        reachy.r_arm.r_wrist_pitch: -31,
        reachy.r_arm.r_wrist_roll: 53,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm above the mixing container before pouring
def above_mixing():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -121,
        reachy.r_arm.r_shoulder_roll: -36,
        reachy.r_arm.r_arm_yaw: 107,
        reachy.r_arm.r_elbow_pitch: -117,
        reachy.r_arm.r_forearm_yaw: -15,
        reachy.r_arm.r_wrist_pitch: -20,
        reachy.r_arm.r_wrist_roll: 65,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    
# Function for the first step of the mixing process
def mixing_step_1():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -73,
        reachy.r_arm.r_shoulder_roll: -30,
        reachy.r_arm.r_arm_yaw: 109,
        reachy.r_arm.r_elbow_pitch: -105,
        reachy.r_arm.r_forearm_yaw: 28,
        reachy.r_arm.r_wrist_pitch: -8,
        reachy.r_arm.r_wrist_roll: 59,
    }
    goto(
            goal_positions=pos,
            duration=0.8,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )
    
# Function for the second step of the mixing process
def mixing_step_2():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -64,
        reachy.r_arm.r_shoulder_roll: -22,
        reachy.r_arm.r_arm_yaw: 97,
        reachy.r_arm.r_elbow_pitch: -91,
        reachy.r_arm.r_forearm_yaw: 37,
        reachy.r_arm.r_wrist_pitch: -19,
        reachy.r_arm.r_wrist_roll: 58,
    }
    goto(
            goal_positions=pos,
            duration=0.6,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function for the third step of the mixing process
def mixing_step_3():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -72,
        reachy.r_arm.r_shoulder_roll: -19,
        reachy.r_arm.r_arm_yaw: 100,
        reachy.r_arm.r_elbow_pitch: -95,
        reachy.r_arm.r_forearm_yaw: 28,
        reachy.r_arm.r_wrist_pitch: -24,
        reachy.r_arm.r_wrist_roll: 46,
    }
    goto(
            goal_positions=pos,
            duration=0.6,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function for the fourth step of the mixing process
def mixing_step_4():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -66,
        reachy.r_arm.r_shoulder_roll: -34,
        reachy.r_arm.r_arm_yaw: 96,
        reachy.r_arm.r_elbow_pitch: -115,
        reachy.r_arm.r_forearm_yaw: 37,
        reachy.r_arm.r_wrist_pitch: -7,
        reachy.r_arm.r_wrist_roll: 53,
    }
    goto(
            goal_positions=pos,
            duration=0.6,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function for the fifth step of the mixing process
def mixing_step_5():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -71,
        reachy.r_arm.r_shoulder_roll: -26,
        reachy.r_arm.r_arm_yaw: 102,
        reachy.r_arm.r_elbow_pitch: -96,
        reachy.r_arm.r_forearm_yaw: 36,
        reachy.r_arm.r_wrist_pitch: -15,
        reachy.r_arm.r_wrist_roll: 56,
    }
    goto(
            goal_positions=pos,
            duration=0.6,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the left arm high above the red color
def before_pick_r():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -70,
        reachy.l_arm.l_shoulder_roll: 53,
        reachy.l_arm.l_arm_yaw: -84,
        reachy.l_arm.l_elbow_pitch: -90,
        reachy.l_arm.l_forearm_yaw: 0,
        reachy.l_arm.l_wrist_pitch: 38,
        reachy.l_arm.l_wrist_roll: -62,
    }
    goto(
            goal_positions=pos,
            duration=4.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the left arm close above the red color
def above_pick_r():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -87,
        reachy.l_arm.l_shoulder_roll: 55,
        reachy.l_arm.l_arm_yaw: -96,
        reachy.l_arm.l_elbow_pitch: -95,
        reachy.l_arm.l_forearm_yaw: 11,
        reachy.l_arm.l_wrist_pitch: 39,
        reachy.l_arm.l_wrist_roll: -60,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to pick the red color with the left arm
def pick_r():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -48,
        reachy.l_arm.l_shoulder_roll: 49,
        reachy.l_arm.l_arm_yaw: -66,
        reachy.l_arm.l_elbow_pitch: -82,
        reachy.l_arm.l_forearm_yaw: -6,
        reachy.l_arm.l_wrist_pitch: 33,
        reachy.l_arm.l_wrist_roll: -56,
    }
    goto(
            goal_positions=pos,
            duration=2.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the left arm high above the yellow color
def before_pick_y():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -64,
        reachy.l_arm.l_shoulder_roll: 59,
        reachy.l_arm.l_arm_yaw: -81,
        reachy.l_arm.l_elbow_pitch: -81,
        reachy.l_arm.l_forearm_yaw: -6,
        reachy.l_arm.l_wrist_pitch: 21,
        reachy.l_arm.l_wrist_roll: -58,
    }
    goto(
            goal_positions=pos,
            duration=4.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the left arm close above the yellow color
def above_pick_y():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -93,
        reachy.l_arm.l_shoulder_roll: 75,
        reachy.l_arm.l_arm_yaw: -98,
        reachy.l_arm.l_elbow_pitch: -102,
        reachy.l_arm.l_forearm_yaw: 4,
        reachy.l_arm.l_wrist_pitch: 26,
        reachy.l_arm.l_wrist_roll: -63,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to pick the yellow color with the left arm
def pick_y():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -46,
        reachy.l_arm.l_shoulder_roll: 57,
        reachy.l_arm.l_arm_yaw: -62,
        reachy.l_arm.l_elbow_pitch: -81,
        reachy.l_arm.l_forearm_yaw: -12,
        reachy.l_arm.l_wrist_pitch: 23,
        reachy.l_arm.l_wrist_roll: -49,
    }
    goto(
            goal_positions=pos,
            duration=2.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the left arm high above the blue color
def before_pick_b():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -58,
        reachy.l_arm.l_shoulder_roll: 67,
        reachy.l_arm.l_arm_yaw: -74,
        reachy.l_arm.l_elbow_pitch: -76,
        reachy.l_arm.l_forearm_yaw: -6,
        reachy.l_arm.l_wrist_pitch: 11,
        reachy.l_arm.l_wrist_roll: -50,
    }
    goto(
            goal_positions=pos,
            duration=4.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the left arm close above the blue color
def above_pick_b():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -84,
        reachy.l_arm.l_shoulder_roll: 72,
        reachy.l_arm.l_arm_yaw: -92,
        reachy.l_arm.l_elbow_pitch: -84,
        reachy.l_arm.l_forearm_yaw: 6,
        reachy.l_arm.l_wrist_pitch: 16,
        reachy.l_arm.l_wrist_roll: -64,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to pick the blue color with the left arm
def pick_b():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -47,
        reachy.l_arm.l_shoulder_roll: 60,
        reachy.l_arm.l_arm_yaw: -61,
        reachy.l_arm.l_elbow_pitch: -72,
        reachy.l_arm.l_forearm_yaw: -14,
        reachy.l_arm.l_wrist_pitch: 12,
        reachy.l_arm.l_wrist_roll: -57,
    }
    goto(
            goal_positions=pos,
            duration=2.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to handover a color container with the left arm
def handover():
    pos = {
        reachy.l_arm.l_shoulder_pitch: -92,
        reachy.l_arm.l_shoulder_roll: 17,
        reachy.l_arm.l_arm_yaw: -28,
        reachy.l_arm.l_elbow_pitch: 0,
        reachy.l_arm.l_forearm_yaw: -59,
        reachy.l_arm.l_wrist_pitch: 5,
        reachy.l_arm.l_wrist_roll: -64,
    }
    goto(
            goal_positions=pos,
            duration=2.5,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the right arm with the brush above an empty container
def above_place_position():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -104,
        reachy.r_arm.r_shoulder_roll: -61,
        reachy.r_arm.r_arm_yaw: 100,
        reachy.r_arm.r_elbow_pitch: -67,
        reachy.r_arm.r_forearm_yaw: -17,
        reachy.r_arm.r_wrist_pitch: 6,
        reachy.r_arm.r_wrist_roll: 65,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to lower the brush into the empty container
def place_position():
    pos = {
        reachy.r_arm.r_shoulder_pitch: -64,
        reachy.r_arm.r_shoulder_roll: -49,
        reachy.r_arm.r_arm_yaw: 75,
        reachy.r_arm.r_elbow_pitch: -52,
        reachy.r_arm.r_forearm_yaw: 17,
        reachy.r_arm.r_wrist_pitch: -10,
        reachy.r_arm.r_wrist_roll: 53,
    }
    goto(
            goal_positions=pos,
            duration=2.0,
            interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the head to the right
def moving_head_to_right():
    head_pos = {
        reachy.head.neck_yaw: -34,
        reachy.head.neck_pitch: 19,
        reachy.head.neck_roll: -11
    }
    goto(
        goal_positions= head_pos,
        duration=2,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the head to the left
def moving_head_to_left():
    head_pos = {
        reachy.head.neck_yaw: 27,
        reachy.head.neck_pitch: 2,
        reachy.head.neck_roll: -31
    }
    goto(
        goal_positions= head_pos,
        duration=2,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the head for Reachy to look to the person while handover
def moving_head_to_handover():
    head_pos = {
        reachy.head.neck_yaw: 18,
        reachy.head.neck_pitch: -5,
        reachy.head.neck_roll: 0
    }
    goto(
        goal_positions= head_pos,
        duration=2,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the head to the ready position
def moving_head_ready():
    head_pos = {
        reachy.head.neck_yaw: 1,
        reachy.head.neck_pitch: -3,
        reachy.head.neck_roll: 7
    }
    goto(
        goal_positions= head_pos,
        duration=2,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to lower the head directed to the mixing container
def moving_head_to_mixing():
    head_pos = {
        reachy.head.neck_yaw: 3,
        reachy.head.neck_pitch: 13,
        reachy.head.neck_roll: -28
    }
    goto(
        goal_positions= head_pos,
        duration=2,
        interpolation_mode=InterpolationMode.MINIMUM_JERK
    )

# Function to move the antennas, which symbolises joy
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

# Function to pick up the red color, do a handover and put the left arm back into ready position 
def red():
    moving_head_to_left()
    above_pick_r()
    before_pick_r()
    pick_r()
    gripper_close_l()
    above_pick_r()
    moving_head_to_handover()
    handover()
    sleep(1) # Waits for the test person to touch the container
    playsound('MP3/attention.mp3') # Reachy warns the test person before letting go of the container
    gripper_open_l()
    happy_gesture()
    sleep(1) 
    ready_position_l_1()
    ready_position_l_2()

# Function to pick up the yellow color, do a handover and put the left arm back into ready position 
def yellow():
    moving_head_to_left()
    above_pick_r()
    before_pick_r()
    before_pick_y()
    pick_y()
    gripper_close_l()
    above_pick_y()
    moving_head_to_handover()
    handover()
    sleep(1)  # Waits for the test person to touch the container
    playsound('MP3/attention.mp3') # Reachy warns the test person before letting go of the container
    gripper_open_l()
    happy_gesture()
    sleep(1)
    ready_position_l_1()
    ready_position_l_2()

# Function to pick up the blue color, do a handover and put the left arm back into ready position 
def blue():
    moving_head_to_left()
    above_pick_r()
    before_pick_r()
    before_pick_y()
    before_pick_b()
    pick_b()
    gripper_close_l()
    above_pick_b()
    moving_head_to_handover()
    handover()
    sleep(1) # Waits for the test person to touch the container
    playsound('MP3/attention.mp3') # Reachy warns the test person before letting go of the container
    gripper_open_l()
    happy_gesture()
    sleep(1)
    ready_position_l_1()
    ready_position_l_2()

# Function to circle the brush inside the mixing container
def mixing():
    moving_head_ready()
    moving_head_to_mixing()
    mixing_step_1()
    a = 1
    while (a<4):
        mixing_step_2()
        mixing_step_3()
        mixing_step_4()
        mixing_step_5()
        a += 1
        mixing_step_2()
        mixing_step_3()
        mixing_step_4()
        mixing_step_5()
        a += 1
    sleep(1)

# Function to pick up the brush and move it above the mixing container
def picking_brush():
    moving_head_ready()
    moving_head_to_right()
    above_pick_position()
    down_to_pick()
    gripper_close_r()
    above_pick_position()
    moving_head_ready()
    above_mixing()

#Functions
turn_on_fans()
ready_position()
gripper_open_l()
gripper_open_r()
moving_head_ready()
playsound('MP3/greeting.mp3') # Reachy greets the test person
playsound('MP3/Farbkarten AUSWAHL 2.mp3') # Reachy explains the procedure, test person has to choose a color card
sleep(3) # Waits for the person the choose the color card
##########################################################
color = ColourFinder(False, reachy)
if color[1] > color[0] and color[1] > color[2]: # The colour value of green is higher than red and blue
    user_color = "Green" 
    print(user_color)
elif color[1] > color[2] and color[0] > color[2]: # The colour value of red and green are both higher than blue 
    user_color = "Orange"
    print(user_color)
else: 
    user_color = "Violet"
    print(user_color)
##########################################################
playsound('MP3/Farben suchen 3.mp3') # Reachy confirms the chosen colour
playsound('MP3/Mischverhältnis 4.mp3') # Reachy explains the mixing procedure
if user_color == "Green":
    yellow() # Giving the yellow color first
    picking_brush()
    mixing()
    blue() # Giving the blue color after mixing
    mixing()
elif user_color == "Orange":
    red() # Giving the red color first
    picking_brush()
    mixing()
    yellow() # Giving the yellow color after mixing
    mixing()
else:
    red() # Giving the red color first
    picking_brush()
    mixing()
    blue() # Giving the blue color after mixing
    mixing() 

moving_head_ready()
user_is_happy = input("Are you happy with the mixed color? If not, which color would you like to add more of?") # Wizard of oz, input for following task is needed
satisfaction = False
while satisfaction == False: # Loop until test person is satisfied with the result
    playsound('MP3/Feedback 5.mp3') # Reachy asks the test person if they are satisfied with the result or if the test person needs any color next
    if user_is_happy == "yellow":
        yellow()
        mixing()
    elif user_is_happy == "blue":
        blue()
        mixing()
    elif user_is_happy == "red":
            red()
            mixing()
    else:
        moving_head_ready()
        playsound('MP3/Ende 6.mp3') # Reachy thanks the test person for the coorperation
        satisfaction = True

above_mixing()
moving_head_to_right()
above_place_position()
place_position()
gripper_open_r()
above_place_position()
moving_head_ready()
ready_position()
playsound('MP3/Ende 6.mp3') # Reachy says goodbye
sleep(5)

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

reachy.turn_off_smoothly('reachy')