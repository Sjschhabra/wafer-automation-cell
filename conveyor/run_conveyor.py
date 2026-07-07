import DobotDllType as dType
import time
import msvcrt
import cv2
import numpy as np
import os
import re
already_photo = 0
first_run = 0

SAVE_DIR = "captured_images"
os.makedirs(SAVE_DIR, exist_ok=True)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Camera not found")
    exit()



print("Camera started. Press q to quit.")
PORT = "COM3"
STEPPER_PORT = 0
SENSOR_PORT1 = 16 # EIO16
SENSOR_PORT2 = 18 # EIO18
conveyor_status = 0
i = 0
api = dType.load()

state = dType.ConnectDobot(api, PORT, 115200)[0]

if state != dType.DobotConnect.DobotConnect_NoError:
    print("Connection failed")
    quit()

print("Connected to Dobot")

# configure EIO16 as digital input
dType.SetIOMultiplexing(api, SENSOR_PORT1, 3, 0)
dType.SetIOMultiplexing(api, SENSOR_PORT2, 3, 0)
os.makedirs(SAVE_DIR, exist_ok=True)


def get_next_image_number(folder):
    max_num = 0

    for filename in os.listdir(folder):
        match = re.match(r"^(\d{4})\.jpg$", filename)
        if match:
            num = int(match.group(1))
            max_num = max(max_num, num)

    return max_num + 1


def save_image(frame, number):
    filename = f"{number:04d}.jpg"
    path = os.path.join(SAVE_DIR, filename)
    cv2.imwrite(path, frame)
    print(f"[SAVE]：{path}")
    
def conveyor1_forward():
    global conveyor_status
    dType.SetEMotor(api, STEPPER_PORT, 1, 10000, 0)
    conveyor_status = 1
    time.sleep(2.5)
    
def conveyor1_reverse():
    global conveyor_status
    dType.SetEMotor(api, STEPPER_PORT, 1, -10000, 0)
    conveyor_status = -1
    time.sleep(2.5)

def stop_conveyor():
    global conveyor_status
    dType.SetEMotor(api, STEPPER_PORT, 1, 0, 0)
    conveyor_status = 0
    time.sleep(2.5)

enabled = False
image_number = get_next_image_number(SAVE_DIR)
print("Press SPACE to start (enable sensor logic). Press 's' to stop and exit.")

try:
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                enabled = True
                print("Enabled. Sensor logic is now active.")
            elif key in (b's', b'S'):
                stop_conveyor()
                print("Stopped motor. Exiting.")
                break

        sensor1 = dType.GetIODI(api, SENSOR_PORT1)[0]
        sensor2 = dType.GetIODI(api, SENSOR_PORT2)[0]
        print(f"Sensor 1: {sensor1}, Sensor 2: {sensor2}")
        ret, frame = cap.read()

        if not ret:
            print("ERROR: Could not read camera frame")
            break

        output = frame.copy()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 7)

        circles = cv2.HoughCircles(
            gray,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=100,
            param1=80,
            param2=35,
            minRadius=40,
            maxRadius=250
        )

        cd_detected = False
        
        if circles is not None:
            circles = np.uint16(np.around(circles))

            for circle in circles[0, :]:
                x, y, r = circle

                if r > 40 and first_run == 1:
                    cd_detected = True

                    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
                    cv2.circle(output, (x, y), 3, (0, 0, 255), 3)
                    cv2.putText(
                        output,
                        "CD DETECTED",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.2,
                        (0, 255, 0),
                        3
                    )

                    break
        cv2.imshow("CD Detection Camera",frame)        
        if enabled:


            if cd_detected == 1 and already_photo == 0 :
                already_photo = 1

               
                print("CD DETECTED")
                time.sleep(1.8)
                # Send LOW to stop conveyor
                stop_conveyor()
                print("LOW sent: conveyor stop signal")

                # Small delay so conveyor can stop before picture
                time.sleep(2)
                ret, frame = cap.read()
                # Capture/save image
                save_image(frame, image_number)
                image_number += 1

                # Keep LOW for 2 seconds
                time.sleep(2)

                # Send HIGH again to start conveyor
                conveyor1_forward()
                
                print("HIGH sent again: conveyor moving")

             

        
            if sensor1 == 0 and conveyor_status == 0:
                first_run = 1
                already_photo = 0
                conveyor1_forward()
            elif sensor1 == 0 and conveyor_status == -1:
                stop_conveyor()
            elif sensor2 == 0 and conveyor_status == 0:
                conveyor1_reverse()
            elif sensor2 == 0 and conveyor_status == 1:
                stop_conveyor()
            
        time.sleep(0.05)
except KeyboardInterrupt:
    stop_conveyor()
finally:
    try:
        dType.DisconnectDobot(api)
    except Exception:
        pass



