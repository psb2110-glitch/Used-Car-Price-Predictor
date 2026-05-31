# Used Car Price Predictor

A Machine Learning web application built using Flask and Scikit-Learn that predicts the resale value of used cars based on vehicle specifications.

---

## Features

- Used Car Price Prediction
- Dynamic Brand & Model Selection
- Estimated Price Range
- Car Details Summary
- Compare Two Cars
- Responsive User Interface

---

## Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- HTML
- CSS
- Bootstrap
- JavaScript
- AJAX

---

## Project Workflow

1. User selects car details.
2. Flask receives the input.
3. Trained Machine Learning model predicts the price.
4. Estimated price range is generated.
5. Users can compare two cars based on predicted value.

---

## Features Implemented

### Price Prediction

Predicts resale value based on:

- Brand
- Model
- Year
- Fuel Type
- Kilometers Driven

### Price Range Estimation

Displays a realistic estimated range around the predicted price.

### Compare Cars

Compare two cars and view:

- Predicted prices
- Price difference
- Which vehicle is more expensive

---

## Project Structure

```text
CarPricePredictor/
│
├── application.py
├── Corrected Cardataset.csv
├── LinearRegressionModel.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
└── static/
    └── css/
        └── style.css
```

---

## How To Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python application.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Learning Outcomes

- Machine Learning Model Integration
- Flask Backend Development
- AJAX-Based Frontend Communication
- Dynamic Form Handling
- Data Processing with Pandas
- End-to-End ML Web Application Development

---

## Author

Priyanshu Sekhar Bhuyan

B.Tech Computer Science and Engineering Student
