from gpiozero import TonalBuzzer, Button, TrafficLights
from time import sleep

buzzer = TonalBuzzer(17)
button = Button(16)
traffic_lights = TrafficLights(27,22,23)

try:
    while True:
        if button.is_pressed:
             print("Pedestrian crossing activated!")
             buzzer.play(440)
             traffic_lights.red.on()
             traffic_lights.yellow.off()
             traffic_lights.green.off()
             sleep(5)
             buzzer.stop()
             traffic_lights.red.off()
        else:
            traffic_lights.green.on()
            traffic_lights.yellow.off()
            traffic_lights.red.off()
            sleep(5)
            
            traffic_lights.green.off()
            traffic_lights.yellow.on()
            sleep(2)
            
            traffic_lights.yellow.off()
            traffic_lights.red.on()
            sleep(5)
            
            traffic_lights.red.off()
            
except KeyboardInterrupt:
    print("Program interrupted")
          
finally:
    traffic_lights.close()
            