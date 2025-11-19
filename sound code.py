from gpiozero import Buzzer
from time import sleep


buzzer = Buzzer(4)


for i in range(5):
    buzzer.on()
    print ("testing")
    sleep(0.5)
    buzzer.off()
    print ("buzzer off")
    sleep(5)