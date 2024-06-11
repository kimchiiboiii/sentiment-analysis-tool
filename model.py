import pickle
import tensorflow as tf
from flask import jsonify
from tensorflow.keras.preprocessing.sequence import pad_sequences

class PreprocessingError(Exception):
    # Custom exception class for preprocessing errors
    # Type errors and value errors with the input data etc.
    pass
class PredictionError(Exception):
    # Custom exception class for prediction errors
    # TensorFlow errors, model not loaded, etc.
    pass


# Load the model
model = tf.keras.models.load_model("put_model_here.h5")

# Load the tokenizer
with open("path_to_tokenizer.pickle", "rb") as handle:
    tokenizer = pickle.load(handle)


def preprocess_text(text):
    try:
        # Implement preprocessing here
        # Tokenize, pad, etc.
        sequences = tokenizer.texts_to_sequences(text)
        preprocessed_text = pad_sequences(sequences, maxlen=100)
        return preprocessed_text
    except ValueError as ve:
        raise PreprocessingError("ValueError: " + str(ve))

def interpret_prediction(prediction):
    try:
        # Implement interpretation here
        # Control flow based on how the model scores sentiment
        # e.g. if score > 0.5, positive statement, if score < 0.5, negative, etc.
        sentiment = "positive" if prediction > 0.5 else "negative"
        return sentiment
    except TypeError as te:
        raise Exception("TypeError: " + str(te))
    except Exception as e:
        raise Exception("error: " + str(e))
    

def predict_sentiment(text):
    # Function that is callled by the API
    try:
        preprocessed_text = preprocess_text(text)
        prediction = model.predict(preprocessed_text)
        sentiment = interpret_prediction(prediction)
        return sentiment
    except ValueError as ve:
        raise PreprocessingError("ValueError: " + str(ve))
    except tf.errors.OpError as oe:
        raise PredictionError("TensorFlow error: " + str(oe))
    except Exception as e:
        raise Exception(str(e))