import json
import pickle
import numpy as np


__model1 = None
__data_columns102  = None
__region = None
__crop_name = None

# location.lower() ki location ko lower case mein kar de
def predict_crop_price(state, region, market,  crop_name, day, month):
    # Initialize x array with zeros of length equal to number of columns in X
    try:
        loc_index1 = __data_columns102.index(state.lower())
        loc_index2 = __data_columns102.index(region.lower())
        loc_index3 = __data_columns102.index(market.lower())
        loc_index4 = __data_columns102.index(crop_name.lower())

    except:
        loc_index1=-1
        loc_index2=-1

    x = np.zeros(len(__data_columns102))

    # Set the corresponding feature values in the x array
    x[0] = day
    x[1] = month

    # Set the values of the Cardiac_CT and Previous_illnesses features to 1
    if loc_index1 > 0:
        x[loc_index1] = 1
    if loc_index2 > 0:
        x[loc_index2] = 1

    # Use the trained random forest classifier model to predict the diagnosis
    prediction2 = round(__model2.predict([x])[0],2)

    return {"Price estimated": prediction2}

def get_region():
    return __region

def get_crop_name():
    return __crop_name

def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns102
    global __region
    global __crop_name

    with open("./artifacts/columns_crops_price_new_new1.json",'r') as f:
        __data_columns102=json.load(f)['data_columns']
        __region = __data_columns102[2:8]
        __crop_name = __data_columns102[9:]


    global __model2

    with open("./artifacts/rfc_model_crops_price_new_new1.pickle",'rb') as f:
        __model2 = pickle.load(f)
    # print(predict_crop_price('Surat - Gujarat - (Western)', 'Banana', 14, 7))
    print("loading saved artifacts........")

if __name__=='__main__':
    load_saved_artifacts()
    print(get_crop_name())
    print(get_region())
    print(predict_crop_price('hyderabad - telangana - (southern)','coconut',5,7))
    print(predict_crop_price('Sonipat - Haryana - (Northern)','Apple',14,7))
    print(predict_crop_price('Surat - Gujarat - (Western)','Banana',14,7))
    print(predict_crop_price('Surat - Gujarat - (Western)', 'Mango', 14, 7))