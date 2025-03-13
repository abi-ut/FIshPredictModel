from flask import Flask, render_template, request
import numpy as np
import joblib
import os

# Load the trained model and scaler
model = joblib.load('fish_model.pkl')
scaler = joblib.load('scaler.pkl')

app = Flask(__name__)

# Serve the HTML page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get form inputs
            weight = float(request.form["Weight"])
            length1 = float(request.form["Length1"])
            length2 = float(request.form["Length2"])
            length3 = float(request.form["Length3"])
            height = float(request.form["Height"])
            width = float(request.form["Width"])

            # Prepare the input data and scale it
            input_data = np.array([[weight, length1, length2, length3, height, width]])
            scaled_input = scaler.transform(input_data)

            # Make the prediction
            prediction = model.predict(scaled_input)[0]  # prediction is a species name, not an integer

            # Species labels (Update these to match your dataset)
            species = ["Bream", "Roach", "Whitefish", "Parkki", "Perch", "Pike", "Smelt"]

            # Return the prediction
            return render_template("index.html", prediction=prediction)

        except Exception as e:
            return f"Error: {str(e)}"

    return render_template("index.html", prediction=None)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the PORT from Heroku's environment
    app.run(host="0.0.0.0", port=port, debug=True)  # Bind to 0.0.0.0

