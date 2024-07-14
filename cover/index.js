let weatherdata
let weatherdata2

function submitaaa(){
 let value=weatherdata["records"]["location"]
 let value2=weatherdata2[document.getElementById("task").value]

 for(let i=0;i<value.length;i=i+1){
  if(value[i]["locationName"]==document.getElementById("task").value){
   value=value[i]
  }
 }

 let pop="rain.png"
 
 if(value2["PoP"]<10){
  pop="rain.png"
 }else if(value2["PoP"]>20 && value2["PoP"]<50){

 }


 // if(hazards.length==0){}
 if(0<value["hazardConditions"]["hazards"].length){
  document.getElementById("show").innerHTML=`
   <div id="dan_climate">
   <img src="！.png" class="omg"> 氣候警訊：${value["hazardConditions"]["hazards"][0]["info"]["phenomena"]}
   </div>
   <br/>
   <br/>
  `
 }else{
  document.getElementById("show").innerHTML=`
   <div id="dan_climate">
    <img src="！.png" class="omg"> 氣候警訊：無特殊氣候
   </div>
   <br>
   <br>
  `
 }

 document.getElementById("show").innerHTML=`
  ${document.getElementById("show").innerHTML}
  <div class="condition">
    <div class="weatherPhenomena">
    <img src="天氣現象.png" class="phemomena"> <br/> <br/>今日天氣現象： ${value2["Wx"]}
    </div>
    <div class="rainRate">
    <br> <img src="${pop}" class="rainImg"><br/><br/>
    降雨機率:  ${value2["PoP"]}%
    </div>
  </div>  

 `

}

let ajax=fetch("https://opendata.cwa.gov.tw/api/v1/rest/datastore/W-C0033-001?Authorization=CWA-85C09E85-3D71-4466-9252-BCA3299EC408")
 .then(function(response){ return response.json() })
 .then(function(data){ weatherdata=data })
 .catch(function(error){ console.log(error) })

let ajax2=fetch("Weather.json")
 .then(function(response){ return response.json() })
 .then(function(data){ weatherdata2=data })
 .catch(function(error){ console.log(error) })