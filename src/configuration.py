train_path =  "data/train.csv"

test_path = "data/test.csv"

model_path = "models/encoded.pickle"

target_column = "Time_taken(min)"

na_values =    [
                    "", 
                    "NaN ", 
                    "#N/A", 
                    "#N/A N/A", 
                    "#NA", 
                    "-1.#IND", 
                    "-1.#QNAN", 
                    "-NaN", 
                    "-nan", 
                    "1.#IND", 
                    "1.#QNAN", 
                    "<NA>", 
                    "N/A", 
                    "NA", 
                    "NULL", 
                    "NaN", 
                    "n/a", 
                    "nan", 
                    "null"
                ]

predictor_column = ['Delivery_person_Age', 'distance', 'Delivery_person_Ratings',
       'Weatherconditions', 'Road_traffic_density', 'Vehicle_condition',
       'Type_of_order', 'Type_of_vehicle', 'multiple_deliveries', 'Festival',
       'City', 'Order_prep_time']