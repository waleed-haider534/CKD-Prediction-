from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from pathlib import Path
from classifier import load_model, predict, ALL_FEATURES, LABELS


class PatientFeatures(BaseModel):
    # Numeric
    age:  float = Field(..., description="Age in years")
    bp:   float = Field(..., description="Blood Pressure (mmHg)")
    sg:   float = Field(..., description="Specific Gravity")
    al:   float = Field(..., description="Albumin (0-5)")
    su:   float = Field(..., description="Sugar (0-5)")
    bgr:  float = Field(..., description="Blood Glucose Random (mg/dL)")
    bu:   float = Field(..., description="Blood Urea (mg/dL)")
    sc:   float = Field(..., description="Serum Creatinine (mg/dL)")
    sod:  float = Field(..., description="Sodium (mEq/L)")
    pot:  float = Field(..., description="Potassium (mEq/L)")
    hemo: float = Field(..., description="Hemoglobin (g/dL)")
    pcv:  float = Field(..., description="Packed Cell Volume (%)")
    wbcc: float = Field(..., description="White Blood Cell Count")
    rbcc: float = Field(..., description="Red Blood Cell Count")
    # Categorical
    rbc:   str = Field(..., description="normal/abnormal")
    pc:    str = Field(..., description="normal/abnormal")
    pcc:   str = Field(..., description="present/notpresent")
    ba:    str = Field(..., description="present/notpresent")
    htn:   str = Field(..., description="yes/no")
    dm:    str = Field(..., description="yes/no")
    cad:   str = Field(..., description="yes/no")
    appet: str = Field(..., description="good/poor")
    pe:    str = Field(..., description="yes/no")
    ane:   str = Field(..., description="yes/no")


class Prediction(BaseModel):
    label: str
    class_index: int
    probabilities: dict
    confidence: float


class ModelInfo(BaseModel):
    features: list[str]
    labels: list[str]
    model_type: str
    n_features: int
    n_classes: int


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model()
    yield


app = FastAPI(
    title="CKD Prediction API",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "CKD Prediction API", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/model/info", response_model=ModelInfo)
def model_info():
    model = load_model()
    return {
        "features": ALL_FEATURES,
        "labels": LABELS,
        "model_type": type(model).__name__,
        "n_features": len(ALL_FEATURES),
        "n_classes": len(LABELS),
    }


@app.post("/predict", response_model=Prediction)
def predict_single(payload: PatientFeatures):
    return predict(payload.model_dump())