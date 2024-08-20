import requests
import time

# API Keys
API_KEY_WEATHER = '249e40695aa1eeb76b7024b7a5380724'
API_KEY_THINGSPEAK = 'SWEAP6GKNL1888ID'

# URLs base
url_thingspeak = f"https://api.thingspeak.com/update?api_key={API_KEY_THINGSPEAK}"
url_weather_buenos_aires = f"http://api.openweathermap.org/data/2.5/weather?q=Buenos%20Aires,AR&appid={API_KEY_WEATHER}&units=metric"
url_weather_villa_maria = f"http://api.openweathermap.org/data/2.5/weather?q=Villa%20Maria,AR&appid={API_KEY_WEATHER}&units=metric"

# Función para obtener datos del clima
def obtener_datos(url):
    response = requests.get(url)
    data = response.json()
    temperatura = data['main']['temp']
    humedad = data['main']['humidity']
    precipitacion = data['rain']['1h'] if 'rain' in data else 0  # Precipitación en la última hora
    return temperatura, humedad, precipitacion

# Bucle para enviar datos cada 15 minutos (900 segundos)
while True:
    # Obtener datos de Buenos Aires
    temperatura_ba, humedad_ba, precipitacion_ba = obtener_datos(url_weather_buenos_aires)

    # Obtener datos de Villa María
    temperatura_vm, humedad_vm, precipitacion_vm = obtener_datos(url_weather_villa_maria)

    # Enviar datos a ThingSpeak (Field1: Temperatura BA, Field2: Humedad BA, Field3: Precipitación BA, Field4: Temperatura VM, Field5: Humedad VM, Field6: Precipitación VM)
    payload = {
        'field1': temperatura_ba,
        'field2': humedad_ba,
        'field3': precipitacion_ba,
        'field4': temperatura_vm,
        'field5': humedad_vm,
        'field6': precipitacion_vm
    }

    response = requests.get(url_thingspeak, params=payload)

    if response.status_code == 200:
        print(f"Datos enviados: Buenos Aires - Temperatura={temperatura_ba}°C, Humedad={humedad_ba}%, Precipitación={precipitacion_ba}mm")
        print(f"Datos enviados: Villa María - Temperatura={temperatura_vm}°C, Humedad={humedad_vm}%, Precipitación={precipitacion_vm}mm")
    else:
        print(f"Error al enviar datos: {response.status_code}")

    # Esperar 15 minutos antes de la próxima actualización
    time.sleep(900)
