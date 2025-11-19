import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

if GPIO.input(17) == GPIO.HIGH:
    print("You're in plain sight!")
else:
    print("Where'd you go?")