# Chronic Kidney Disease (CKD) Prediction System

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit-learn-1.8.0-orange.svg)](https://scikit-learn.org/)
[![LightGBM](https://img.shields.io/badge/LightGBM-4.5.0-green.svg)](https://lightgbm.readthedocs.io/)
[![XGBoost](https://img.shields.io/badge/XGBoost-2.8.0-red.svg)](https://xgboost.readthedocs.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance machine learning system for predicting Chronic Kidney Disease (CKD) based on clinical and laboratory measurements. The system achieves exceptional performance with multiple ensemble models, with LightGBM delivering perfect accuracy on the test dataset.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Model Results](#model-results)
5. [Project Structure](#project-structure)
6. [Installation](#installation)
7. [Usage](#usage)
   - [Loading the Model](#loading-the-model)
   - [Making Predictions](#making-predictions)
   - [Running the Notebooks](#running-the-notebooks)
8. [Model Details](#model-details)
   - [Preprocessing Pipeline](#preprocessing-pipeline)
   - [Hyperparameters](#hyperparameters)
   - [Evaluation Methodology](#evaluation-methodology)
9. [Reports & Visualizations](#reports--visualizations)
10. [Technical Notes](#technical-notes)
11. [License](#license)
12. [Authors](#authors)
13. [Acknowledgments](#acknowledgments)

---

## 🔍 Overview

Chronic Kidney Disease (CKD) is a global health concern affecting millions of people worldwide. Early detection and diagnosis are critical for effective treatment and management of the disease. This project implements a complete machine learning pipeline for CKD prediction using clinical and laboratory data.

The system includes:
- **Comprehensive data preprocessing** with categorical encoding and KNN imputation
- **Seven ensemble machine learning models** for comparison
- **Stratified cross-validation** to ensure robust model evaluation
- **Detailed model evaluation** with multiple metrics
- **Deployment-ready** saved model artifacts

### Key Highlights

- ✅ **2,500 patient records** with 24 clinical features
- ✅ **7 different ML models** compared
- ✅ **100% accuracy** achieved with LightGBM
- ✅ **5-fold cross-validation** for robust evaluation
- ✅ **Pipeline-based preprocessing** to prevent data leakage

---

## 🚀 Features

- **Multiple Model Support**: Compare 7 different ensemble algorithms
- **Automated Preprocessing**: Built-in categorical encoding and missing value imputation
- **Cross-Validation**: Stratified K-Fold for reliable performance estimates
- **Model Persistence**: Save and load models using joblib
- **Visualization Reports**: Generate comprehensive performance charts
- **Production Ready**: Pipeline encapsulation for seamless deployment

---

## 📊 Dataset

The project uses the Chronic Kidney Disease dataset from clinical records. The dataset has been preprocessed to handle missing values and categorical variables.

### Dataset Summary

| Attribute | Value |
|-----------|-------|
| Total Samples | 2,500 |
| Features | 24 |
| Target Classes | 2 (CKD / Not CKD) |
| Class Distribution | 1,566 CKD (62.6%), 934 Not CKD (37.4%) |
| Train Set Size | 2,000 samples (80%) |
| Test Set Size | 500 samples (20%) |

### Feature Description

The dataset includes 24 clinical features covering various aspects of patient health:

#### Demographics
| Feature | Description | Type |
|---------|-------------|------|
| `age` | Age of the patient | Numeric |

#### Vital Signs
| Feature | Description | Type |
|---------|-------------|------|
| `bp` | Blood Pressure | Numeric |

#### Urinalysis
| Feature | Description | Type |
|---------|-------------|------|
| `sg` | Specific Gravity | Numeric |
| `al` | Albumin | Numeric |
| `su` | Sugar | Numeric |
| `rbc` | Red Blood Cells | Categorical |
| `pc` | Pus Cell | Categorical |
| `pcc` | Pus Cell Clumps | Categorical |
| `ba` | Bacteria | Categorical |

#### Blood Chemistry
| Feature | Description | Type |
|---------|-------------|------|
| `bgr` | Blood Glucose Random | Numeric |
| `bu` | Blood Urea | Numeric |
| `sc` | Serum Creatinine | Numeric |
| `sod` | Sodium | Numeric |
| `pot` | Potassium | Numeric |

#### Hematology
| Feature | Description | Type |
|---------|-------------|------|
| `hemo` | Hemoglobin | Numeric |
| `pcv` | Packed Cell Volume | Numeric |
| `wbcc` | White Blood Cell Count | Numeric |
| `rbcc` | Red Blood Cell Count | Numeric |

#### Clinical Conditions
| Feature | Description | Type |
|---------|-------------|------|
| `htn` | Hypertension | Categorical |
| `dm` | Diabetes Mellitus | Categorical |
| `cad` | Coronary Artery Disease | Categorical |
| `appet` | Appetite | Categorical |
| `pe` | Pedal Edema | Categorical |
| `ane` | Anemia | Categorical |

---

## 📈 Model Results

The following table shows the comprehensive comparison of all 7 trained models. Results are sorted by F1 Macro score in descending order.

| Model | Accuracy | Precision | Recall | F1 Macro | ROC-AUC | CV F1 Mean | CV F1 Std |
|-------|----------|-----------|--------|----------|---------|------------|-----------|
| **LightGBM** 🏆 | **100.00%** | **100.00%** | **100.00%** | **100.00%** | **100.00%** | 99.73% | ±0.17% |
| XGBoost | 99.80% | 99.73% | 99.84% | 99.79% | 100.00% | 99.68% | ±0.20% |
| Random Forest | 99.60% | 99.68% | 99.47% | 99.57% | 99.99% | 99.41% | ±0.26% |
| Voting Classifier | 99.40% | 99.41% | 99.31% | 99.36% | 100.00% | 99.36% | ±0.36% |
| Stacking Classifier | 99.40% | 99.41% | 99.31% | 99.36% | 100.00% | 99.57% | ±0.27% |
| Gradient Boosting | 99.20% | 99.15% | 99.15% | 99.15% | 99.99% | 98.82% | ±0.50% |
| AdaBoost | 98.20% | 97.85% | 98.35% | 98.09% | 99.96% | 98.72% | ±0.20% |

### 🏆 Best Model: LightGBM

The **LightGBM** classifier achieved **perfect 100% accuracy** on the held-out test set, making it the best-performing model for this dataset.

#### Performance Metrics

| Metric | Score |
|--------|-------|
| Accuracy | 100.00% |
| Precision | 100.00% |
| Recall | 100.00% |
| F1 Macro | 100.00% |
| ROC-AUC | 100.00% |
| Cross-Validation F1 Mean | 99.73% |
| Cross-Validation F1 Std | ±0.17% |

#### Classification Report

```
              precision    recall  f1-score   support

         ckd       1.00      1.00      1.00       313
       notckd       1.00      1.00      1.00       187

    accuracy                           1.00       500
   macro avg       1.00      1.00      1.00       500
weighted avg       1.00      1.00      1.00       500
```

---

## 📁 Project Structure

```
CKD-ML/
│
├── README.md                     # This file
│
├── artifacts/
│   └── final_model.joblib       # Saved LightGBM model (best performer)
│
├── notebooks/
│   ├── data/
│   │   └── kidney_disease.csv  # Dataset (2,500 samples, 24 features)
│   │
│   ├── ml_v0.ipynb              # Initial data exploration & visualization
│   │   ├── Data loading and cleaning
│   │   ├── Missing value analysis
│   │   ├── Class distribution analysis
│   │   ├── Feature correlation heatmap
│   │   └── Numeric feature distributions
│   │
│   ├── ml_v1.ipynb              # Hyperparameter tuning
│   │   ├── KNN Imputer optimization
│   │   ├── Random Forest hyperparameter search
│   │   ├── GridSearchCV implementation
│   │   └── Best parameters identification
│   │
│   └── ml_v2.ipynb              # Final model training & evaluation
│       ├── All 7 models training
│       ├── Cross-validation
│       ├── Model comparison
│       ├── Best model selection
│       └── Model persistence
│
├── report/                       # Generated visualizations
│   ├── categorical_features.png     # Categorical feature analysis
│   ├── class_distribution.png       # Target class distribution
│   ├── confusion_matrix.png         # Best model confusion matrix
│   ├── correlation_heatmap.png      # Feature correlations
│   ├── feature_importance.png       # Feature importance scores
│   ├── model_comparison.png         # All models comparison chart
│   ├── model_results.csv            # Detailed results table
│   ├── missing_values.png           # Missing values visualization
│   └── numeric_distributions.png    # Numeric feature distributions
│
└── .venv/                        # Virtual environment (Python 3.11+)
```

---

## 💾 Installation

### Prerequisites

- **Python 3.11** or higher
- **Windows 10/11**, **macOS**, or **Linux**

### Quick Start


1. Clone the repository and navigate to the project folder
   cd CKD-ML

2. Create virtual environment:
   ```bash
   uv init 
   python -m venv .venv
   ```
3. Activate the environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies:
   ```bash
   pip install pandas numpy scikit-learn xgboost lightgbm matplotlib seaborn joblib
   ```
5. RUN Frontend and backend 
   uv run main.py


### Required Packages

| Package | Version | Purpose |
|---------|---------|---------|
| pandas | - | Data manipulation |
| numpy | - | Numerical computing |
| scikit-learn | 1.8.0 | Machine learning |
| xgboost | 2.8.0 | XGBoost classifier |
| lightgbm | 4.5.0 | LightGBM classifier |
| matplotlib | - | Visualization |
| seaborn | - | Statistical graphics |
| joblib | - | Model persistence |

---

## 🎯 Usage

### Loading the Model

The trained LightGBM model is saved as `artifacts/final_model.joblib`. You can load it and use it for predictions:

```python
import joblib
import pandas as pd
import numpy as np

# Load the saved model
model = joblib.load('artifacts/final_model.joblib')

print("Model loaded successfully!")
print(f"Model type: {type(model)}")
```

### Making Predictions

Here's how to make predictions for new patient data:

```python
import joblib
import pandas as pd
import numpy as np

# Load the model
model = joblib.load('artifacts/final_model.joblib')

# Prepare new patient data (24 features in correct order)
new_patient = pd.DataFrame({
    'age': [55],
    'bp': [80],
    'sg': [1.015],
    'al': [2],
    'su': [1],
    'rbc': [0],        # encoded: 0=abnormal, 1=normal
    'pc': [1],         # encoded: 0=abnormal, 1=normal
    'pcc': [0],        # encoded: 0=notpresent, 1=present
    'ba': [0],         # encoded: 0=notpresent, 1=present
    'bgr': [140],
    'bu': [25],
    'sc': [1.2],
    'sod': [138],
    'pot': [4.5],
    'hemo': [12],
    'pcv': [38],
    'wbcc': [7000],
    'rbcc': [4.2],
    'htn': [1],        # encoded: 0=no, 1=yes
    'dm': [0],         # encoded: 0=no, 1=yes
    'cad': [0],        # encoded: 0=no, 1=yes
    'appet': [1],      # encoded: 0=poor, 1=good
    'pe': [0],         # encoded: 0=no, 1=yes
    'ane': [0]         # encoded: 0=no, 1=yes
})

# Ensure column order matches training data
new_patient = new_patient[model.named_steps['clf'].feature_names_in_]

# Make prediction
prediction = model.predict(new_patient)
probability = model.predict_proba(new_patient)[:, 1]

# Display results
class_labels = {0: 'CKD (Chronic Kidney Disease)', 1: 'Not CKD (Healthy)'}
print(f"Patient Prediction: {class_labels[prediction[0]]}")
print(f"CKD Probability: {probability[0]:.2%}")
print(f"Healthy Probability: {1 - probability[0]:.2%}")
```

### Running the Notebooks

Open and run the Jupyter notebooks in sequential order:

1. **Data Exploration** (`ml_v0.ipynb`):
   - Load and clean the dataset
   - Analyze missing values
   - Visualize feature distributions
   - Generate correlation heatmap

2. **Hyperparameter Tuning** (`ml_v1.ipynb`):
   - Optimize KNN imputer parameters
   - GridSearchCV for Random Forest
   - Identify best hyperparameters

3. **Final Model Training** (`ml_v2.ipynb`):
   - Train all 7 ensemble models
   - Perform 5-fold cross-validation
   - Compare model performances
   - Save the best model

```bash
# Start Jupyter Notebook
jupyter notebook

# Or open a specific notebook
jupyter notebook notebooks/ml_v2.ipynb
```

---

## ⚙️ Model Details

### Preprocessing Pipeline

The model uses a scikit-learn Pipeline that encapsulates all preprocessing steps, ensuring no data leakage during cross-validation:

1. **Categorical Encoding**: Label encoding for 10 categorical features
   - Features: `rbc`, `pc`, `pcc`, `ba`, `htn`, `dm`, `cad`, `appet`, `pe`, `ane`
   - Missing values filled with 'missing' category before encoding

2. **Missing Value Imputation**: KNN Imputer with k=3 neighbors
   - Uses Euclidean distance for finding nearest neighbors
   - Applied within the pipeline to prevent data leakage

3. **Feature Standardization**: Feature names converted to strings for compatibility

### Hyperparameters

#### LightGBM (Best Configuration)

```python
{
    'clf__n_estimators': 100,
    'clf__max_depth': 5,
    'clf__learning_rate': 0.1,
    'clf__reg_alpha': 0.1,
    'clf__reg_lambda': 0.1,
    'imputer__n_neighbors': 3
}
```

#### Other Models Tested

| Model | Key Hyperparameters |
|-------|---------------------|
| XGBoost | n_estimators=100, max_depth=5, learning_rate=0.1 |
| Random Forest | n_estimators=100, max_depth=5, max_features='sqrt' |
| Gradient Boosting | n_estimators=100, max_depth=5, learning_rate=0.1 |
| AdaBoost | n_estimators=100, learning_rate=0.1 |
| Voting Classifier | Soft voting with RF, GB, XGB |
| Stacking Classifier | Meta-learner: Logistic Regression |

### Evaluation Methodology

- **Train/Test Split**: 80/20 with stratified sampling to maintain class balance
- **Cross-Validation**: 5-fold Stratified K-Fold
- **Primary Metric**: F1 Macro (balances precision and recall for both classes)
- **Validation Strategy**: Held-out test set to confirm cross-validation results
- **Random State**: 42 for reproducibility

---

## 📉 Reports & Visualizations

The project automatically generates comprehensive visualization reports in the `report/` directory:

| File | Description |
|------|-------------|
| `model_comparison.png` | Bar chart comparing all metrics across models |
| `confusion_matrix.png` | Confusion matrix for the best model (LightGBM) |
| `correlation_heatmap.png` | Heatmap showing feature correlations |
| `class_distribution.png` | Pie chart of CKD vs Not CKD distribution |
| `missing_values.png` | Bar chart showing missing values per feature |
| `numeric_distributions.png` | Histograms of numeric feature distributions |
| `categorical_features.png` | Count plots for categorical features |
| `feature_importance.png` | Feature importance scores from Random Forest |

---

## 📝 Technical Notes

### Data Leakage Prevention

- The KNN Imputer is included inside the Pipeline, ensuring it's fitted only on training data during cross-validation
- Test data is transformed using the imputer fitted during training
- No data leakage occurs between training and evaluation phases

### Model Performance Considerations

⚠️ **Important**: The 100% accuracy achieved by LightGBM should be interpreted with caution:

1. **Possible Causes**:
   - The dataset may have highly separable classes
   - Some features might be strong predictors (potential leakage)
   - The dataset size (2,500 samples) may be sufficient for the task

2. **Recommendations for Production**:
   - Validate on external datasets
   - Perform feature ablation studies
   - Consider model interpretability (SHAP values)
   - Implement proper train/validation/test splits

### Reproducibility

All experiments use `random_state=42` for reproducibility:
- Train/test split
- Cross-validation folds
- All ML models

---

## 📄 License

This project is licensed under the MIT License.

---

## 👥 Authors

- **Waleed Haider** - Primary Developer

---

## 🙏 Acknowledgments

- Dataset source: UCI Machine Learning Repository / Clinical data
- Built with the following open-source libraries:
  - [scikit-learn](https://scikit-learn.org/) - Machine learning
  - [XGBoost](https://xgboost.readthedocs.io/) - Gradient boosting
  - [LightGBM](https://lightgbm.readthedocs.io/) - Light gradient boosting
  - [pandas](https://pandas.pydata.org/) - Data manipulation
  - [matplotlib](https://matplotlib.org/) - Visualization
  - [seaborn](https://seaborn.pydata.org/) - Statistical graphics