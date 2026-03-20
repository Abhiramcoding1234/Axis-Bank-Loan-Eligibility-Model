import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# ── 1. Load data ────────────────────────────────────────────────────────────
df = pd.read_csv("loan_train.csv")
df.dropna(inplace=True)

# ── 2. Encode categorical columns ────────────────────────────────────────────
cat_cols = ["Gender", "Married", "Dependents", "Education", "Self_Employed", "Area"]
encoders = {}

for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# ── 3. Features & target ─────────────────────────────────────────────────────
X = df.drop(columns=["Status"])
y = df["Status"]

# ── 4. Scale features ────────────────────────────────────────────────────────
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── 5. Train / test split ────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# ── 6. Train model ───────────────────────────────────────────────────────────
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# ── 7. Evaluate ──────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {acc * 100:.1f}%")

# ── 8. Save pkl files ────────────────────────────────────────────────────────
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

with open("encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("✅ Saved: model.pkl, scaler.pkl, encoders.pkl")
