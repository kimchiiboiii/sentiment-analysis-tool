from sentiment_model import predict_sentiment, PreprocessingError, PredictionError
from werkzeug.utils import escape
from flask import Flask, Blueprint, request, jsonify
import re

app = Flask(__name__)

# Trying to keep the components seperated as of now
# Blueprints allow you to turn your code into a modular component
# that can be used in other parts of the application
api = Blueprint('api', __name__)


test_input = "This is a input string"

def validate_input(input): 
    if len(input) > 2000:
        return False, "String exceeds 2000 characters"
    
    cleaned_input = re.sub(r'<.*?>', "", escape(input)) # Remove HTML/Javascript tags + Remove special characters
    if not isinstance(input, str):
        return False, "Input is not a string"
    if not input.strip():
        return False, "String is blank"
    return True, "Input is valid", cleaned_input


@app.route('/predict', methods=['POST']) # Placeholder URL route
def prediction_api(): # Get the text from the POST request
    try:                            
        text = request.form['text'] # placeholder ID for the text input
        is_valid, message, cleaned_text = validate_input(text)
        if not is_valid:
            return jsonify({"error": message}), 400

        sentiment = predict_sentiment(cleaned_text)
        return jsonify({"sentiment": sentiment})
    except PreprocessingError as ppe:
        return jsonify({"error": str(ppe)}), 400
    except PredictionError as pe:
        return jsonify({"error": str(pe)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500