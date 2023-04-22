function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var nitrogen = document.getElementById("uiN");
    var phosphorous = document.getElementById("uiP");
    var potassium = document.getElementById("uiK");
    var temperature = document.getElementById("uitemp");
    var humidity = document.getElementById("uihum");
    var ph = document.getElementById("uiph");
    var rainfall = document.getElementById("uirf");
    var estcrop = document.getElementById("uiEstimatedPrice");

  
    var url = "http://127.0.0.1:5000/predict_crops"; //Use this if you are NOT using nginx which is first 7 tutorials
    // var url = "/api/predict_disease"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
  
    $.post(url, {
        nitrogen: parseFloat(nitrogen.value),
        phosphorous: parseFloat(phosphorous.value),
        potassium: parseFloat(potassium.value),
        temperature: parseFloat(temperature.value),
        humidity: parseFloat(humidity.value),
        ph: parseFloat(ph.value),
        rainfall: parseFloat(rainfall.value),
        
    },function(data, status) {
        console.log(data.predicted_crop);
        if (data.predicted_crop) {
          var crop_suitable = data.predicted_crop.Crop_suitable;
          estcrop.innerHTML = "<h2>Predicted crop for growing is : " + crop_suitable + "</h2>";
        } else {
            estcrop.innerHTML = "<h2>Unable to determine disease output</h2>";
        }
        // if (data.predicted_crop) {
        //     var crop_suitable = data.predicted_crop.crop_suitable;
        //     estcrop.innerHTML = "<h2>crop suitable : " + crop_suitable + "</h2>";
        //   } 
        // const cropSuitable = data.Crop_suitable; // using dot notation
        // console.log(cropSuitable); // output: "mango"
        // console.log(status);

    });
  }

function onClickedEstimatePrice2() {
    var estimatedPrice = 0;

    var region = document.getElementById("uir").value;
    var crop_name = document.getElementById("uicn").value;
    var month = parseInt(document.getElementById("uimon").value);
    var day = parseInt(document.getElementById("uid").value);

    if (region == "hyd" && crop_name == "dal" && month == 7 && day == 14) {
        estimatedPrice = 1000; // set the estimated price based on your criteria
    } else {
        estimatedPrice = "Price cannot be estimated for the given input.";
    }

    document.getElementById("uiEstimatedPrice").innerHTML = "<h2>Estimated Price: " + estimatedPrice + "</h2>";
}


