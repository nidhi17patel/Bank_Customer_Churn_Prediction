<div style="background-color: #4A235A;
            color: #FFFFFF;
            text-align: center;
            border: 3px solid #2980B9;
            border-radius: 15px;
            box-shadow: 0px 4px 8px rgba(0, 0, 255, 0.4);
            font-family: 'Arial Black', Gadget, sans-serif;
            font-size: 12px;
            text-transform: uppercase;
            font-style: italic;
            width: 850px;
            margin: left;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 50px; /* Set a fixed height */
            padding: 0;">
    <h1 style="margin: 0;">🔍 🔮 Bank Customer Churn Prediction</h1>
</div>










In this repository, we have performed the end to end Exploratory Data Analysis, and idenfitied the characteristics of the customers that are more likely to churn, and I have used them wisely to create a model, and lately, have deployed the model.

<div style="border-radius:10px; border:#808080 solid; padding: 15px; background-color: ##F0E68C ; font-size:100%; text-align:left">

<h3 align="left"><font color=brown>📊 Business Objective:</font></h3>
   
- The goal would be to identify which customers are most likely to churn (leave the service) and understand the key factors driving their decision to leave. `Churn Reduction through Predictive Analytics`
- Churn refers to the process by which a customer stops doing business with a company.

<h3 align="left"><font color=brown>📊 Business Value:</font></h3>
- Customer retention is critical for a bank’s profitability. Predicting which customers are likely to churn can help the bank take proactive steps (e.g., offering personalized services or incentives) to retain valuable customers.

### Description:

This dataset contains information about bank customers and their churn status, indicating whether they have exited the bank or not. It is suitable for exploring and analyzing factors influencing customer churn in banking institutions and for building predictive models to identify customers at risk of churning.

### Features:

- **RowNumber:**    The sequential number assigned to each row in the dataset.
- **CustomerId:**   A unique identifier for each customer.
- **Surname:**  The surname of the customer.
- **CreditScore:**  The credit score of the customer.
- **Geography:**    The geographical location of the customer (e.g., country or region).
- **Gender:**   The gender of the customer.
- **Age:**  The age of the customer.
- **Tenure:**   The number of years the customer has been with the bank.
- **Balance:**  The account balance of the customer.
- **NumOfProducts:**    The number of bank products the customer has.
- **HasCrCard:**    Indicates whether the customer has a credit card (binary: yes/no).
- **IsActiveMember:**   Indicates whether the customer is an active member (binary: yes/no).
- **EstimatedSalary:**  The estimated salary of the customer.
- **Exited:**   Indicates whether the customer has exited the bank (binary: yes/no).

### 🟢 For EDA and Model Building, please refer to : Banking_Churn_Prediction.ipynb
### 🟢 For Model Deployment, please refer to app.py
### 🔵 Creating the flask API

```
app = Flask("__name__")
```

The loadPage method calls our home.html.
```
@app.route("/")
def loadPage():
	return render_template('home.html', query="")
```

The predict method is our POST method, which is basically called when we pass all the inputs from our front end and click SUBMIT.
```
@app.route("/", methods=['POST'])
def predict():
```
  
The run() method of Flask class runs the application on the local development server.
```
app.run()
```


Yay, our model is ready, let’s test our bot.
The above given Python script is executed from Python shell.

Go to Anaconda Prompt, and run the below query.
```
python app.py
```


Below message in Python shell is seen, which indicates that our App is now hosted at http://127.0.0.1:5000/ or localhost:5000
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```
