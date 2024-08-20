import requests
import time

API_KEY = 'SWEAP6GKNL1888ID'  # Tu API Key de ThingSpeak

def send_data(value):
    url = f"https://api.thingspeak.com/update?api_key={API_KEY}&field1={value}"
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Data sent: {value}")
    else:
        print("Failed to send data")

if __name__ == "__main__":
    # Envía datos cada 15 segundos
    for i in range(10):
        send_data(i + 10)  # Enviar un valor diferente en cada iteración
        time.sleep(15)
