from gpiozero import TonalBuzzer
from time import sleep

buzzer = TonalBuzzer(17)

buzzer.stop()

buzzer.play("A4")
sleep(10)
buzzer.stop()

sleep(5)
buzzer.play("C5")
sleep(10)

buzzer.stop()