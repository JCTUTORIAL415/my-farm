let humidity;

let ajax = fetch("humidity.json")
    .then(function(response) { return response.json() })
    .then(function(data) { 
        humidity = data; 
        updateWeatherInfo(); // 呼叫函式更新天氣資訊
    })
    .catch(function(error) { console.log(error) });

function updateWeatherInfo() {
    // 從 JSON 資料中獲取溫度和濕度
    const temperature = humidity.Temperature;
    const humidityValue = humidity.Humidity;

    // 將資料寫入 HTML 中的對應元素
    document.getElementById("temperature").textContent = "空氣溫度:"+temperature;
    document.getElementById("humidity").textContent = "空氣濕度:"+humidityValue;
}