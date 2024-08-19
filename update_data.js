const fetch = require('node-fetch');

// Configuración
const weatherApiKey = '249e40695aa1eeb76b7024b7a5380724';
const thingsSpeakApiKey = 'SWEAP6GKNL1888ID';
const city = 'Buenos Aires'; // Puedes cambiar la ciudad aquí

// Función para obtener datos del clima
async function getWeather() {
    const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${weatherApiKey}&units=metric`;
    const response = await fetch(url);
    const data = await response.json();
    const temperature = data.main.temp;
    return temperature;
}

// Función para enviar datos a ThingSpeak
async function updateThingsSpeak(temperature) {
    const url = `https://api.thingspeak.com/update?api_key=${thingsSpeakApiKey}&field1=${temperature}`;
    await fetch(url);
}

// Función principal
async function updateWeatherData() {
    const temperature = await getWeather();
    await updateThingsSpeak(temperature);
}

updateWeatherData();
