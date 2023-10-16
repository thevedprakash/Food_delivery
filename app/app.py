import sys
sys.path.append('src')
import joblib
import pickle
import pandas as pd
from flask_cors import CORS
from flask import Flask, json, request, jsonify , render_template
from werkzeug.utils import secure_filename
from predict import preprocess_and_predict
from variables import airlines, sources, destinations, routes


# This will enable CORS for all routes
'''
Cross-origin resource sharing (CORS) is a browser security feature 
that restricts cross-origin HTTP requests that are initiated from scripts running in the browser.
'''
app = Flask(__name__)
CORS(app) 

# Load data (deserialize)
with open('models/encoded.pickle', 'rb') as handle:
    encoded_dict = pickle.load(handle)
model_path = "models/XgBoost.pickle"
model= joblib.load(model_path)


@app.route('/api', methods=['POST','GET'])
def predict():
    # Get the data from the POST request.
    json_data = request.get_json(force=True)

    # Convert json data to dataframe
    df = pd.DataFrame.from_dict(pd.json_normalize(json_data), orient='columns')

    # Pre-process and make prediction using model loaded from disk as per the data.
    data = preprocess_and_predict(df,encoded_dict)

    # Predict with Model
    prediction = model.predict(data)

    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)


@app.route("/prediction")
def prediction():
    # get inputs from webpage
    ID = request.args.get('ID')
    Delivery_person_ID = request.args.get('Delivery_person_ID')
    Delivery_person_Age = request.args.get('Delivery_person_Age')
    Delivery_person_Ratings = request.args.get('Delivery_person_Ratings')
    Restaurant_latitude = request.args.get('Restaurant_latitude')
    Restaurant_longitude = request.args.get('Restaurant_longitude')
    Delivery_location_latitude = request.args.get('Delivery_location_latitude')
    Delivery_location_longitude = request.args.get('Delivery_location_longitude')
    Order_Date = request.args.get('Order_Date')
    Time_Ordered = request.args.get('Time_Ordered')
    Time_Order_picked = request.args.get('Time_Order_picked')
    Weatherconditions = request.args.get('Weatherconditions')
    Road_traffic_density = request.args.get('Road_traffic_density')
    Vehicle_condition = request.args.get('Vehicle_condition')
    Type_of_order = request.args.get('Type_of_order')
    Type_of_vehicle = request.args.get('Type_of_vehicle')
    multiple_deliveries = request.args.get('multiple_deliveries')
    Festival = request.args.get('Festival')
    City = request.args.get('City')
    data_dict = {
            'ID': ID,
            'Delivery_person_ID': Delivery_person_ID,
            'Delivery_person_Age': Delivery_person_Age,
            'Delivery_person_Ratings': Delivery_person_Ratings,
            'Restaurant_latitude': Restaurant_latitude,
            'Restaurant_longitude': Restaurant_longitude,
            'Delivery_location_latitude': Delivery_location_latitude,
            'Delivery_location_latitude': Delivery_location_longitude,
            'Order_Date': Order_Date,
            'Time_Ordered': Time_Ordered,
            'Time_Order_picked': Time_Order_picked,
            'Weatherconditions': Weatherconditions,
            'Road_traffic_density': Road_traffic_density,
            'Vehicle_condition': Vehicle_condition,
            'Type_of_order': Type_of_order,
            'Type_of_vehicle': Type_of_vehicle,
            'multiple_deliveries': multiple_deliveries,
            'Festival': Festival,
            'City':City,
        }
    
    # Convert input recieved from webpage as dict to dataframe
    df = pd.DataFrame.from_dict([data_dict],orient='columns')

    # Pre-process and make prediction using model loaded from disk as per the data.
    data = preprocess_and_predict(df,encoded_dict)
    prediction = model.predict(data)
    return str(prediction[0])


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)