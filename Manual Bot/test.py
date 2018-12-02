from evdev import InputDevice, categorize, ecodes, events
import time


gamepad = InputDevice('/dev/input/event17')
ARM = False
DRIVE = True


def drive():

    global gamepad, ARM, DRIVE
    for event in gamepad.read_loop():

        if event.code == 17:

            if event.value == -1:
                print("Forward")

            elif event.value == 1:
                print("Backward")

            elif event.value == 0:
                print("Stop")

        elif event.code == 16:

            if event.value == -1:
                print("Left")
            elif event.value == 1:
                print("Right")

            elif event.value == 0:
                print("Stop")

        elif event.code == 4:

            if event.value == 589833:
                print("Controll Change")
                ARM = True
                DRIVE = False
                break;

def arm():

    global gamepad, DRIVE, ARM

    for event in gamepad.read_loop():

        if event.code == 17:

            if event.value == -1:
                print("Suction Cup On")

            elif event.value == 1:
                print("Suction Cup Off")
        elif event.code == 16:

            if event.value == -1:
                print("Dart Released")
            elif event.value == 1:
                print("Dart Released")

        elif event.code == 04:

            if event.value == 589825 :
                print("Servo 1 Forward")

            elif event.value == 589827:
                print("Servo 1 Backward")

            elif event.value == 589828:
                print("Servo 2 Backward")

            elif event.value == 589826:
                print("Servo 2 Backward")

            elif event.value == 589831:
                print("Servo 3 Backward")

            elif event.value == 589832:
                print("Servo 3 Backward")

            elif event.value == 589830:
                print("Stepper Forward")
            elif event.value == 589829:
                print("Stepper Backward")

            elif event.value == 589834:
                print("Controll Change")
                DRIVE = True
                ARM = False
                break


def main():

    global ARM , DRIVE

    while True:
        if ARM == True:
            arm()
        elif DRIVE == True:
            drive()

if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Shutting Down")
    finally:
        print("Done")
