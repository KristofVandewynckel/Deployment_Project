from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/predict")
def predict():
    Area = request.form.get("Area", type=int)
    Type = request.form.get("Property Type", type=int)
    Rooms = request.form.get("Number of rooms", type=int)
    Zip = request.form.get("Zip Code", type=int)

    entry = "Hello"
    return render_template('form.html')

@app.route("/result")
def result():
    entry = "Simsalabim"
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)