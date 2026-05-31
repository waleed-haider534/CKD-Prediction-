# 🏥 Chronic Kidney Disease Prediction System

<!-- Badges and Shields -->
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Framework](https://img.shields.io/badge/Framework-FastAPI%2BStreamlit-orange)](https://fastapi.tiangolo.com/)
[![ML](https://img.shields.io/badge/ML-LightGBM%2FRandomForest-red)](https://lightgbm.readthedocs.io/)
[![Dataset](https://img.shields.io/badge/Dataset-UCI-yellow)](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/)

---

A machine learning-powered web application for **early detection and prediction of Chronic Kidney Disease (CKD)** using ensemble learning algorithms. The system analyzes 24 clinical features from blood and urine tests to predict whether a patient has CKD or not.

<p align="center">
  <img src="https://img.shields.io/badge/Accuracy-100%25-success?style=for-the-badge" alt="Model Accuracy">
  <img src="https://img.shields.io/badge/F1%20Score-0.9797-yellowgreen?style=for-the-badge" alt="F1 Score">
</p>

---

## 📑 Table of Contents

1. [About The Project](#about-the-project)
2. [Problem Statement](#problem-statement)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [Dataset](#dataset)
6. [Project Structure](#project-structure)
7. [Methodology](#methodology)
8. [Model Performance](#model-performance)
9. [Quick Start](#quick-start)
10. [Installation](#installation)
11. [Running the Application](#running-the-application)
12. [API Documentation](#api-documentation)
13. [Example Usage](#example-usage)
14. [Contributing](#contributing)
15. [License](#license)
16. [References](#references)

---

## 📖 About The Project

**Course:** CSE6505 — Machine Learning  
**Semester:** BSCS 6th Semester  
**Institution:** Lahore Garrison University, Lahore, Pakistan

**Reference Paper:**
> *Machine learning models for chronic kidney disease diagnosis and prediction*
> Biomedical Signal Processing and Control, 2024
> DOI: 10.1016/j.bspc.2023.105368

This project implements a complete **end-to-end ML pipeline** for CKD prediction — from raw data preprocessing to a deployable web application. It combines state-of-the-art ensemble learning algorithms with a modern FastAPI backend and Streamlit frontend.

---

## 🎯 Problem Statement

**Chronic Kidney Disease (CKD)** is a progressive condition affecting approximately **10% of the global population**. Often called a "silent disease" because symptoms do not appear until the disease has significantly advanced, CKD presents major healthcare challenges:

| Challenge | Impact |
|-----------|--------|
| **Late Detection** | Most patients are diagnosed only in advanced stages |
| **High Treatment Cost** | Dialysis and kidney transplants are extremely expensive |
| **Resource Scarcity** | Shortage of specialized nephrologists in developing countries |

### 🎓 Solution

Machine learning models can analyze routine blood and urine test results to detect CKD in early stages — enabling **timely treatment** and **better patient outcomes**.

---

## ✨ Features

- **24 Clinical Features Analysis** — Comprehensive analysis of blood and urine test parameters
- **Ensemble Learning** — Multiple ML algorithms (Random Forest, Gradient Boosting, XGBoost, LightGBM)
- **Automated Preprocessing** — Built-in data cleaning, imputation, and encoding
- **REST API** — FastAPI backend for programmatic access
- **Web Interface** — User-friendly Streamlit UI for predictions
- **Cross-Validation** — Robust model evaluation using StratifiedKFold
- **No Data Leakage** — KNNImputer inside Pipeline ensures proper imputation
- **High Accuracy** — 100% test accuracy with 0.9797 CV F1-score

---

## 🛠 Tech Stack

### Core Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.11+ | Core programming language |
| **pandas** | 2.x | Data manipulation and analysis |
| **numpy** | 1.x | Numerical computing |
| **scikit-learn** | 1.x | Machine learning algorithms |

### Visualization

| Technology | Purpose |
|------------|---------|
| **matplotlib** | Static plotting and charts |
| **seaborn** | Statistical graphics |

### Machine Learning

| Technology | Purpose |
|------------|---------|
| **scikit-learn** | Random Forest, Gradient Boosting, Voting, Stacking |
| **XGBoost** | Extreme Gradient Boosting |
| **LightGBM** | Light Gradient Boosting Machine |

### Web Framework

| Technology | Purpose |
|------------|---------|
| **FastAPI** | REST API backend |
| **Uvicorn** | ASGI server |
| **Streamlit** | Web UI frontend |
| **joblib** | Model serialization |

---

## 📊 Dataset

| Property | Value |
|----------|-------|
| **Source** | UCI Machine Learning Repository |
| **Link** | [chronic+kidney+disease](https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease) |
| **Instances** | 400 patients |
| **Features** | 24 clinical features + 1 target |
| **Classes** | CKD (250) and NOTCKD (150) |
| **Missing Values** | Present in multiple columns |

### 📋 Feature Description

The dataset includes 24 clinical features from blood and urine tests:

#### Numeric Features

| Feature | Description | Unit | Range |
|---------|-------------|------|-------|
| `age` | Patient age | years | 1-90 |
| `bp` | Blood Pressure | mmHg | 50-180 |
| `sg` | Specific Gravity | - | 1.005-1.025 |
| `al` | Albumin | - | 0-5 |
| `su` | Sugar | - | 0-5 |
| `bgr` | Blood Glucose Random | mg/dL | 70-490 |
| `bu` | Blood Urea | mg/dL | 1.5-391 |
| `sc` | Serum Creatinine | mg/dL | 0.2-18.0 |
| `sod` | Sodium | mEq/L | 4.5-163 |
| `pot` | Potassium | mEq/L | 2.5-47.0 |
| `hemo` | Hemoglobin | g/dL | 3.1-17.8 |
| `pcv` | Packed Cell Volume | % | 16-54 |
| `wbcc` | White Blood Cell Count | cells/mm³ | 2100-26000 |
| `rbcc` | Red Blood Cell Count | millions/mm³ | 2.1-8.0 |

#### Categorical Features

| Feature | Description | Values |
|---------|-------------|--------|
| `rbc` | Red Blood Cells | normal, abnormal |
| `pc` | Pus Cell | normal, abnormal |
| `pcc` | Pus Cell Clumps | present, notpresent |
| `ba` | Bacteria | present, notpresent |
| `htn` | Hypertension | yes, no |
| `dm` | Diabetes Mellitus | yes, no |
| `cad` | Coronary Artery Disease | yes, no |
| `appet` | Appetite | good, poor |
| `pe` | Pedal Edema | yes, no |
| `ane` | Anemia | yes, no |

#### Target Variable

| Class | Description | Count |
|-------|-------------|-------|
| `ckd` | Chronic Kidney Disease | 250 (62.5%) |
| `notckd` | No Chronic Kidney Disease | 150 (37.5%) |

---

## 📂 Project Structure

```
CKD-ML/
├── notebooks/                  # Jupyter notebooks for ML pipeline
│   ├── data/
│   │   └── kidney_disease.csv # Raw UCI dataset
│   ├── ml_v0.ipynb            # Exploratory Data Analysis (EDA)
│   ├── ml_v1.ipynb            # Preprocessing + GridSearchCV
│   └── ml_v2.ipynb            # Final model training & evaluation
│
├── artifacts/                 # Trained models and outputs
│   └── final_model.joblib     # Best trained model (LightGBM Pipeline)
│
├── app/                       # FastAPI backend
│   ├── classifier.py          # Model loading and prediction logic
│   └── main.py                # FastAPI application entry point
│
├── report/                    # Analysis reports and visualizations
│   ├── missing_values.png     # Missing values analysis
│   ├── class_distribution.png # Class balance visualization
│   ├── numeric_distributions.png # Feature distributions
│   ├── correlation_heatmap.png   # Feature correlations
│   ├── categorical_features.png  # Categorical analysis
│   ├── confusion_matrix.png   # Model confusion matrix
│   ├── model_comparison.png   # All models comparison chart
│   └── model_results.csv      # Detailed metrics table
│
├── streamlit_app.py           # Streamlit web interface
├── main.py                    # Main entry point
├── pyproject.toml             # Project dependencies
├── uv.lock                    # Locked dependencies
├── .gitignore                 # Git ignore rules
├── .python-version            # Python version specification
└── README.md                  # This file
```

---

## 🔬 Methodology

### Phase 1: Exploratory Data Analysis (`notebooks/ml_v0.ipynb`)

- Dataset shape, data types, and statistical summary
- Missing values analysis and visualization
- Class distribution analysis (imbalance detection)
- Numeric feature distributions and boxplots
- Correlation heatmap for feature relationships
- Categorical feature analysis

### Phase 2: Preprocessing & Model Selection (`notebooks/ml_v1.ipynb`)

#### Data Cleaning Pipeline
1. **Dropped rows** with missing target variable
2. **Label encoded** categorical features (0/1 mapping)
3. **Stratified train/test split** (80/20 ratio)

#### Pipeline Architecture (No Data Leakage)

```
┌─────────────────────────────────────────┐
│           Pipeline                      │
│  ┌─────────────────────────────────┐    │
│  │  KNNImputer (K=3)              │    │
│  │  - Fits only on training data   │    │
│  │  - No data leakage to validation│    │
│  └─────────────────────────────────┘    │
│                  ↓                       │
│  ┌─────────────────────────────────┐    │
│  │  RandomForestClassifier        │    │
│  │  - Base estimator              │    │
│  └─────────────────────────────────┘    │
└─────────────────────────────────────────┘
```

#### Hyperparameter Tuning
- **Method:** GridSearchCV with 5-fold StratifiedKFold
- **Scoring:** `f1_macro` (handles class imbalance)
- **Best Parameters Found:**

| Parameter | Value |
|-----------|-------|
| `n_neighbors` (KNN) | 3 |
| `n_estimators` (RF) | 100 |
| `max_depth` | 5 |
| `min_samples_split` | 2 |
| `min_samples_leaf` | 1 |
| `max_features` | sqrt |

### Phase 3: Final Model Training (`notebooks/ml_v2.ipynb`)

Seven ensemble models trained and evaluated:

| # | Model | Description |
|---|-------|-------------|
| 1 | **Random Forest** | Bagged decision trees with bootstrap sampling |
| 2 | **Gradient Boosting** | Sequential error-correcting trees |
| 3 | **AdaBoost** | Adaptive weighted boosting |
| 4 | **XGBoost** | Optimized gradient boosting with L1+L2 regularization |
| 5 | **LightGBM** | Leaf-wise gradient boosting (fastest) |
| 6 | **Voting Classifier** | Soft voting ensemble (RF + GB + XGB) |
| 7 | **Stacking Classifier** | Meta-learner (Logistic Regression) on base models |

---

## 📈 Model Performance

### Comparison Results

| Model | Accuracy | Precision | Recall | F1 Macro | ROC-AUC | CV F1 (std) |
|-------|----------|-----------|--------|---------|---------|-------------|
| **LightGBM** 🏆 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9797 (±0.017) |
| AdaBoost | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 0.9539 (±0.032) |
| Random Forest | 0.9875 | 0.9902 | 0.9833 | 0.9866 | 1.0000 | 0.9864 (±0.014) |
| Stacking | 0.9875 | 0.9902 | 0.9833 | 0.9866 | 1.0000 | 0.9797 (±0.020) |
| XGBoost | 0.9875 | 0.9902 | 0.9833 | 0.9866 | 1.0000 | 0.9698 (±0.025) |
| Voting | 0.9750 | 0.9808 | 0.9667 | 0.9730 | 1.0000 | 0.9696 (±0.025) |
| Gradient Boosting | 0.9750 | 0.9808 | 0.9667 | 0.9730 | 0.9660 | 0.9563 (±0.030) |

### 🏆 Best Model: LightGBM

| Metric | Value |
|--------|-------|
| **Test Accuracy** | 100% |
| **CV F1 Score** | 0.9797 |
| **CV Standard Deviation** | 0.0168 (lowest) |
| **Inference Time** | Fastest |

### Key Findings

1. **LightGBM** achieved highest CV F1-score with lowest variance (most stable)
2. **KNNImputer** inside Pipeline eliminated data leakage completely
3. **StratifiedKFold** preserved class ratios across all 5 folds
4. **f1_macro** scoring effectively handled class imbalance (62.5% CKD vs 37.5% NOTCKD)
5. **Strongest Predictors:** Serum Creatinine, Hemoglobin, and Packed Cell Volume

---

## ⚡ Quick Start

### Prerequisites

- Python 3.11 or higher
- uv package manager (recommended)

### Clone the Repository

```bash
git clone https://github.com/waleed-haider534/CKD-ML.git
cd CKD-ML
```

### Install Dependencies

```bash
# Create virtual environment
uv venv

# Activate (Windows)
.venv\Scripts\activate

# Activate (Linux/Mac)
source .venv/bin/activate

# Install all dependencies
uv pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm fastapi uvicorn streamlit joblib requests
```

### Run the Application

**Terminal 1 — Start FastAPI Backend:**
```bash
cd app
uvicorn main:app --reload --port 8000
```

**Terminal 2 — Start Streamlit Frontend:**
```bash
streamlit run streamlit_app.py
```

### Access the Application

- 🌐 **Streamlit UI:** http://localhost:8501
- 📚 **API Documentation:** http://127.0.0.1:8000/docs

---

## 📥 Installation

### Option 1: Using uv (Recommended)

```bash
# Install uv if not installed
pip install uv

# Create and activate virtual environment
uv venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
uv pip install -r requirements.txt
```

### Option 2: Using pip

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn xgboost lightgbm fastapi uvicorn streamlit joblib requests
```

### Option 3: Using pyproject.toml

```bash
# Install with uv (auto-reads pyproject.toml)
uv sync
```

---

## 🚀 Running the Application

### Running the Notebooks

```bash
# Open Jupyter Lab
jupyter lab notebooks/

# Or Jupyter Notebook
jupyter notebook notebooks/
```

**Recommended Order:**
1. `ml_v0.ipynb` → Run Exploratory Data Analysis
2. `ml_v1.ipynb` → Run Preprocessing and GridSearch
3. `ml_v2.ipynb` → Train final models and evaluate

### Running the Web Application

#### Step 1: Start the Backend API

```bash
# Navigate to app directory
cd app

# Start FastAPI server
uvicorn main:app --reload --port 8000
```

Expected output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Application startup complete
```

#### Step 2: Start the Frontend

```bash
# From project root
streamlit run streamlit_app.py
```

Expected output:
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

### Running with Docker (Optional)

```bash
# Build the image
docker build -t ckd-ml .

# Run the container
docker run -p 8000:8000 -p 8501:8501 ckd-ml
```

---

## 📚 API Documentation

Once the FastAPI server is running, visit:
- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

### Endpoints

#### Health Check
```
GET /health
```

Response:
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

#### Prediction
```
POST /predict
```

**Request Body:**
```json
{
  "age": 48,
  "bp": 80,
  "sg": 1.020,
  "al": 1,
  "su": 0,
  "bgr": 121,
  "bu": 36,
  "sc": 1.2,
  "sod": 140,
  "pot": 4.0,
  "hemo": 15.4,
  "pcv": 44,
  "wbcc": 7800,
  "rbcc": 5.2,
  "rbc": "normal",
  "pc": "normal",
  "pcc": "notpresent",
  "ba": "notpresent",
  "htn": "yes",
  "dm": "yes",
  "cad": "no",
  "appet": "good",
  "pe": "no",
  "ane": "no"
}
```

**Response:**
```json
{
  "prediction": "ckd",
  "probability": {
    "ckd": 0.75,
    "notckd": 0.25
  },
  "confidence": 0.75
}
```

---

## 💻 Example Usage

### Using Python (requests)

```python
import requests

# Prepare patient data
payload = {
    "age": 48, "bp": 80, "sg": 1.020, "al": 1, "su": 0,
    "bgr": 121, "bu": 36, "sc": 1.2, "sod": 140, "pot": 4.0,
    "hemo": 15.4, "pcv": 44, "wbcc": 7800, "rbcc": 5.2,
    "rbc": "normal", "pc": "normal", "pcc": "notpresent",
    "ba": "notpresent", "htn": "yes", "dm": "yes",
    "cad": "no", "appet": "good", "pe": "no", "ane": "no"
}

# Make prediction
response = requests.post("http://127.0.0.1:8000/predict", json=payload)
result = response.json()

print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']:.2%}")
```

### Using cURL

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 48, "bp": 80, "sg": 1.020, "al": 1, "su": 0,
    "bgr": 121, "bu": 36, "sc": 1.2, "sod": 140, "pot": 4.0,
    "hemo": 15.4, "pcv": 44, "wbcc": 7800, "rbcc": 5.2,
    "rbc": "normal", "pc": "normal", "pcc": "notpresent",
    "ba": "notpresent", "htn": "yes", "dm": "yes",
    "cad": "no", "appet": "good", "pe": "no", "ane": "no"
  }'
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please make sure to update tests as appropriate.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📚 References

### Dataset
> Dua, D. & Graff, C. (2019). UCI Machine Learning Repository. University of California, Irvine. http://archive.ics.uci.edu/ml

### Reference Paper
> Rahman, M.M., Al-Amin, M., & Hossain, J. (2024). Machine learning models for chronic kidney disease diagnosis and prediction. Biomedical Signal Processing and Control, 87, 105368. DOI: 10.1016/j.bspc.2023.105368

### Learning Resources
- [scikit-learn Documentation](https://scikit-learn.org/)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/waleed-haider534">Waleed Haider</a>
</p>