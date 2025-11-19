import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=40.71&longitude=-71.01&current=temperature_2m'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data["current"]["temperature_2m"]
    print(f"The current temperature is {temperature} C")
else:
    print("Error retrieving data :(")