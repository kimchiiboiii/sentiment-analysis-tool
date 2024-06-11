from flask import Flask
from flask_cors import CORS
from api import api

# Entry point for the app that sets up and configures the server


app = Flask(__name__)
CORS(app) # Middleware that will allow the React app to make requests to the Flask app

# Loads the blueprint from api.py and registers it with the app
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=True)
