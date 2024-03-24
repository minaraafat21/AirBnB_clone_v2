#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB!"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display “C ” followed by the value of the text variable"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyisfun(text="is cool"):
    """display “py ” followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """display “n is a number” only if n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """return html repr of number"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def evenodd(n):
    """return html repr of number"""
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, x="even")
    if n % 2 != 0:
        return render_template('6-number_odd_or_even.html', n=n, x="odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
