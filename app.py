from flask import Flask, request, jsonify
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
model = joblib.load('fish_model.pkl')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Fish Species Prediction API!'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    length = float(data['length'])
    height = float(data['height'])
    width = float(data['width'])

    # Prepare the input for the model
    input_data = np.array([length, height, width]).reshape(1, -1)
    input_data_scaled = scaler.transform(input_data)

    # Make the prediction
    prediction = model.predict(input_data_scaled)

    # Define species labels (this must match the model's labels)
    species = ['Species A', 'Species B', 'Species C']  # Replace with actual species names

    return jsonify({'prediction': species[prediction[0]]})

if __name__ == '__main__':
    app.run(debug=True)
