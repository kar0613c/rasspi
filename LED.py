from gpiozero import LED, Button
from time import sleep

led1= LED(17)
button = Button(2)
led2= LED(22)

while True:
    button.wait_for_press()
    led1.toggle()
    led2.toggle() 
    sleep(0.5)
    led1.on()
    sleep(0.1)
    led1.off()
    sleep(0.1)
    
    led2.on()
    sleep(0.1)
    led2.off()
    sleep(0.1)
    