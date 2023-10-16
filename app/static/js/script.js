function ResetData() {
    document.getElementById("formId").reset();
    document.getElementById('resultText').setAttribute('class', 'd-none');
    document.getElementById('resetButton').setAttribute('class', 'd-none')
}

function fetchPrediction() {
    let ID =  document.getElementById('ID').value;
    let Delivery_person_ID = document.getElementById('Delivery_person_ID').value;
    let Delivery_person_Age =  document.getElementById('Delivery_person_Age').value;
    let Delivery_person_Ratings =  document.getElementById('Delivery_person_Ratings').value;
    let Restaurant_latitude=  document.getElementById('Restaurant_latitude').value;
    let Restaurant_longitude =  document.getElementById('Restaurant_longitude').value;
    let Delivery_location_latitude =  document.getElementById('Delivery_location_latitude').value;
    let Delivery_location_longitude =  document.getElementById('Delivery_location_longitude').value;
    let Order_Date =  document.getElementById('Order_Date').value;
    let Time_Ordered =  document.getElementById('Time_Ordered').value;
    let Time_Order_picked =  document.getElementById('Time_Order_picked').value;
    let Weatherconditions =  document.getElementById('Weatherconditions').value;
    let Road_traffic_density =  document.getElementById('Road_traffic_density').value;
    let Vehicle_condition =  parseInt(document.getElementById('Vehicle_condition').value);
    let Type_of_order =  document.getElementById('Type_of_order').value;
    let Type_of_vehicle =  document.getElementById('Type_of_vehicle').value;
    let multiple_deliveries =  document.getElementById('multiple_deliveries').value;
    let Festival =  document.getElementById('Festival').value;
    let City =  document.getElementById('City').value;

    console.log(
        ID,
        Delivery_person_ID,
        Delivery_person_Age,
        Delivery_person_Ratings,
        Restaurant_latitude,
        Restaurant_longitude,
        Delivery_location_latitude,
        Delivery_location_longitude,
        Order_Date,
        Time_Ordered,
        Time_Order_picked,
        Weatherconditions,
        Road_traffic_density,
        Vehicle_condition,
        Type_of_order,
        Type_of_vehicle,
        multiple_deliveries,
        Festival,
        City,
    )

    $.ajax({
        method: 'GET',
        url: '/prediction',
        data: {
            ID: ID,
            Delivery_person_ID: Delivery_person_ID,
            Delivery_person_Age: Delivery_person_Age,
            Delivery_person_Ratings: Delivery_person_Ratings,
            Restaurant_latitude: Restaurant_latitude,
            Restaurant_longitude: Restaurant_longitude,
            Delivery_location_latitude: Delivery_location_latitude,
            Delivery_location_longitude: Delivery_location_longitude,
            Order_Date: Order_Date,
            Time_Ordered: Time_Ordered,
            Time_Order_picked: Time_Order_picked,
            Weatherconditions: Weatherconditions,
            Road_traffic_density: Road_traffic_density,
            Vehicle_condition: Vehicle_condition,
            Type_of_order: Type_of_order,
            Type_of_vehicle: Type_of_vehicle,
            multiple_deliveries: multiple_deliveries,
            Festival: Festival,
            City:City,
        },
        success: function (data) {
            document.getElementById('resultText').removeAttribute('class', 'd-none');
            document.getElementById('resultText').setAttribute('class', 'text-white');

            document.getElementById('resetButton').removeAttribute('class');
            document.getElementById('resetButton').setAttribute('class', 'btn btn-secondary btn-lg');
            $("#result").text(data)

        },
        error: function (error_data) {
            alert(error_data)
        }
    })
}


function ResetData() {
    document.getElementById("deliveryForm").reset();
    document.getElementById('resultText').setAttribute('class', 'd-none');
    document.getElementById('resetButton').setAttribute('class', 'd-none')
}



// document.getElementById('deliveryForm').addEventListener('submit', function(event) {
//     event.preventDefault();

//     // Capture input values
//     var inputs = {
//         'ID': document.getElementById('ID').value,
//         'Delivery_person_ID': document.getElementById('Delivery_person_ID').value,
//         'Delivery_person_Age': parseFloat(document.getElementById('Delivery_person_Age').value),
//         'Delivery_person_Ratings': parseFloat(document.getElementById('Delivery_person_Ratings').value),
//         'Restaurant_latitude': parseFloat(document.getElementById('Restaurant_latitude').value),
//         'Restaurant_longitude': parseFloat(document.getElementById('Restaurant_longitude').value),
//         'Delivery_location_latitude': parseFloat(document.getElementById('Delivery_location_latitude').value),
//         'Delivery_location_longitude': parseFloat(document.getElementById('Delivery_location_longitude').value),
//         'Order_Date': document.getElementById('Order_Date').value,
//         'Time_Ordered': document.getElementById('Time_Ordered').value,
//         'Time_Order_picked': document.getElementById('Time_Order_picked').value,
//         'Weatherconditions': document.getElementById('Weatherconditions').value,
//         'Road_traffic_density': document.getElementById('Road_traffic_density').value,
//         'Vehicle_condition': parseInt(document.getElementById('Vehicle_condition').value),
//         'Type_of_order': document.getElementById('Type_of_order').value,
//         'Type_of_vehicle': document.getElementById('Type_of_vehicle').value,
//         'multiple_deliveries': parseFloat(document.getElementById('multiple_deliveries').value),
//         'Festival': document.getElementById('Festival').value,
//         'City': document.getElementById('City').value,
//     };
//     console.log(inputs)

//     // Send data to API
//     fetch('https://example.com/api', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//         },
//         body: JSON.stringify(inputs)
//     })
//     .then(response => response.json())
//     .then(data => {
//         // Display prediction result
//         document.getElementById('result').textContent = 'Predicted Time: ' + data.predicted_time; // Adjust according to your API response
//     })
//     .catch(error => console.error('Error:', error));
// });
