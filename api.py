from sentiment_model import predict_sentiment, PreprocessingError, PredictionError
from werkzeug.utils import escape
from flask import Flask, Blueprint, request, jsonify
import re

app = Flask(__name__)

# Trying to keep the components seperated as of now
# Blueprints allow you to turn your code into a modular component
# that can be used in other parts of the application
api = Blueprint('api', __name__)


# Change the string in test_input to test out your data validation 
test_input = "This is a test string"

def validate_input(test): 
    if len(test) > 2000:
        return False, "String exceeds 2000 characters"
    
    test = re.sub(r'<.*?>', "", escape(test)) # Remove HTML/Javascript tags + Remove special characters (escape)
    
    if not isinstance(test, str):
        return False, "Input is not a string"
    if not test.strip():
        return False, "String is blank"
    return True, "Input is valid", print(test)


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