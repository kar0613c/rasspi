from gpiozero import InputDevice, LED
import time
import csv
import matplotlib.pyplot as plt 

light_sensor = InputDevice(17)
light_data = []
led = LED(27)

with open("light_data.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Time (s)", "light Detected!"])
    
    for i in range(10):
        if light_sensor.is_active:
          led.off()
          light_data.append(1)
          
        else:
          light_data.append(0)
          time.sleep(1)

plt.plot(light_data)
plt.title("Light Level Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Light Intensity (%)")
plt.show()
     