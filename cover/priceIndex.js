<script>
let weatherdata3;

function displayData() {
let selectedCrop = document.getElementById("task").value;
let cropData = weatherdata3[selectedCrop];
if (!cropData) {
alert("今日沒有该作物的交易行情數據QAQ！");
return;
}
let htmlContent = "";
for (let location in cropData) {
htmlContent += `
    <div class="location">
        <div >${location}</div>
        <div class="priceIndex">
            
            <span>上價: ${cropData[location]["上價"]}</span>
            <span>中價: ${cropData[location]["中價"]}</span>
            <span>下價: ${cropData[location]["下價"]}</span>
            <span>平均價(元/公斤): ${cropData[location]["平均價(元/公斤)"]}</span>               
            <span>跟前一交易日比較%: ${cropData[location]["跟前一交易日比較%"]}</span>
            <span>交易量(公斤): ${cropData[location]["交易量(公斤)"]}</span>
        </div>
    </div>
`;
}

document.getElementById("cropData").innerHTML = htmlContent;
}

fetch("officialveg.json")
.then(response => response.json())
.then(data => {
weatherdata3 = data;
// Populate the select dropdown with crop options
let selectDropdown = document.getElementById("task");
for (let crop in weatherdata3) {
    let option = document.createElement("option");
    option.value = crop;
    option.text = crop;
    selectDropdown.appendChild(option);
}
})
.catch(error => console.error('Error fetching data:', error));

<script/>
