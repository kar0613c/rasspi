from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("you moved")
    pir.wait_for_motion()