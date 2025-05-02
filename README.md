# 🚀 Loan Default Prediction

## 📌 Overview

This project aims to predict the likelihood of a borrower defaulting on a loan using a machine learning model.  
It uses a **CatBoostClassifier**, a modern web stack with **Flask**, and DevOps tools like **Docker** and **GitHub Actions** for CI/CD.

🔗 [**Live Demo Form**](https://loan-default-prediction-jit-3b7d62d99e52.herokuapp.com/)

---

## 🧠 Problem Statement

Financial institutions face risks from loan defaults. Traditional assessments (credit score, income) often fail to capture complex borrower patterns.  
This project builds a robust ML solution using advanced preprocessing, modeling, and evaluation techniques.

---

## 📊 Dataset Description

The dataset contains borrower-related features.  
The target variable is `Default` (`1 = defaulted`, `0 = not defaulted`).

| Column                       | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| Client_Income               | Client income in $                                           |
| Car_Owned, Bike_Owned       | 0 = No, 1 = Yes                                              |
| Active_Loan, House_Own      | 0 = No, 1 = Yes                                              |
| Child_Count                 | Number of children                                           |
| Credit_Amount               | Loan credit amount                                           |
| Loan_Annuity                | Monthly repayment amount                                     |
| Accompany_Client            | Who accompanied the client                                   |
| Client_Income_Type          | Type of income (e.g., working, pensioner)                   |
| Client_Education            | Highest education level                                      |
| Client_Marital_Status       | Marital status                                               |
| Client_Gender               | Gender                                                       |
| Loan_Contract_Type          | Loan type (CL = Cash Loan, RL = Revolving Loan)             |
| Client_Housing_Type         | Client's housing situation                                   |
| Population_Region_Relative  | Region's relative population                                 |
| Age_Days, Employed_Days     | Time-based features (negative values = number of days ago)  |
| ID_Days, Registration_Days  | Document and registration update timelines                  |
| Own_House_Age               | House age in years                                           |
| Phone Tags                  | 0 = Not Provided, 1 = Provided (Mobile/Home/Work)           |
| Client_Occupation           | Occupation type                                              |
| Client_Family_Members       | Number of family members                                     |
| Cleint_City_Rating          | City rating (1 = Average, 2 = Good, 3 = Best)                |
| Application_Process_*       | Day and Hour of application                                  |
| Score_Source_1/2/3          | Normalized external scores                                   |
| Social_Circle_Default       | Number of known defaulters in client’s circle                |
| Credit_Bureau               | Loan inquiries in the last year                              |
| Default                     | ✅ Target variable                                            |

---

## 🧰 Tech Stack

- **Machine Learning**: CatBoost
- **Backend**: Flask
- **Validation**: Pydantic
- **Containerization**: Docker
- **CI/CD**: GitHub Actions
- **Deployment**: Heroku

---

## 🧪 Model Pipeline

### 🔧 Preprocessing
- Imputes missing values
- Detects and handles outliers
- Encodes categorical variables (label + one-hot)
- Applies feature scaling (`StandardScaler`)

### 🧠 Modeling
- Algorithm: `CatBoostClassifier`
- Handles class imbalance with `class_weights`
- Tuned via `GridSearchCV`

### 📈 Evaluation
- Accuracy
- Precision / Recall / F1
- ROC-AUC Curve
- Confusion Matrix

---

## 🌐 Deployment

Deployed on Heroku using Docker containers.  
CI/CD enabled via GitHub Actions.

### 🔄 Run Locally

```bash
git clone https://github.com/yourusername/loan-default-prediction.git
cd loan-default-prediction
docker build -t loan-default-app .
docker run -p 5000:5000 loan-default-app
# Open in browser: http://localhost:5000
```

---

## 📂 Project Structure

```plaintext
.
├── app/
│   ├── main.py                 # Flask application logic
│   ├── model/
│   │   ├── catboost_model_version_1.pkl
│   │   ├── data_scaling_latest.pkl
│   │   └── data_preprocessing_v3.pkl
│   └── templates/
│       └── home.html           # HTML form for user input
├── Dockerfile
├── requirements.txt
├── Procfile                   # For Heroku deployment
├── README.md
└── .github/
    └── workflows/
        └── main.yml           # GitHub Actions CI/CD pipeline
```

---

## 🔮 Future Improvements

- Add SHAP-based model interpretability
- Store prediction logs in a database
- Add login/authentication with admin dashboard
- Visualize metrics and errors in real time
- Use of Deep Learning techniques to achieve better metrices

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork the repo, create a feature branch, and open a PR.

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).
