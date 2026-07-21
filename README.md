# CUSTOMER-CHURN-PREDICTION-USING-COST-SENSITIVE-MACHINE-LEARNING
# CUSTOMER-CHURN-PREDICTION-USING-COST-SENSITIVE-MACHINE-LEARNING

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by subscription-based and service-oriented businesses. Losing existing customers not only reduces revenue but also increases the cost of acquiring new customers. This project develops a **Cost-Sensitive Machine Learning** model that predicts whether a customer is likely to churn, while emphasizing the importance of correctly identifying customers at risk of leaving.

Unlike traditional machine learning models that treat all classification errors equally, cost-sensitive learning focuses on reducing the cost of **False Negatives** (customers who churn but are predicted to stay), helping organizations take proactive retention measures.

---

## 🎯 Problem Statement

Build an intelligent machine learning model that accurately predicts customer churn using customer demographic and financial information. The model incorporates data preprocessing, feature engineering, class imbalance handling using **SMOTE**, and **XGBoost** classification to improve churn prediction performance.

---

## 🚀 Features

* Data preprocessing and cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Feature Selection
* Categorical Data Encoding
* Class Imbalance Handling using SMOTE
* Cost-Sensitive Machine Learning Approach
* XGBoost Classification Model
* Model Evaluation using multiple metrics
* Ready for deployment

---

## 📂 Dataset

The project uses the **Customer Churn Modeling Dataset**, which contains customer information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Is Active Member
* Estimated Salary
* Exited (Target Variable)

**Target Variable**

* `0` → Customer Not Churned
* `1` → Customer Churned

---

## 🛠️ Technologies Used

### Programming Language

* Python 3.x

### Python Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* XGBoost
* Imbalanced-learn (SMOTE)
* Joblib / Pickle (for model saving)

### Development Environment

* Jupyter Notebook
* Visual Studio Code

---

## 📋 Project Workflow

```text
Problem Statement
        │
Collect Dataset
        │
Import Libraries
        │
Load Dataset
        │
Understand Dataset
        │
Exploratory Data Analysis (EDA)
        │
Data Cleaning
        │
Feature Engineering
        │
Encode Categorical Data
        │
Feature Selection
        │
Train-Test Split
        │
Feature Scaling
        │
Apply SMOTE
        │
Train XGBoost Model
        │
Make Predictions
        │
Evaluate Model
        │
Hyperparameter Tuning
        │
Save Model
        │
Deploy Model
```

---

## ⚙️ Machine Learning Algorithm

### XGBoost Classifier

Model Parameters

* Number of Trees: 100
* Learning Rate: 0.1
* Maximum Depth: 4
* Random State: 42

---

## 📊 Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

---

## 📈 Model Performance

Example Metrics

| Metric    | Value                       |
| --------- | --------------------------- |
| Accuracy  | *(Update with your result)* |
| Precision | *(Update)*                  |
| Recall    | *(Update)*                  |
| F1-Score  | *(Update)*                  |

---

## 📁 Project Structure

```text
CUSTOMER-CHURN-PREDICTION-USING-COST-SENSITIVE-MACHINE-LEARNING/
│
├── Dataset/
│   └── Churn_Modelling.csv
│
├── notebooks/
│   └── Customer_Churn_Prediction.ipynb
│
├── models/
│   └── churn_model.pkl
│
├── images/
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   └── confusion_matrix.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 💻 System Requirements

### Hardware

* Processor: Intel Core i5 (8th Generation or above) / AMD Ryzen 5 or above
* RAM: 8 GB or higher
* Storage: Minimum 10 GB free space

### Software

* Windows 10 / Windows 11 (64-bit)
* Python 3.10 or later
* Jupyter Notebook or Visual Studio Code

---

## 💻 Development Environment

**Laptop Information**

> Replace the placeholders below with your actual laptop details.

| Component            | Details                                            |
| -------------------- | -------------------------------------------------- |
| Laptop Brand         | Acer                                               |
| Operating System     | Windows 10 Pro (64-bit)                            |
| OS Version           | Version 10.0.19045                                 |
| Processor            | *(e.g., Intel Core i5-10210U / AMD Ryzen 5 5500U)* |
| RAM                  | *(e.g., 8 GB DDR4)*                                |
| Storage              | *(e.g., 512 GB SSD)*                               |
| IDE                  | Visual Studio Code                                 |
| Notebook Environment | Jupyter Notebook                                   |
| Python Version       | 3.x                                                |

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/CUSTOMER-CHURN-PREDICTION-USING-COST-SENSITIVE-MACHINE-LEARNING.git
```

Navigate to the project directory

```bash
cd CUSTOMER-CHURN-PREDICTION-USING-COST-SENSITIVE-MACHINE-LEARNING
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the notebook

```bash
jupyter notebook
```

---

## ▶️ Usage

1. Open the Jupyter Notebook.
2. Load the customer churn dataset.
3. Execute the preprocessing steps.
4. Apply SMOTE to balance the training data.
5. Train the XGBoost model.
6. Evaluate the model using the provided metrics.
7. Save the trained model for deployment.

---

## 🔮 Future Enhancements

* Hyperparameter optimization using GridSearchCV or RandomizedSearchCV
* Integration with SHAP for model explainability
* Real-time customer churn prediction dashboard
* Streamlit or Flask web application deployment
* Cloud deployment using AWS, Azure, or Google Cloud

---

## 👩‍💻 Author

**Monika R**

**B.Tech – Artificial Intelligence and Data Science**

**Nehru Institute of Engineering and Technology, Coimbatore**

GitHub: https://github.com/Monika843

LinkedIn: *(Add your LinkedIn profile URL here.)*

---

## 📜 License

This project is developed for academic learning and placement portfolio purposes. You are free to use and modify the project with proper attribution.

---

## ⭐ Acknowledgements

* Scikit-learn
* XGBoost
* Imbalanced-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Kaggle Customer Churn Modeling Dataset
