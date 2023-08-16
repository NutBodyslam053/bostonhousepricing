import pickle
from flask import Flask, request, app, jsonify, render_template
import numpy as np
import pandas as pd

app=Flask(__name__)

# load the model
regmodel=pickle.load(open('regmodel.pkl', 'rb'))
scaler=pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')  # Home page
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])  # API
def predict_api():
    data = request.json['data']
    print("Raw Data:", data)
    print("Data:", np.array(list(data.values())).reshape(1,-1))
    data_transformed = scaler.transform(np.array(list(data.values())).reshape(1,-1))
    print("Tranformed Data:", data_transformed)
    output = regmodel.predict(data_transformed)
    print("Output:", output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])  # Web-UI
def predict():
    data = [float(x) for x in request.form.values()]
    print("Input Data:", data)
    data_transformed = scaler.transform(np.array(data).reshape(1,-1))
    print("Tranformed Data:", data_transformed)
    output = regmodel.predict(data_transformed)[0]
    print("Output:", output)
    return render_template("home.html", prediction_text="The House Price prediction is {}".format(output))


if __name__=="__main__":
    app.run(debug=True)