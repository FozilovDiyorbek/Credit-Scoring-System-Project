# Credit-Scoring-System-Project   

## 📌 Project Overview
The **Credit Scoring System Project** is a machine learning solution designed to predict whether a customer is a potential credit risk (good or bad borrower).  
This project follows a structured ML pipeline including **data preparation, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment**.  

The final best-performing model is stored as `best_model.pkl` and can be used to make predictions through a simple deployment app.

---

## 📂 Project Structure
```
Credit_Scoring_System_Project/
│── data/
│ ├── raw/ # Raw dataset
│ ├── processed/ # Cleaned and processed dataset
│
│── notebooks/
│ ├── 01_data_preparation.ipynb
│ ├── 02_eda.ipynb
│ ├── 03_feature_engineering.ipynb
│ ├── 04_modeling.ipynb
│ ├── 05_model_evaluation.ipynb
│ ├── 06_model_deployment.ipynb
│
│── models/
│ ├── best_model.pkl # Saved best model
│
│── app/
│ ├── app.py # Deployment script (Streamlit/Flask)
│
│── requirements.txt # Required libraries
│── README.md # Project documentation
│── .gitignore
```

---

## ⚙️ Installation & Setup
Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/Credit-Scoring-System-Project.git
cd Credit-Scoring-System-Project
pip install -r requirements.txt
```
🚀 Running the Project
1. Run Jupyter Notebooks

Each step of the project is available in notebooks/:

Data Preparation

EDA

Feature Engineering

Model Training

Model Evaluation

Deployment

2. Run the Deployment App

If you are using Streamlit:
```
streamlit run app/app.py
```
📊 Features

Data preprocessing & cleaning

Exploratory Data Analysis (EDA) with visualization

Feature engineering (encoding, scaling, balancing with SMOTE)

Model comparison (Logistic Regression, Random Forest, XGBoost, LightGBM, CatBoost)

Model evaluation (Confusion Matrix, ROC Curve, AUC Score)

Deployment-ready best model (best_model.pkl)

✅ Results

The model successfully predicts whether a customer is likely to default or repay a loan.

Evaluation metrics such as accuracy, precision, recall, F1-score, and ROC-AUC are provided.

🔮 Future Improvements

Add hyperparameter tuning with Optuna

Implement explainability with SHAP/LIME

Deploy as a full web service with FastAPI + Docker

Integrate CI/CD pipeline for production readiness

👤 Author

Diyorbek Fozilov
📧 Email: diyorbekfozilov011@gmail.com

🌐 GitHub: (https://github.com/FozilovDiyorbek)

💼 LinkedIn: (https://www.linkedin.com/in/diyorbek-fozilov-251975305/)
