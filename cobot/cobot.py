import time
from pymycobot import MyCobot

mc = MyCobot("/dev/ttyUSB0", 115200)

# PLC / handshake pins
START_IN = 0
DONE_OUT = 1

# Pickup path every cycle
PICK_1 = [-342.22, 344.90, 329.72, -178.95, 0.63, -67.55]
PICK_2 = [-342.79, 345.81, 253.84, -179.05, 1.23, -67.56]
PICK_3 = [-343.18, 346.43, 332.54, -179.14, 1.76, -67.56]
PICK_4 = [-342.36, 345.12, 330.60, -178.97, 0.77, -67.56]

# 2 points each placement spot
PLACE_A_UP   = [-168.08, 489.28, 296.63, -179.27, 1.37, -68.17]
PLACE_A_DOWN = [-168.24, 490.83, 238.01, -179.00, 2.37, -68.26]

PLACE_B_UP   = [ -76.17, 396.76, 329.51, -179.40, 0.95, -67.33]
PLACE_B_DOWN = [ -76.03, 398.39, 234.58, -179.00, 1.73, -67.32]

PLACE_C_UP   = [  19.02, 491.73, 238.31, -179.72, 0.87, -70.66]
PLACE_C_DOWN = [  15.13, 496.51, 359.29, -179.77, 0.98, -70.78]

def wait_for_start():
    while mc.get_basic_input(START_IN) != 1:
        time.sleep(0.05)

def pulse_done():
    mc.set_basic_output(DONE_OUT, 1)
    time.sleep(2)
    mc.set_basic_output(DONE_OUT, 0)

def move_path(points, speed):
    for p in points:
        mc.sync_send_coords(p, speed, 0)

def pick_wafer():
    mc.set_gripper_state(0, 80)   # open
    move_path([PICK_1, PICK_2, PICK_3, PICK_4], 80)
    mc.set_gripper_state(1, 80)   # close
    time.sleep(1)

def place_wafer(place_up, place_down):
    mc.sync_send_coords(place_up, 100, 0)
    mc.sync_send_coords(place_down, 36, 0)
    mc.set_gripper_state(0, 80)   # release
    time.sleep(1)
    mc.sync_send_coords(place_up, 100, 0)

def run_cycle(place_up, place_down):
    wait_for_start()

    pick_wafer()
    place_wafer(place_up, place_down)

    # go back ready for next pickup
    mc.sync_send_coords(PICK_1, 100, 0)

    pulse_done()

# Example: A / B / C
run_cycle(PLACE_A_UP, PLACE_A_DOWN)
# run_cycle(PLACE_B_UP, PLACE_B_DOWN)
# run_cycle(PLACE_C_UP, PLACE_C_DOWN)
