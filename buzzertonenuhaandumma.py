from gpiozero import LED, Button, MotionSensor
from time import sleep

sens =  MotionSensor(18)
led1 = LED(22)
led2 = LED(27)
button = Button(2)

while True:
    led1.on()
    sleep(1)
    led1.off()
    led2.on()
    sleep(2)
    led2.off()
    button.wait_for_press()
    led2.toggle()
    sleep(0.5)
    
#use
print("The script is starting. Press Ctrl+C to quit!")
print("LED 1 is being controlled by the SENS sensor.")
print("LED 2 is being controlled by the button!")

try:
    while True:
        if sens.motion_detected:
            print("I saw that! Now turning on LED 1.")
            led1.on()
        else:
            led1.off()
            
        if button.is_active:
            print("You pressed the button!! Now turning on LED 2.")
            led1.close()
        else:
            led2.off()
        sleep(0.1)
except KeyboardInterrupt:
    print("Your script was stopped. Cleaning up GPIO pins...")
    led1.close()
    led2.close()
    