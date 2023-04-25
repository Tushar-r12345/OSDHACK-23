from flask import Flask, request, jsonify
from flask_cors import CORS
import util
import util2

app = Flask(__name__)
CORS(app)


@app.route('/get_region', methods=['GET'])
def get_region():
    response = jsonify({
        'region': util2.get_region()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_crop_name', methods=['GET'])
def get_crop_name():
    response = jsonify({
        'crop_name': util2.get_crop_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/get_predict_crop_price', methods=['POST'])
# def get_predict_crop_price():
#     # Set the corresponding feature values in the x array
#     region = request.form['region']
#     crop_name = request.form['crop_name']
#     day = request.form['day']  # convert to str
#     month = request.form['month']  # convert to str
#
#     # Use the trained random forest classifier model to predict the diagnosis
#     response = jsonify({
#         'predicted_crop_price': util2.predict_crop_price(region, crop_name, day, month)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


import json

@app.route('/get_predict_crop_price', methods=['POST'])
def get_predict_crop_price():
    # Set the corresponding feature values in the x array
    region_d = request.form['region_d']
    crop_name_d = request.form['crop_name_d']
    day_d = float(request.form['day_d'])  # convert to integer
    month_d = float(request.form['month_d'])  # convert to integer

    # Use the trained random forest classifier model to predict the crop price
    predicted_crop_price = util2.predict_crop_price(region_d, crop_name_d, day_d, month_d)

    # Convert the prediction to a JSON serializable format
    prediction_json = json.dumps({'predicted_crop_price': predicted_crop_price})

    # Create the response with the serialized prediction
    response = app.response_class(
        response=prediction_json,
        status=200,
        mimetype='application/json'
    )

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("starting server......")
    util.load_saved_artifacts()
    util2.load_saved_artifacts()
    app.run()
