import streamlit as st
import pickle
import pandas as pd

# --- Load model and encoders ---
with open("customer_churn_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]                  # RandomForestClassifier
feature_names = model_data["features_names"] # list of columns used during training

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

st.title("📊 Customer Churn Prediction Dashboard")

# --- Input fields ---
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, step=1)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, step=1.0)
total_charges = st.number_input("Total Charges", min_value=0.0, step=1.0)

# --- Prepare input dictionary ---
input_data = {
    "gender": gender,
    "SeniorCitizen": senior,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MultipleLines": multiple_lines,
    "InternetService": internet_service,
    "OnlineSecurity": online_security,
    "OnlineBackup": online_backup,
    "DeviceProtection": device_protection,
    "TechSupport": tech_support,
    "StreamingTV": streaming_tv,
    "StreamingMovies": streaming_movies,
    "Contract": contract,
    "PaperlessBilling": paperless_billing,
    "PaymentMethod": payment_method,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}

# --- Sidebar summary ---
st.sidebar.header("📋 Customer Profile")
for key, value in input_data.items():
    st.sidebar.write(f"**{key}:** {value}")

# --- Apply encoders ---
for col, encoder in encoders.items():
    if col in input_data:
        input_data[col] = encoder.transform([input_data[col]])[0]

# --- Convert to DataFrame with correct feature order ---
input_df = pd.DataFrame([[input_data[col] for col in feature_names]], columns=feature_names)

# --- Prediction ---
if st.button("Predict Churn"):
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0][1]

    prediction_label = "Churn" if prediction == 1 else "No Churn"

    # Color-coded output
    if prediction_label == "Churn":
        st.error(f"🔴 Prediction: {prediction_label}")
    else:
        st.success(f"🟢 Prediction: {prediction_label}")

    # Probability bar
    st.write("### Probability of Churn")
    st.progress(int(probability * 100))  # progress bar
    st.write(f"{probability:.2%}")       # percentage nicely formatted
