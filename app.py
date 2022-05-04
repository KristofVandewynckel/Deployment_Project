from flask import Flask, render_template, request
from sympy import N
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open('model/model.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    return render_template('form.html')

@app.route('/result')
def result():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)
    entry = output
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)