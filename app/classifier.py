from functools import lru_cache
from pathlib import Path
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

MODEL_PATH = Path(__file__).parent.parent / "artifacts" / "final_model.joblib"
LABELS = ["ckd", "notckd"]

NUMERIC_FEATURES = [
    "age", "bp", "sg", "al", "su",
    "bgr", "bu", "sc", "sod", "pot",
    "hemo", "pcv", "wbcc", "rbcc"
]

CATEGORICAL_FEATURES = [
    "rbc", "pc", "pcc", "ba",
    "htn", "dm", "cad", "appet", "pe", "ane"
]

CATEGORICAL_MAPPING = {
    "rbc":   {"normal": 1, "abnormal": 0, "missing": 2},
    "pc":    {"normal": 1, "abnormal": 0, "missing": 2},
    "pcc":   {"present": 1, "notpresent": 0, "missing": 2},
    "ba":    {"present": 1, "notpresent": 0, "missing": 2},
    "htn":   {"yes": 1, "no": 0, "missing": 2},
    "dm":    {"yes": 1, "no": 0, "missing": 2},
    "cad":   {"yes": 1, "no": 0, "missing": 2},
    "appet": {"good": 1, "poor": 0, "missing": 2},
    "pe":    {"yes": 1, "no": 0, "missing": 2},
    "ane":   {"yes": 1, "no": 0, "missing": 2},
}

# Must match order used in model training
ALL_FEATURES = [
    "age", "bp", "sg", "al", "su", "rbc", "pc", "pcc", "ba",
    "bgr", "bu", "sc", "sod", "pot", "hemo", "pcv", "wbcc", "rbcc",
    "htn", "dm", "cad", "appet", "pe", "ane"
]

@lru_cache
def load_model():
    return joblib.load(MODEL_PATH)


def preprocess(features: dict) -> pd.DataFrame:
    row = {}
    for col in ALL_FEATURES:
        if col in CATEGORICAL_MAPPING:
            val = str(features.get(col, "missing")).strip().lower()
            row[col] = CATEGORICAL_MAPPING[col].get(val, 2)
        else:
            val = features.get(col)
            row[col] = float(val) if val not in (None, "", "?") else float("nan")
    
    return pd.DataFrame([row], columns=ALL_FEATURES)


def predict(features: dict) -> dict:
    X = preprocess(features)
    model = load_model()
    proba = model.predict_proba(X)[0]
    idx = int(proba.argmax())
    return {
        "label": LABELS[idx],
        "class_index": idx,
        "probabilities": {
            "ckd": round(float(proba[0]), 4),
            "notckd": round(float(proba[1]), 4)
        },
        "confidence": round(float(proba[idx]), 4),
    }