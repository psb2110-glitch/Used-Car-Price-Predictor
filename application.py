from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv("Corrected Cardataset.csv")


@app.route('/')
def index():
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    return render_template(
        'index.html',
        companies=companies,
        car_models=car_models,
        years=years,
        fuel_types=fuel_types
    )


@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = int(request.form.get('year'))
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kilo_driven'))

    prediction = model.predict(pd.DataFrame(
        [[car_model, company, year, kms_driven, fuel_type]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    ))

    price = round(prediction[0])
    lower_price = round(price * 0.90)
    upper_price = round(price * 1.10)

    return {
        "price": "{:,.0f}".format(price),
        "lower_price": "{:,.0f}".format(lower_price),
        "upper_price": "{:,.0f}".format(upper_price),
        "company": company,
        "car_model": car_model,
        "year": year,
        "fuel_type": fuel_type,
        "kms_driven": "{:,}".format(kms_driven)
    }


@app.route('/compare', methods=['POST'])
def compare():
    company1 = request.form.get('company1')
    car_model1 = request.form.get('car_model1')
    year1 = int(request.form.get('year1'))
    fuel_type1 = request.form.get('fuel_type1')
    kms_driven1 = int(request.form.get('kilo_driven1'))

    company2 = request.form.get('company2')
    car_model2 = request.form.get('car_model2')
    year2 = int(request.form.get('year2'))
    fuel_type2 = request.form.get('fuel_type2')
    kms_driven2 = int(request.form.get('kilo_driven2'))

    price1 = model.predict(pd.DataFrame(
        [[car_model1, company1, year1, kms_driven1, fuel_type1]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    ))[0]

    price2 = model.predict(pd.DataFrame(
        [[car_model2, company2, year2, kms_driven2, fuel_type2]],
        columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
    ))[0]

    difference = abs(price1 - price2)

    if price1 > price2:
        message = f"{car_model1} is more expensive than {car_model2}"
    elif price2 > price1:
        message = f"{car_model2} is more expensive than {car_model1}"
    else:
        message = "Both cars have almost the same predicted price"

    return {
        "car1": car_model1,
        "car2": car_model2,
        "price1": "{:,.0f}".format(price1),
        "price2": "{:,.0f}".format(price2),
        "difference": "{:,.0f}".format(difference),
        "message": message
    }


if __name__ == "__main__":
    app.run(debug=True)