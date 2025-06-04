# AutoValuator 🚗

AutoValuator is a Flask-based web application that predicts the resale price of a used car based on user input. It uses a machine learning model trained on real-world data scraped from PakWheels.

## 🔧 Features

* Predicts car resale value in PKR
* Clean UI with dropdowns for car brand, model, year, fuel type, and kilometers driven
* Instant prediction with no page reloads
* Backed by an XGBoost regression model

## 🗂️ Project Structure

```
.
├── auto-price-app.py              # Main Flask app
├── pakwheels\_Cleaned\_Car\_data.csv # Cleaned dataset
├── XGBoostModel.pkl               # Trained ML model
├── static/
│   └── css/
│       └── style.css              # Custom styling
├── templates/
│   └── index.html                 # Web interface
```

##     How to Run

1. Clone the repository
2. Create a virtual environment and activate it
3. Run:
   \\\
   pip install -r requirements.txt
   python auto-price-app.py
   \\\
4. Open browser at: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## 🧠 Model

The model is trained using XGBoost on features such as:

* Car company
* Model name
* Year of purchase
* Kilometers driven
* Fuel type

## 📷 Screenshot

![image](https://github.com/user-attachments/assets/1bbf43bc-bc85-44fa-9f03-a72909ea1a27)


## Jupyter Notebook

To explore the machine learning workflow, feature selection, preprocessing, model training, and evaluation, refer to the notebook:

▶️ [Car_price.ipynb](Car_price.ipynb)



## 

Developed by Muhammad Ali Asjad — feel free to contribute or reach out for suggestions!


