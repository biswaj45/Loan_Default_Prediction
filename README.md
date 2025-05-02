Loan Default Prediction
🚀 Overview
This project aims to predict the likelihood of a borrower defaulting on a loan using a machine learning model. Financial institutions face substantial risk from defaulted loans, which can result in losses and damage credibility. This solution leverages the power of CatBoost, an advanced gradient boosting algorithm, to deliver high-performance predictions, along with a modern DevOps pipeline for seamless deployment.

🔗 Live Demo: Loan Default Prediction Form

🧠 Problem Statement
Title: Loan Default Prediction and Evaluation Criteria

Financial institutions struggle with accurately identifying borrowers likely to default. Traditional methods like credit scores or income-based assessments fail to capture the complexity of the underlying data. This project aims to develop a robust machine learning model that accounts for a wide range of borrower attributes and relationships, providing an accurate prediction of loan defaults.

📊 Dataset Description
The dataset contains various features related to clients applying for loans. The target variable is Default (1 = defaulted, 0 = not defaulted).

Key Features
Column Name	Description
Client_Income	Client Income in $
Car_Owned, Bike_Owned	0 = No, 1 = Yes
Active_Loan, House_Own	0 = No, 1 = Yes
Child_Count	Number of children
Credit_Amount	Credit amount of the loan
Loan_Annuity	Loan annuity in $
Accompany_Client	Companion when applying
Client_Income_Type, Client_Education, Client_Marital_Status, Client_Gender, Client_Housing_Type, Type_Organization, Client_Occupation	Categorical variables
Loan_Contract_Type	Type of loan (Cash or Revolving)
Population_Region_Relative	Region's relative population
Age_Days, Employed_Days, Registration_Days, ID_Days, Phone_Change, Own_House_Age	Time-based features
Mobile_Tag, Homephone_Tag, Workphone_Working	0 = No, 1 = Yes
Client_Family_Members	Family size
Cleint_City_Rating	3 = best, 2 = good, 1 = average
Application_Process_Day, Application_Process_Hour	Temporal application info
Client_Permanent_Match_Tag, Client_Contact_Work_Tag	Address match indicators
Score_Source_1/2/3	Normalized external scores
Social_Circle_Default	# of defaults among contacts
Credit_Bureau	Inquiries in last year
Default	Target variable (1 = Default)

🧰 Tech Stack
Machine Learning: CatBoost

Framework: Flask

Validation: Pydantic

Deployment: Heroku

Containerization: Docker

CI/CD: GitHub Actions

🔧 Features
End-to-end loan default prediction web app

User input form with client features (Bootstrap styled)

Automatic prediction of default status

CI/CD pipeline with Docker and GitHub Actions

RESTful API endpoint for model inference

Handles missing data, outliers, and class imbalance

🧪 Model Pipeline
Data Preprocessing

Missing value handling

Outlier detection

Label encoding and one-hot encoding

Feature scaling (if needed)

Modeling

Algorithm: CatBoostClassifier

Class imbalance handled via class weights

Hyperparameter tuning using cross-validation

Evaluation Metrics

Accuracy

Precision, Recall, F1 Score

ROC-AUC Curve

Confusion Matrix

🌐 Deployment
The app is deployed on Heroku and containerized using Docker for portability.

Steps:
Clone repo:

bash
Copy
Edit
git clone https://github.com/yourusername/loan-default-prediction.git
cd loan-default-prediction
Build Docker image:

bash
Copy
Edit
docker build -t loan-default-app .
Run locally:

bash
Copy
Edit
docker run -p 5000:5000 loan-default-app
Access at http://localhost:5000

CI/CD:

GitHub Actions triggered on push to main

Auto-deploys to Heroku via container registry

📂 Project Structure
bash
Copy
Edit
.
├── app/
│   ├── main.py                # Flask app
│   ├── model/
│   │   ├── catboost_model.cbm # Trained model
│   │   └── preprocessor.pkl   # Preprocessing pipeline
│   └── templates/
│       └── index.html         # Bootstrap form
├── Dockerfile
├── requirements.txt
├── .github/workflows/
│   └── ci-cd.yml              # GitHub Actions workflow
├── README.md
└── Procfile                  # For Heroku
📈 Future Improvements
Use SHAP for model interpretability

Incorporate time series behavior

Add admin dashboard to monitor predictions

Integrate with a database for storing user inputs

🤝 Contributing
Contributions are welcome! Please fork the repo, create a branch, and open a pull request.

📜 License
This project is licensed under the MIT License.

