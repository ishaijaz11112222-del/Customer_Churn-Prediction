## 📌 Project Overview
Customer Churn Prediction is a Machine Learning project developed to predict whether a customer is likely to leave a company or continue using its services.
The project uses customer-related information and a trained Machine Learning classification model to generate a binary churn prediction:

- *0 → Customer will stay*
- *1 → Customer is likely to churn*

The project demonstrates an end-to-end Machine Learning workflow. It includes data preparation, model training, model saving, prediction, and application development using Streamlit.

## 🎯 Objective
The primary objective of this project is to help businesses identify customers who are at risk of churning.
By predicting potential customer churn at an early stage, businesses can take proactive actions. It includes improving customer experience, providing personalised offers, and developing customer retention strategies.

## ✨ Key Features
- Customer churn prediction using Machine Learning
- Pre-trained classification model
- Real-time customer churn prediction
- Interactive and user-friendly Streamlit interface
- Easy-to-use prediction system
- Saved model for making predictions without retraining
- Complete Machine Learning workflow from data preparation to prediction

## 🛠️ Technologies Used
Python ( Core programming language )
Pandas ( Data manipulation and analysis )
NumPy ( Numerical computations )
Scikit-learn ( Machine Learning model development )
Streamlit ( Web application interface )
Joblib ( Model saving and loading )
Google Colab ( Model development and training )
GitHub ( Version control and project hosting )

## 📂 Project Structure
```text
Customer-Churn-Prediction/
│
├── app.py
├── churn_model.pkl
├── requirements.txt
└── README.md

File Description
app.py — Contains the Streamlit web application and prediction logic.
churn_model.pkl — Contains the trained Machine Learning model.
requirements.txt — Contains the Python libraries required to run the project.
README.md — Provides project documentation and usage instructions.

📊 Dataset
The project uses the Churn Modelling dataset, which contains customer-related information used for Machine Learning.
The dataset includes customer attributes that help the model learn patterns associated with customer churn.
The target variable is:
Exited
where:
0 → Customer stayed
1 → Customer churned
The relevant customer attributes are prepared and provided to the trained model for prediction.
The dataset that I have used in it is:
https://ap.wps.com/cms/docs/d/cbCainhmauwuvEkc

🤖 Machine Learning Model
A Machine Learning classification model was trained using the customer churn dataset.
The trained model is saved as:
churn_model.pkl
The saved model is loaded by the Streamlit application and used to generate predictions for new customer data.
This approach allows the application to use the already-trained model without retraining it every time the application runs.

🔄 Machine Learning Workflow
The project follows a complete Machine Learning workflow:
         Dataset
            ↓
     Data Preparation
            ↓
  Feature Selection & Encoding
            ↓
      Model Training
            ↓
       Model Saving
            ↓
    Streamlit Application
            ↓
      Customer Input
            ↓
     Churn Prediction

💻 Installation
1. Clone the Repository
git clone https://github.com/ishaijaz11112222-del/Customer_Churn-Prediction.git
2. Navigate to the Project Directory
cd Customer_Churn-Prediction
3. Install Required Dependencies
pip install -r requirements.txt

▶️ Run the Application
Start the Streamlit application using:
streamlit run app.py
After running the command, Streamlit will launch the application in your web browser.

🔮 Prediction
The application accepts customer information through the Streamlit interface and passes the input to the trained Machine Learning model.
The model then predicts whether the customer is likely to stay or churn.
Prediction Classes
Prediction
Meaning
0
Customer will stay
1
Customer is likely to churn

📈 Prediction Output
The application provides a clear prediction indicating whether the customer is:
Likely to Stay
or
Likely to Churn
This allows users to quickly understand the predicted customer behaviour.

🔮 Future Improvements
The project can be further enhanced through:
Improving model performance and accuracy
Comparing multiple Machine Learning algorithms
Hyperparameter tuning
Feature engineering
Adding customer churn probability
Adding model performance visualisations
Improving the Streamlit user interface
Adding additional customer features
Implementing advanced customer retention insights
Completing production-level deployment

🎓 Learning Outcomes
Through this project, the following concepts were applied:
Data preprocessing
Feature selection
Categorical data encoding
Machine Learning classification
Model training
Model persistence
Prediction using a trained model
Streamlit application development
GitHub project management

👩‍💻 Author
Isha Ijaz
BS Artificial Intelligence Student
Interested in:
Artificial Intelligence
Machine Learning
Data Science
Generative AI
