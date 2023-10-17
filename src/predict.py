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
    print(" type_of_order_dict:",type_of_order_dict)
    df['Type_of_order'] = df['Type_of_order'].apply(lambda x: type_of_order_dict[x])
    type_of_vehicle_dict = encoded_dict['nominal_dict']['type_of_vehicle_dict']
    print(" type_of_order_dict:",type_of_vehicle_dict)
    df['Type_of_vehicle'] = df['Type_of_vehicle'].apply(lambda x: type_of_vehicle_dict[x])


    print(df)
  
def preprocess_and_predict(df,encoded_dict):
    '''
      This function takes in new dataframe or row of observation and generate all features
    Input :
        df : DataFrame or row of observation
        encoded_dict : Dictonary created while training for Categorical Encoded Value.
    '''
    prepare_data(df)
    print(" preprocess and predict:",df.info)
    decode_predict_input(df,encoded_dict)
    X = df[predictor_column]
    return X

