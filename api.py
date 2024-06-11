from flask import Flask, Blueprint, render_template, request, jsonify
from model import predict_sentiment, PreprocessingError, PredictionError

app = Flask(__name__)

# Trying to keep the components seperated as of now
# Blueprints allow you to turn your code into a modular component
# that can be used in other parts of the application
api = Blueprint('api', __name__)

@app.route('/predict', methods=['POST']) # Placeholder URL route
def prediction_api():
    try:
        text = request.form['text']
        sentiment = predict_sentiment(text)
        return render_template('result.html', sentiment=sentiment)
    except PreprocessingError as ppe:
        return jsonify({"error": str(ppe)}), 400
    except PredictionError as pe:
        return jsonify({"error": str(pe)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500