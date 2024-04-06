#!/usr/bin/python3
"""This script defines a simple Flask web application
that listens on 0.0.0.0, port 5000."""
from flask import Flask

# Create a Flask application instance
app = Flask(__name__)


# Define a route for the home page
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
