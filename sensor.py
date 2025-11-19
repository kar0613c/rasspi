from gpiozero import LED,Button, MotionSensor
from time import sleep

sensor = MotionSensor(27)


pir = MotionSensor(27)
led1 = LED(17)
led2 = LED(22)
buttton = Button(2)
print("Starting script. Press Ctrl+C to quit.")
print("LED 1 is controlled by the PIR sensor.")
print("lED 2 is controlled by the button.")
    
try:
    while True:
        if pir.motion_dectected:
            print("Motion dected! Tunring on LED 1.")
            led.on()
        else:
            led1.off()
        if button.is_active:
            print("Button pressed! Turning on LED 2.")
            led2.on()
        else:
            led2.off()
        sleep(0.1)
        
except KeyboardInteruppt:
    print("Script interrupted. Cleaning up GPIO pins.")
    led1.close()
    led2.close()