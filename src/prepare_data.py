import numpy as np
import pandas as pd
from datetime import timedelta
from math import sin, cos, sqrt, atan2, radians
from configuration import *
from pre_clean import pre_cleanup, fix_datatype, check_category


def func_distance(lat1,lon1,lat2,lon2):
    '''
    This function calculates distance between two geographical coordinates.
    params:
        lat1: latitude of first location,
        lon1: longitude of first location,
        lat2: latitude of second location,
        lon2: longitude of second location
    returns:
        distance
    '''
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = format(R * c,'.2f')
    return float(distance)


def calculate_distance(df):
    '''
    This function is to calculate the distance between longitude and latitude.
    params:
        df : Dataframe to be processed
    return:
        Numpy array of caluclated Distance
    '''
    df['distance'] = df.apply(lambda df: func_distance(df['Restaurant_latitude'],df['Restaurant_longitude'],
                                                    df['Delivery_location_latitude'],df['Delivery_location_longitude']),axis=1)
    return df


def create_orderprep_time(df):
    '''
    This function is to process timestamp columns from data for model building.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    def func_nextday(x,y):
        if x > y:
            y = y + timedelta(days=1)
        return y

    df['Time_Order_picked'] = pd.to_timedelta(df.apply(lambda x: func_nextday(x['Time_Orderd'],x['Time_Order_picked']), axis=1))
    '''
    bug fix : Fix this to handle properly.
    Error:
        numpy.core._exceptions._UFuncBinaryResolutionError: 
        ufunc 'add' cannot use operands with types dtype('<m8[ns]') and dtype('float64')
    ```
    print("df['Time_Order_picked'] dtype: ",df['Time_Order_picked'].dtype)
    print("df['Time_Orderd'] dtype: ",df['Time_Orderd'].dtype)
    df['Time_Order_picked'] dtype:  float64
    df['Time_Orderd'] dtype:  timedelta64[ns]
    ```
    changing df['Time_Order_picked'] datatype to timedelta.
        df['Time_Order_picked'] = pd.to_timedelta(df['Time_Order_picked'], errors='coerce')
    '''
    df['Order_prep_time'] = ((df['Time_Order_picked'] - df['Time_Orderd']).dt.total_seconds())/60
    return df


def drop_columns(df):
    '''
    This function is to remove unwanted columns from data for model building.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    # Dropping after processing calculate_distance.
    df.drop(['Restaurant_latitude', 'Restaurant_longitude',
        'Delivery_location_latitude', 'Delivery_location_longitude'],axis = 1,inplace = True)
    df.drop(['ID','Delivery_person_ID','Order_Date'],axis = 1, inplace = True)
    df.drop(['Time_Orderd','Time_Order_picked'],axis = 1, inplace = True)
    return df


def handle_missing_value(df):
    '''
    This function is to handles missing values in  data.
    '''
    df.dropna(inplace = True)
    return df


def prepare_data(df):
    '''
    This function is to prepare data for model building.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    pre_cleanup(df)
    fix_datatype(df)
    print(" After datatype fix: ",df.info())
    handle_missing_value(df)

    calculate_distance(df)
    print(df)
    create_orderprep_time(df)
    print(" Order Prep time creation: ",df)
    drop_columns(df)
    check_category(df)
    return df
