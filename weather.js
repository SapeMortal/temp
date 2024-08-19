const apiKey = '249e40695aa1eeb76b7024b7a5380724';
const city = 'Buenos Aires';  // Puedes cambiarlo según la ciudad seleccionada

async function getWeatherData() {
    const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`);
    const data = await response.json();
    return data;
}

getWeatherData().then(data => console.log(data));
