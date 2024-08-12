from flask import Flask

app = Flask(__name__)


# Existing route
@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


# Existing greet route
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


# Celsius to Fahrenheit conversion function
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32


# New route for converting Celsius to Fahrenheit
@app.route('/convert/<celsius>')
def convert(celsius):
    fahrenheit = celsius_to_fahrenheit(float(celsius))
    return f"{celsius} Celsius is {fahrenheit} Fahrenheit"


if __name__ == '__main__':
    app.run(debug=True)
