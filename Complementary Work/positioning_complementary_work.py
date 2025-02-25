#Positioning colour container
turn_on_fans()
ready_position()
gripper_open_l()
gripper_open_r()
moving_head_ready()
red()
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


#Positioning pick container for brush
turn_on_fans()
ready_position()
gripper_open_l()
gripper_open_r()
moving_head_ready()
picking_brush()
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


#Positioning mixing container
turn_on_fans()
ready_position()
gripper_open_l()
gripper_open_r()
moving_head_ready()
picking_brush()
mixing()
above_mixing()
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


#Positioning place container for brush
turn_on_fans()
ready_position()
gripper_open_l()
gripper_open_r()
moving_head_ready()
picking_brush()
moving_head_to_right()
above_place_position()
place_position()
gripper_open_r()
above_place_position()
moving_head_ready()
ready_position()
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