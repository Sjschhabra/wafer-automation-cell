import time
from pymycobot import MyCobot

mc = MyCobot("/dev/ttyUSB0", 115200)

# Handshake pins
START_IN = 1
DONE_OUT = 1

# First pickup path from your export
PICK_1 = [-342.22, 344.90, 329.72, -178.95, 0.63, -67.55]
PICK_2 = [-342.79, 345.81, 253.84, -179.05, 1.23, -67.56]
PICK_3 = [-343.18, 346.43, 332.54, -179.14, 1.76, -67.56]
PICK_4 = [  15.13, 496.51, 359.29, -179.77, 0.98, -70.78]

# A / B / C placement points from your export
A_UP   = [-168.08, 489.28, 296.63, -179.27, 1.37, -68.17]
A_DOWN = [-168.24, 490.83, 238.01, -179.00, 2.37, -68.26]

B_UP   = [ -76.17, 396.76, 329.51, -179.40, 0.95, -67.33]
B_DOWN = [ -76.03, 398.39, 234.58, -179.00, 1.73, -67.32]

C_UP   = [  19.02, 491.73, 238.31, -179.72, 0.87, -70.66]
C_DOWN = [  15.13, 496.51, 359.29, -179.77, 0.98, -70.78]


def wait_for_start():
    while mc.get_basic_input(START_IN) != 1:
        time.sleep(0.05)


def pulse_done():
    mc.set_basic_output(DONE_OUT, 1)
    time.sleep(2)
    mc.set_basic_output(DONE_OUT, 0)


def move_path(points, speeds):
    for point, speed in zip(points, speeds):
        mc.sync_send_coords(point, speed, 0)


def pick_wafer():
    mc.set_gripper_state(0, 80)  # open
    move_path(
        [PICK_1, PICK_2, PICK_3, PICK_4],
        [100, 9, 36, 100]
    )
    mc.set_gripper_state(1, 80)  # close
    time.sleep(1)


def place_wafer(place_up, place_down):
    mc.sync_send_coords(place_up, 100, 0)
    mc.sync_send_coords(place_down, 36, 0)
    mc.set_gripper_state(0, 80)  # release
    time.sleep(1)
    mc.sync_send_coords(place_up, 100, 0)


def run_cycle(place_up, place_down):
    wait_for_start()
    pick_wafer()
    place_wafer(place_up, place_down)

    # Go back ready for the next pickup
    mc.sync_send_coords(PICK_1, 100, 0)

    pulse_done()


while True:
    run_cycle(A_UP, A_DOWN)
    run_cycle(B_UP, B_DOWN)
    run_cycle(C_UP, C_DOWN)
