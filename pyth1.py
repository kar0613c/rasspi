from gpiozero import Buzzer, Button
from time import sleep

Buzzer = Buzzer(4)
button = Button(18)

while true button.wait_for_press()
Buzzer.toggle()
sleep(0.5)