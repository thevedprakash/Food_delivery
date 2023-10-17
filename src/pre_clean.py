import pandas as pd
import numpy as np
from configuration import *
from datetime import timedelta


def pre_cleanup(df):
    '''
    This function is to process Weather conditions column.
    params:
        df : Dataframe to be processed
    return: 
        Processed Dataframe
    '''
    df.replace(" ","",regex=True,inplace=True)
    df['Weatherconditions'] = df['Weatherconditions'].apply(lambda x : x.replace("conditions","") if "conditions" in x else x)
    if 'Time_taken(min)' in df.columns:
        df['Time_taken(min)'] = df['Time_taken(min)'].apply(lambda x : x.replace("(min)","") if "(min)" in x else x).astype(int)  
    return df


def check_category(df):
    category_cols = df.describe(include='O').columns
    for col in category_cols:
        print(df[col].value_counts())
        print(df[col].unique())


def fix_datatype(df,
                 integer_column=integer_column,
                 float_column=float_column,
                 category_column=category_column,
                 datetime_column=datetime_column,
                 time_column=time_column):
  '''
  This function is to fix datatypes before any Data cleaning process. 
  This doesn't changes or delete any np.nan values in data.
  params:
      df : Dataframe to be processed
      integer_column: list of columns to be converted into or supposed to be interger.
      float_column: list of columns to be converted into or supposed to be float.
      category_column: list of columns to be converted into or supposed to be object or category.
      datetime_column: list of columns to be converted into or supposed to be date.
      time_column: list of columns to be converted into or supposed to be time.
  '''
  print(" columns in fix_datatypes: ",df.columns)
  for col in category_column:
    print(col)
    df[col].fillna('-99999999',inplace=True)
    df[col] = df[col].astype(str)
    df[col] = df[col].replace('-99999999', np.nan)

  for col in integer_column:
    df[col].fillna(99999999,inplace=True)
    df[col] = df[col].astype(int)
    df[col] = df[col].replace(99999999, np.nan)

  for col in float_column:
    df[col].fillna(-99999999.00,inplace=True)
    df[col] = df[col].astype(float)
    df[col] = df[col].replace(-99999999.00, np.nan)

  for col in datetime_column:
    df[col] = pd.to_datetime(df[col],format='mixed')

  for col in time_column:
    df[col] = pd.to_timedelta(df[col])