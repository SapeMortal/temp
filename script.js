document.getElementById('city-select').addEventListener('change', (e) => {
  const city = e.target.value;
  document.getElementById('city').innerText = `Ciudad: ${city}`;
  fetchWeather(city);
});

async function fetchWeather(city) {
  const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=249e40695aa1eeb76b7024b7a5380724&units=metric`);
  const data = await response.json();
  document.getElementById('temperature').innerText = `Temperatura: ${data.main.temp}°C`;
}

// Cargar gráfico de ThingSpeak
window.onload = function() {
  fetchWeather('Buenos Aires');
  const chart = document.createElement('iframe');
  chart.src = 'https://thingspeak.com/channels/2624195/charts/1';
  chart.width = '100%';
  chart.height = '400';
  document.getElementById('thingspeak-chart').appendChild(chart);
};
