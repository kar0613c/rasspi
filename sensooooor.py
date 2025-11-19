from gpiozero import MotionSensor

sens = MotionSensor(18)

while True:
    sens.wait_for_motion()
    print("Saw you!!")
    sens.wait_for_no_motion()