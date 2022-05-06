from flask import Flask, render_template, request
import pickle
import numpy as np
import math

app = Flask(__name__)

model = pickle.load(open('model/model.pickle', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    return render_template('form.html')

@app.route('/result', methods=['GET','POST'])
def result():
    bedrooms = request.form.get("Rooms", type=int)
    liv_area = request.form.get("Living Area", type=int)
    surface_area = request.form.get("Surface Land Area", type=int)
    subtype = request.form.get("Type")
    house = 0
    villa = 0
    farmhouse = 0
    mansion = 0
    mixed_use = 0
    if subtype == "House":
        house = 1
    elif subtype == "Villa":
        villa = 1
    elif subtype == "Farmhouse":
        farmhouse = 1
    elif subtype == "Mansion":
        mansion = 1
    elif subtype == "Mixed_use":
        mixed_use = 1

    kitchen = request.form.get("Kitchen Equipped?")
    if kitchen == "Yes":
        kitchen = 1
    else:
        kitchen = 0
    fireplace = request.form.get("Open fireplace")
    if fireplace == "Yes":
        fireplace = 1
    else:
        fireplace = 0  
    terrace = request.form.get("Terrace")
    if terrace == "Yes":
        terrace = 1
    else:
        terrace = 0  
    garden = request.form.get("Garden")
    if garden == "Yes":
        garden = 1
    else:
        garden = 0   
    pool = request.form.get("Pool")
    if pool== "Yes":
        pool = 1
    else:
        pool = 0  
    condition = request.form.get("Condition")
    if condition == "To be renovated":
        condition = 1
    else:
        condition = 0
    
    request_values = [bedrooms,liv_area,surface_area,farmhouse, house, mansion, mixed_use, villa, kitchen,fireplace,terrace,garden,pool,condition]
    int_features = [int(x) for x in request_values]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = int(math.ceil(prediction / 1000)) *1000
    entry = output
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)