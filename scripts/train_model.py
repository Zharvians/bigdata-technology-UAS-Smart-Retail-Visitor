import pandas as pd
import joblib
import os

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# ==================================================
# ABSOLUTE PATH
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

PARQUET_PATH = os.path.join(
    PROJECT_ROOT,
    "output",
    "ml_visitor"
)

MODEL_FOLDER = os.path.join(
    PROJECT_ROOT,
    "models"
)

os.makedirs(MODEL_FOLDER, exist_ok=True)

MODEL_PATH = os.path.join(
    MODEL_FOLDER,
    "visitor_prediction.pkl"
)

# ==================================================
# LOAD PARQUET
# ==================================================

df = pd.read_parquet(PARQUET_PATH)

print("\nDATASET ML")
print(df.head())

# ==================================================
# FEATURE & TARGET
# ==================================================

X = df[["hour"]]

y = df["visitor_count"]

# ==================================================
# SPLIT DATA
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==================================================
# TRAIN MODEL
# ==================================================

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

print("Intercept :", model.intercept_)
print("Coef :", model.coef_)

# ==================================================
# EVALUASI
# ==================================================

prediction = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    prediction
)

print("\nMAE :", round(mae, 2))

# ==================================================
# SAVE MODEL
# ==================================================

joblib.dump(
    model,
    MODEL_PATH
)

print("\nMODEL BERHASIL DISIMPAN")
print(MODEL_PATH)