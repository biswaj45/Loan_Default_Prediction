# Loan Default Prediction 🚀

## 📌 Overview

This project aims to predict the likelihood of a borrower defaulting on a loan using a machine learning model.  
It uses a **CatBoostClassifier**, modern web stack with **Flask**, and DevOps tools like **Docker** and **GitHub Actions** for CI/CD.

🔗 [**Live Demo Form**](https://loan-default-prediction-jit-3b7d62d99e52.herokuapp.com/)

---

## 🧠 Problem Statement

Financial institutions face risks from loan defaults. Traditional assessments (credit score, income) fail to capture complex borrower patterns.  
This project builds a robust machine learning solution using advanced preprocessing and model evaluation techniques.

---

## 📊 Dataset Description

The dataset contains borrower attributes.  
The target variable is `Default` (`1 = defaulted`, `0 = not defaulted`).

| Column                    | Description                                                |
|---------------------------|------------------------------------------------------------|
| Client_Income             | Client income in $                                          |
| Car_Owned, Bike_Owned     | 0 = No, 1 = Yes                                             |
| Active_Loan, House_Own    | 0 = No, 1 = Yes                                             |
| Credit_Amount             | Credit amount of the loan                                  |
| Age_Days, Employed_Days   | Time-based features                                        |
| Loan_Contract_Type        | CL = Cash Loan, RL = Revolving Loan                        |
| Application_Process_Hour  | Hour of day client applied                                 |
| Social_Circle_Default     | # of contacts who defaulted                                |
| ...                       | And many more as described in the data dictionary...       |

---

## 🧰 Tech Stack

- **Machine Learning**: CatBoost
- **Backend**: Flask
- **Validation**: Pydantic
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Deployment**: Heroku

---

## 🧪 Model Pipeline

### 🔧 Preprocessing
- Missing value imputation
- One-hot & label encoding
- Outlier handling
- Feature scaling (StandardScaler)

### 🧠 Modeling
- Model: `CatBoostClassifier`
- Class imbalance handled via `class_weights`
- Hyperparameter tuning via `GridSearchCV`

### 📈 Evaluation
- Accuracy
- Precision / Recall / F1
- ROC-AUC
- Confusion Matrix

---

## 🌐 Deployment

Deployed via Docker and GitHub Actions to Heroku.

### 🔄 Run Locally

```bash
git clone https://github.com/yourusername/loan-default-prediction.git
cd loan-default-prediction
docker build -t loan-default-app .
docker run -p 5000:5000 loan-default-app
# Visit http://localhost:5000
