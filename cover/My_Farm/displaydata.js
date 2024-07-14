let sensorData;

let ajax = fetch("../sensor_data.json")
    .then(function(response) {
        if (!response.ok) {
            throw new Error("Network response was not ok " + response.statusText);
        }
        return response.json();
    })
    .then(function(data) { 
        sensorData = data; 
        console.log("獲取到的數據:", sensorData); // 添加這一行以調試
        updateWeatherInfo(); // 呼叫函式更新天氣資訊
    })
    .catch(function(error) { 
        console.error("獲取 JSON 數據時發生錯誤:", error); 
    });

function updateWeatherInfo() {
    if (!sensorData) {
        console.error("sensorData 為空，無法更新資訊");
        return;
    }

    // 獲取 sensor1 和 sensor2 的數據
    const sensor1Moisture = sensorData.sensor1.moisture; // 土壤濕度
    const sensor2Temperature = sensorData.sensor2.temperature; // 溫度
    const sensor2Humidity = sensorData.sensor2.humidity; // 濕度

    // 將資料寫入 HTML 中的對應元素
    document.getElementById("moisture").textContent = sensor1Moisture+"%";
    document.getElementById("temperature").textContent = "空氣溫度: " + sensor2Temperature+"%";
    document.getElementById("humidity").textContent = "空氣濕度: " + sensor2Humidity+"%";
}
