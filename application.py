from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

# Load model and data
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

# Create a mapping from company to its car models
car_dict = car.groupby('company')['name'].unique().apply(list).to_dict()

@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = sorted(car['fuel_type'].unique())
    companies.insert(0, 'Select Company')
    return render_template('index.html', companies=companies, years=years, fuel_types=fuel_types)

@app.route('/get_models/<company>')
def get_models(company):
    models = car_dict.get(company, [])
    return jsonify(models)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_models')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = request.form.get('kilo_driven')

    prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                             data=np.array([car_model, company, year, driven, fuel_type]).reshape(1, 5)))

    return str(np.round(prediction[0], 2))

if __name__ == '__main__':
    app.run(debug=True)
