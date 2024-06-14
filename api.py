from flask import Flask, Blueprint, request, jsonify, escape
from sentiment_model import predict_sentiment, PreprocessingError, PredictionError
import re

app = Flask(__name__)

# Trying to keep the components seperated as of now
# Blueprints allow you to turn your code into a modular component
# that can be used in other parts of the application
api = Blueprint('api', __name__)


# Change the string in test_input to test out your data validation 
test_input = "This is a test input"


# TODO: Data validation prototype function
# Requirements: 
# 1. Must not be a string
# 2. String must not be blank
# 3. String must be less than 2000 characters
# 4. Validation must remove HTML/Javascript tags and special characters
def validate_input(test): 
    if not isinstance(test, str):
        return False, "Input is not a string"
    # elif ...add more validation criteria here
        




validate_input(test_input) # Test the function







    







@app.route('/predict', methods=['POST']) # Placeholder URL route
# TODO: Implement data validation
# Validation criteria (as of now): Text input is a string that isn't blank, 
# and is less than 2000 characters. Feel free to add more validation criteria.
def prediction_api(): # Get the text from the POST request
    try:                            
        text = request.form['text'] # placeholder ID for the text input
        sentiment = predict_sentiment(text)
        return jsonify({"sentiment": sentiment})
    except PreprocessingError as ppe:
        return jsonify({"error": str(ppe)}), 400
    except PredictionError as pe:
        return jsonify({"error": str(pe)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500