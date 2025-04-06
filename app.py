import pandas as pd
import numpy as np
from flask import Flask, request, render_template
import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler

app = Flask(__name__)

# Load dataset to fit transformers (remove unnecessary columns)
df = pd.read_csv("Churn_Modelling.csv")
df.drop(columns=['RowNumber', 'CustomerId', 'Surname', 'Exited'], inplace=True)

# Define categorical and numerical columns
numerical_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
categorical_columns = ['Geography', 'Gender']

# Fit One-Hot Encoder and Standard Scaler on the full dataset
encoder = OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')
scaler = StandardScaler()

df_encoded = encoder.fit_transform(df[categorical_columns])
df_scaled = scaler.fit_transform(df[numerical_columns])

@app.route("/")
def load_page():
    return render_template('home.html')

@app.route("/", methods=['POST'])
def predict():
    try:
        # Capture user input
        input_data = {
            'CreditScore': [float(request.form['query1'])],
            'Geography': [request.form['query2']],
            'Gender': [request.form['query3']],
            'Age': [float(request.form['query4'])],
            'Tenure': [int(request.form['query5'])],
            'Balance': [float(request.form['query6'])],
            'NumOfProducts': [int(request.form['query7'])],
            'HasCrCard': [int(request.form['query8'])],
            'IsActiveMember': [int(request.form['query9'])],
            'EstimatedSalary': [float(request.form['query10'])]
        }

        # Convert to DataFrame
        new_df = pd.DataFrame(input_data)

        # Apply One-Hot Encoding using the pre-trained encoder
        encoded_categorical = encoder.transform(new_df[categorical_columns])

        # Apply Standard Scaling using the pre-trained scaler
        scaled_numerical = scaler.transform(new_df[numerical_columns])

        # Combine processed numerical & categorical features
        final_input = np.hstack((scaled_numerical, encoded_categorical))

        # Load trained XGBoost model
        model = joblib.load("classifier_model.pkl")

        # Predict churn & probability
        prediction = model.predict(final_input)
        probability = model.predict_proba(final_input)[:, 1]

        # Output results
        if prediction == 1:
            result = "This customer is likely to churn!"
        else:
            result = "This customer is likely to continue!"

        #confidence = f"Confidence: {probability[0] * 100:.2f}%"

        return render_template('home.html', output1=result, **request.form)

    except Exception as e:
        return f"Error occurred! {e}"

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
