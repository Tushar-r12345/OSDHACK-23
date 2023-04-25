import json
import pickle
import numpy as np


__model1 = None
__data_columns = None
__data_columns100  = None
__crops_mapping = None


# location.lower() ki location ko lower case mein kar de
def get_predict_crops(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall):

    x = np.zeros(len(__data_columns))

    # Set the corresponding feature values in the x array
    x[0] = nitrogen
    x[1] = phosphorous
    x[2] = potassium
    x[3] = temperature
    x[4] = humidity
    x[5] = ph
    x[6] = rainfall

    # Use the trained random forest classifier model to predict the diagnosis
    prediction1 = __model1.predict([x])[0]

    # Look up the original value
    original_value1 = __crops_mapping[str(prediction1)]

    return {"Crop_suitable": original_value1}


def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns100
    global __crops_mapping
    global __data_columns

    with open("./artifacts/columns_crops.json",'r') as f:
        __data_columns=json.load(f)['data_columns']


    with open("./artifacts/inverse_mapping_crops.json",'r') as f:
        __data_columns_100 = json.load(f)
        __crops_mapping = __data_columns_100["crops"]

    global __model1

    with open("./artifacts/rfc_model_crops.pickle",'rb') as f:
        __model1 = pickle.load(f)

    print("loading saved artifacts........")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_predict_crops(18, 19, 27, 28, 53, 5.0, 95))
    print(get_predict_crops(101, 17, 47, 30, 95, 7, 27))