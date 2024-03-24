#!/usr/bn/python3 
"""script that starts a Flask web application   listening on 0.0.0.0, port 5000"""

from flask import Flask;

app=Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB"""
    return 'Hello HBNB'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Display HBNB"""
    return 'HBNB'

# Define a route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    # Replace underscore symbols with a space
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

#Run flash
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)