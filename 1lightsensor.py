from gpiozero import InputDevice, LED
import time
import csv
import matplotlib.pyplot as plt


light_sensor = InputDevice(17)
light_data = []
led=LED(18)

with open("/home/pi/light_data.csv", mode="w", newline="") as file:
          writer = csv.writer(file)
          writer.writerow(["Time (s)", "Light Detected"])
          

for i in range(30):
    if light_sensor.is_active:
        light_data.append(1)
    else:
        light_data.append(0)
    time.sleep(1)
print("Data collected:", light_data)

plt.plot(light_data)
plt.title("Light Level Over Time")
plt.xlabel("Time (seconds)")
plt.ylabel("Light Intesity (%)")
plt.show()