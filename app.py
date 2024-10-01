# Required Libraries for Flask API
from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (best_model.pkl) when the app starts
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    # Render the HTML form
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get the form data from the request
    calories = float(request.form['calories'])
    protein = float(request.form['protein'])
    fat = float(request.form['fat'])
    sodium = float(request.form['sodium'])

    # Prepare the data for the model
    input_data = np.array([calories, protein, fat, sodium]).reshape(1, -1)

    # Make a prediction using the model
    prediction = model.predict(input_data)

    # Return the index.html with the predicted rating
    return render_template("index.html", rating=prediction[0])

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
