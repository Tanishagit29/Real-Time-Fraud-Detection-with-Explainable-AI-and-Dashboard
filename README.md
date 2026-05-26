<<<<<<< HEAD
# 💳 Real-Time Fraud Detection System with Explainable AI & Live Dashboard

## 📌 Project Overview

This project is an end-to-end AI-powered Fraud Detection System built using Machine Learning, Explainable AI (SHAP), and an interactive Streamlit dashboard.

The system detects fraudulent financial transactions in real time while providing transparent explanations for predictions using SHAP values.

This project simulates a real-world fintech fraud analytics solution used by banks and financial institutions.

---

# 🚀 Features

✅ Fraud Detection using Machine Learning  
✅ Severe Class Imbalance Handling with SMOTE  
✅ Threshold Optimization for better Recall  
✅ Explainable AI using SHAP  
✅ Risk Tier Segmentation  
✅ Interactive Streamlit Dashboard  
✅ Plotly Interactive Visualizations  
✅ Fraud Pattern Analysis  
✅ Business Recommendations & Insights  

---

# 📂 Dataset

Dataset Used: IEEE-CIS Fraud Detection Dataset

Source:
https://www.kaggle.com/c/ieee-fraud-detection/data

Files Used:
- train_transaction.csv
- train_identity.csv

Datasets were merged using:
- TransactionID

---

# 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python | Programming Language |
| Pandas / NumPy | Data Processing |
| Scikit-learn | ML Utilities |
| LightGBM | Fraud Classification |
| XGBoost | Model Comparison |
| SHAP | Explainable AI |
| Plotly | Interactive Charts |
| Streamlit | Dashboard |
| Matplotlib / Seaborn | Visualizations |
| Imbalanced-learn | SMOTE |

---

# 📊 Machine Learning Workflow

## 1️⃣ Data Preprocessing

- Merged transaction and identity datasets
- Handled missing values
- Dropped columns with >50% missing values
- Label Encoding for categorical features
- Feature Scaling using RobustScaler

---

## 2️⃣ Feature Engineering

Created custom features including:

- AmtToMeanRatio
- HourOfDay
- DeviceRisk
- LogTransactionAmt
- IsHighAmount

---

## 3️⃣ Imbalance Handling

Applied:
- SMOTE (Synthetic Minority Oversampling Technique)

Performed:
- Stratified Train-Test Split

---

## 4️⃣ Models Trained

- LightGBM Classifier
- XGBoost Classifier
- Isolation Forest

---

## 5️⃣ Model Evaluation Metrics

Models evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC

---

# 🧠 Explainable AI (SHAP)

Implemented SHAP for model explainability.

Generated:
- SHAP Summary Plot
- SHAP Waterfall Plot
- SHAP Dependence Plot

Key fraud indicators identified:
- Transaction Amount
- Behavioral Features
- Device Risk
- HourOfDay

---

# ⚠️ Risk Segmentation

Transactions segmented into:

| Risk Tier | Probability |
|---|---|
| 🔴 Critical Risk | ≥ 0.75 |
| 🟡 Suspicious | 0.40 – 0.74 |
| 🟢 Clear | < 0.40 |

---

# 📈 Dashboard Features

## Streamlit Multi-Page Dashboard

### 🏠 Overview Page
- KPI Metrics
- Fraud Rate
- Charts & Visualizations

### 🔍 Transaction Explorer
- Search Transactions
- Filter by Risk Tier
- Interactive Analysis

### 🧠 SHAP Explainer
- SHAP Visualization
- Plain-English Fraud Explanation

---

# 📊 Visualizations

Generated charts include:

- SHAP Summary Plot
- ROC Curve
- Precision-Recall Curve
- Risk Tier Donut Chart
- Fraud by Hour of Day
- Threshold vs F1-Score
- Correlation Heatmap
- Transaction Amount Distribution

---

# 📁 Project Structure

```text
FraudDetection_[YourName]
│
├── analysis.ipynb
├── README.md
├── requirements.txt
│
├── charts/
│   ├── shap_summary.png
│   ├── model_comparison.png
│
├── data/
│   ├── train_transaction.csv
│   ├── train_identity.csv
│
├── dashboard/
│   ├── app.py
│   ├── model.pkl
│   │
│   ├── pages/
│   │   ├── 1_Overview.py
│   │   ├── 2_Transaction_Explorer.py
│   │   ├── 3_SHAP_Explainer.py
```

---

# ▶️ How to Run the Project

## Step 1 — Install Libraries

```bash
pip install -r requirements.txt
```

---

## Step 2 — Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📌 Results

✅ LightGBM achieved the best performance  
✅ SHAP improved explainability and trust  
✅ PR-AUC proved more reliable than Accuracy  
✅ Risk segmentation enabled operational fraud monitoring  
✅ Dashboard supports interactive fraud investigation  

---

# 💼 Business Impact

- Faster fraud detection
- Reduced financial loss
- Improved analyst efficiency
- Transparent AI decisions
- Real-time fraud monitoring

Estimated annual fraud savings:
### ~$1.48 Billion

---

# ⚠️ Limitations

- Fraud patterns evolve over time
- False positives still possible
- Requires periodic retraining
- Limited real-time streaming support

---

# 🔮 Future Improvements

Potential future enhancements:

- Real-time streaming pipeline
- Device fingerprinting
- Geolocation intelligence
- Graph-based fraud detection
- Deep learning models
- Cloud deployment

---

# 👩‍💻 Author

Tanisha Poojary


