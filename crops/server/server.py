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


@app.route('/predict_crops', methods=['POST'])
def predict_crops():
    # Set the corresponding feature values in the x array
    nitrogen = request.form['nitrogen']
    phosphorous = request.form['phosphorous']
    potassium = request.form['potassium']
    temperature = request.form['temperature']
    humidity = request.form['humidity']
    ph = request.form['ph']
    rainfall = request.form['rainfall']

    # Use the trained random forest classifier model to predict the diagnosis
    response = jsonify({
        'predicted_crop': util.get_predict_crops(nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/get_predict_crop_price', methods=['POST'])
# def get_predict_crop_price():
#     # Set the corresponding feature values in the x array
#     region = request.form['region']
#     crop_name = request.form['crop_name']
#     day = float(request.form['day'])
#     month = float(request.form['month'])
#
#     # Use the trained random forest classifier model to predict the diagnosis
#     response = jsonify({
#         'predicted_crop_price': util2.predict_crop_price(region, crop_name, day, month)
#     })
#
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


if __name__ == "__main__":
    print("starting server......")
    util.load_saved_artifacts()
    util2.load_saved_artifacts()
    app.run()
