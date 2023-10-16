import json
import pickle
import joblib
from load_data import load_data 
from prepare_data import prepare_data
from configuration import predictor_column

def decode_predict_input(df,encoded_dict):
    '''
    This function decodes categorical values with same values as done training encoded values.
    Input:
        df : DataFrame
        encoded_dict : Category encoded dictionary
    returns :None
    '''
    #Processing Ordinal Columns    
    road_trafic_density_dict= encoded_dict['ordinal_dict']['road_trafic_density_dict']
    df['Road_traffic_density'] = df['Road_traffic_density'].apply(lambda x: road_trafic_density_dict[x])
    festival_dict = encoded_dict['ordinal_dict']['festival_dict']
    df['Festival'] = df['Festival'].apply(lambda x: festival_dict[x])
    city_dict = encoded_dict['ordinal_dict']['city_dict']
    df['City'] = df['City'].apply(lambda x: city_dict[x])

    #Processing Nominal Columns
    weather_conditions_dict = encoded_dict['nominal_dict']['weather_conditions_dict']
    df['Weatherconditions'] = df['Weatherconditions'].apply(lambda x: weather_conditions_dict[x])
    type_of_order_dict = encoded_dict['nominal_dict']['type_of_order_dict']
    df['Type_of_order'] = df['Type_of_order'].apply(lambda x: type_of_order_dict[x])
    type_of_vehicle_dict = encoded_dict['nominal_dict']['type_of_vehicle_dict']
    df['Type_of_vehicle'] = df['Type_of_vehicle'].apply(lambda x: type_of_vehicle_dict[x])
  
def preprocess_and_predict(df,encoded_dict):
    '''
      This function takes in new dataframe or row of observation and generate all features
    Input :
        df : DataFrame or row of observation
        encoded_dict : Dictonary created while training for Categorical Encoded Value.
    '''
    prepare_data(df)
    decode_predict_input(df,encoded_dict)
    X = df[predictor_column]
    return X

if __name__ == "__main__":
     
    # reading configuration from config file.
    with open ("config.json",'r') as file:
        config = json.load(file)
    train = config["test_path"]
    na_values = config["na_values"]
    model_path = config["model_path"]
    target_column = config["target_column"]

    with open('models/encoded.pickle', 'rb') as handle:
        encoded_dict = pickle.load(handle)
    
    model_path = 'models/XgBoost.joblib'
    saved_model= joblib.load(model_path)

    # Reading Train data
    df = load_data(train,na_values)
    test_input = preprocess_and_predict(df,encoded_dict)
    print(test_input.head())
    saved_model.predict(test_input.iloc[0:5,:])
    print(saved_model.predict(test_input.iloc[0:5,:]))