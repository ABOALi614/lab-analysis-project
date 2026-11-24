"""تحميل الموديل والتنبؤ."""
import json
from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "model" / "cbc_model.joblib"
META_PATH = BASE_DIR / "model" / "model_meta.json"


def model_files_exist() -> bool:
    return MODEL_PATH.exists() and META_PATH.exists()


@st.cache_resource(show_spinner=False)
def load_model_and_meta():
    """يتحمل مرة واحدة بس ويفضل في الذاكرة."""
    import joblib  # استيراد متأخر عشان الصفحة تفتح أسرع

    model = joblib.load(MODEL_PATH)
    with open(META_PATH, encoding="utf-8") as f:
        meta = json.load(f)
    return model, meta


def sklearn_mismatch(meta):
    """لو إصدار scikit-learn وقت التدريب غير الإصدار الحالي يرجع (تدريب، حالي)."""
    import sklearn

    trained = meta.get("sklearn_version")
    if trained and trained != sklearn.__version__:
        return trained, sklearn.__version__
    return None


def predict(values: dict):
    """values: {HGB: .., RBC: .., ...} -> (الحالة الأعلى، ثقتها، قاموس كل الاحتمالات)."""
    model, meta = load_model_and_meta()
    features = meta["features"]
    X = pd.DataFrame([[float(values[f]) for f in features]], columns=features)
    proba = model.predict_proba(X)[0]
    probs = {str(c): float(p) for c, p in zip(model.classes_, proba)}
    top = max(probs, key=probs.get)
    return top, probs[top], probs
