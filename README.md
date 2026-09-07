# Customer Churn Prediction

##  Project Overview
Customer Churn Prediction is a Machine Learning project which aims to predict likelihood of customer churning from a company or services. 
The project fundamentally applies customer related information and a trained Machine Learning model to classify the customers into two categories:

- *0 → Customer will stay*
If the number is 1 or less, then the customer's likely to leave the company.
It's a project that will show you the whole ML lifecycle: data-prep, model training and model deployment.

##  Objective
The primary goal of this project is to enable businesses to determine which customers are likely to leave. Early indications of customer churn can enable companies to take proactive measures to improve customer retention.

##  Features
Using machine learning methods to predict customer churn.Prediction of customer churn using machine learning.
- Pre-trained Machine Learning model
- Automatic data backup and secure storage.- User-friendly user interface.
- Real-time prediction
The Streamlit library can be used to deploy models.Model deployment can be done through Streamlit.
- Easy-to-use prediction system

##  Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Google Colab
- GitHub

##  Project Structure
```text
Customer-Churn-Prediction/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md

Dataset
The project uses the Churn Modelling dataset, which contains customer information used to train the Machine Learning model.
The model uses relevant customer attributes to predict the Exited outcome.

Machine Learning Model
A Machine Learning classification model was trained using customer data.
The trained model was saved as:
                   churn_model.pkl
This saved model is loaded by the Streamlit application to make predictions on new customer data.

Installation
Clone the repository:
                   git clone
   https://github.com/ishaijaz11112222-del/Customer_Churn-Prediction
Navigate to the project folder:
                   cd Customer-Churn-Prediction
Install the required libraries:
                   pip install -r requirements.txt

Run the Application
Run the Streamlit application using:
                   streamlit run app.py

Prediction Output
The application predicts whether the customer is:
Likely to Stay
or
Likely to Churn

Future Improvements
Improve model accuracy
Add multiple Machine Learning models
Add model performance visualisations
Add customer churn probability
Improve the user interface
Add more customer features

👩‍💻 Author
Isha Ijaz
BS Artificial Intelligence Student
