from gpiozero import InputDevice
from time import sleep

sensor = InputDevice(21) # Initialize your GPIO port

while True:

    if sensor.is_active:
    
      print ("No obstacle detected")

    else:
    
        print("Obstacle detected")
    sleep(0.5)