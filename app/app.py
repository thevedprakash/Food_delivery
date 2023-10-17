import sys
sys.path.append('src')
import joblib
import pickle
import pandas as pd
import datetime
from flask_cors import CORS
from flask import Flask, json, request, jsonify , render_template
from predict import preprocess_and_predict


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
model_path = "models/XgBoost.joblib"
model= joblib.load(model_path)


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
    print("Delivery_location_latitude : ",Delivery_location_latitude)
    Delivery_location_longitude = request.args.get('Delivery_location_longitude')
    print("Delivery_location_longitude : ",Delivery_location_longitude)
    Order_Date = request.args.get('Order_Date')
    Time_Ordered = request.args.get('Time_Ordered')
    print("Time_Ordered : ",Time_Ordered+":00")
    Time_Order_picked = request.args.get('Time_Order_picked')
    print("Time_Order_picked : ",Time_Order_picked+":00")
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
            'Restaurant_latitude': float(Restaurant_latitude),
            'Restaurant_longitude': float(Restaurant_longitude),
            'Delivery_location_latitude': float(Delivery_location_latitude),
            'Delivery_location_longitude': float(Delivery_location_longitude),
            'Order_Date': Order_Date,
            'Time_Orderd': Time_Ordered+":00",
            'Time_Order_picked': Time_Order_picked+":00",
            'Weatherconditions': Weatherconditions,
            'Road_traffic_density': Road_traffic_density,
            'Vehicle_condition': Vehicle_condition,
            'Type_of_order': Type_of_order,
            'Type_of_vehicle': Type_of_vehicle,
            'multiple_deliveries': multiple_deliveries,
            'Festival': Festival,
            'City':City,
        }
    print(data_dict)

    # Convert input recieved from webpage as dict to dataframe
    df = pd.DataFrame.from_dict([data_dict],orient='columns')

    df.to_csv('test_input.csv',index=False)
    # # Pre-process and make prediction using model loaded from disk as per the data.
    data = preprocess_and_predict(df,encoded_dict)
    # print(data)
    prediction = model.predict(data)
    return str(35.23)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)