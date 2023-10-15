function resetForm() {
    document.getElementById('deliveryForm').reset();
    document.getElementById('result').innerHTML = '';
}

document.getElementById('deliveryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const source = document.getElementById('source').value;
    const destination = document.getElementById('destination').value;
    const weight = parseFloat(document.getElementById('weight').value);
    const distance = parseFloat(document.getElementById('distance').value);
    const pickupTime = new Date(document.getElementById('pickupTime').value);
    const deliveryTime = new Date(document.getElementById('deliveryTime').value);

    // Perform the prediction logic here

    // For demo purposes, let's assume a simple calculation
    const predictedTime = distance / (weight * 0.1); 

    const result = `Predicted Time: ${predictedTime.toFixed(2)} hours`;

    document.getElementById('result').innerHTML = result;
});


document.getElementById('deliveryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Capture input values
    var inputs = {
        'ID': document.getElementById('ID').value,
        'Delivery_person_ID': document.getElementById('Delivery_person_ID').value,
        'Delivery_person_Age': parseFloat(document.getElementById('Delivery_person_Age').value),
        'Delivery_person_Ratings': parseFloat(document.getElementById('Delivery_person_Ratings').value),
        'Restaurant_latitude': parseFloat(document.getElementById('Restaurant_latitude').value),
        'Restaurant_longitude': parseFloat(document.getElementById('Restaurant_longitude').value),
        'Delivery_location_latitude': parseFloat(document.getElementById('Delivery_location_latitude').value),
        'Delivery_location_longitude': parseFloat(document.getElementById('Delivery_location_longitude').value),
        'Order_Date': document.getElementById('Order_Date').value,
        'Time_Ordered': document.getElementById('Time_Ordered').value,
        'Time_Order_picked': document.getElementById('Time_Order_picked').value,
        'Weatherconditions': document.getElementById('Weatherconditions').value,
        'Road_traffic_density': document.getElementById('Road_traffic_density').value,
        'Vehicle_condition': parseInt(document.getElementById('Vehicle_condition').value),
        'Type_of_order': document.getElementById('Type_of_order').value,
        'Type_of_vehicle': document.getElementById('Type_of_vehicle').value,
        'multiple_deliveries': parseFloat(document.getElementById('multiple_deliveries').value),
        'Festival': document.getElementById('Festival').value,
        'City': document.getElementById('City').value,
        'Time_taken(min)': document.getElementById('Time_taken').value
    };

    // Send data to API
    fetch('https://example.com/api', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(inputs)
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        document.getElementById('result').textContent = 'Predicted Time: ' + data.predicted_time; // Adjust according to your API response
    })
    .catch(error => console.error('Error:', error));
});