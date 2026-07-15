# 📊 Customer Churn Prediction App

A machine learning web application that predicts whether a telecom customer is likely to **churn (leave the service)** or **stay**, based on their demographic details, subscribed services, contract type, and billing information. Built with **Streamlit** for an interactive and user-friendly experience.

---

Link : https://customer-churn-prediction-model-by-anishambad.streamlit.app/

## 📝 Description

Customer churn is one of the biggest challenges faced by telecom companies. Identifying customers who are likely to churn allows businesses to take proactive retention measures. This app uses a **Random Forest Classifier** trained on historical telecom customer data to predict churn in real time based on user-provided inputs.

---

## ✨ Features

- 🎛️ Interactive UI to input customer details (demographics, services, billing, contract type)
- 🌲 Predicts customer churn using a trained Random Forest model
- 📈 Displays prediction probability/confidence score
- 🎨 Color-coded results (e.g., red for churn risk, green for retained customer)
- 📊 Visual progress bar representing churn probability
- 📋 Sidebar summary of all customer inputs for quick reference
- ⚡ Fast, real-time predictions with a lightweight web interface

---

## 🛠️ Tech Stack

| Component            | Technology                     |
|-----------------------|---------------------------------|
| Programming Language  | Python                          |
| Machine Learning      | scikit-learn (Random Forest)    |
| Web Framework         | Streamlit                       |
| Data Handling         | pandas                          |
| Model Serialization   | pickle / joblib                 |

---

## ⚙️ Installation

Follow these steps to set up the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/customer-churn-prediction-app.git

# 2. Navigate into the project directory
cd customer-churn-prediction-app

# 3. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# 4. Install required dependencies
pip install -r requirements.txt
```

**`requirements.txt`** should include:

```
streamlit
pandas
scikit-learn
numpy
```

---

## ▶️ How to Run the App Locally

Once dependencies are installed and the model files (`customer_churn_model.pkl` and `encoders.pkl`) are present in the project directory, run:

```bash
streamlit run app.py
```

The app will open automatically in your default browser at:

```
http://localhost:8501
```

---

## 💡 Example Usage

1. Open the app in your browser.
2. Use the sidebar/input form to enter customer details such as:
   - Gender, Senior Citizen status, Partner, Dependents
   - Tenure (months with the company)
   - Phone Service, Internet Service type
   - Contract type (Month-to-month, One year, Two year)
   - Payment Method
   - Monthly Charges and Total Charges
3. Click the **Predict** button.
4. The app will:
   - Encode your categorical inputs using the saved encoders
   - Feed the processed data into the trained Random Forest model
   - Display the result as **"Churn"** or **"No Churn"**
   - Show a probability/confidence score with a color-coded progress bar
5. The sidebar will display a summary of all the inputs used for that prediction.

**Sample scenario:**
> A customer with a month-to-month contract, low tenure (3 months), high monthly charges, and electronic check payment method is more likely to be flagged as **"Churn"** with a high probability score — reflecting real-world churn patterns.

---

## 🖼️ Screenshots

> _Add screenshots of your app here to showcase the UI and predictions._

| Home Page | Prediction Result |
|-----------|-------------------|
| ![Home Page]("C:\Users\anish\OneDrive\Pictures\Screenshots\Screenshot 2026-07-15 154357.png") | ![Prediction Result]("C:\Users\anish\OneDrive\Pictures\Screenshots\Screenshot 2026-07-15 154420.png") |

---

## 🌲 Model Explanation: Random Forest

### What is Random Forest?

Random Forest is an **ensemble learning algorithm** that builds multiple decision trees during training and combines their outputs to make a final prediction. Instead of relying on a single decision tree (which can overfit or be unstable), Random Forest aggregates the predictions of many trees using **majority voting** (for classification tasks), resulting in a more accurate and robust model.

### How the Model Predicts Churn — Step by Step

1. **Input Features**
   The user provides customer details through the Streamlit UI, including:
   - Demographics (gender, senior citizen, partner, dependents)
   - Services subscribed (phone service, internet service, etc.)
   - Contract and billing details (contract type, payment method, monthly charges, total charges, tenure)

2. **Encoding Categorical Values**
   Categorical inputs (like gender, contract type, payment method) are transformed into numerical format using the saved `encoders.pkl` file, ensuring consistency with how the data was encoded during training.

3. **Prediction by Individual Trees**
   The encoded feature set is passed to the trained Random Forest model (`customer_churn_model.pkl`). Each decision tree in the forest independently analyzes the input and makes its own prediction (Churn or No Churn).

4. **Aggregation via Majority Voting**
   The Random Forest aggregates predictions from all individual trees. The final output class is determined by **majority vote** — whichever class (Churn/No Churn) receives the most votes from the trees becomes the final prediction.

5. **Final Output**
   - `1` → **Churn** (customer likely to leave)
   - `0` → **No Churn** (customer likely to stay)

6. **Probability Score**
   Alongside the class label, the model also outputs a **probability score**, representing the model's confidence in its prediction (e.g., 78% probability of churn). This is visually represented using a color-coded progress bar in the app.

### Why Random Forest Was Chosen

- ✅ **Handles both categorical and numerical features** effectively after encoding
- ✅ **Reduces overfitting** compared to a single decision tree, thanks to averaging/voting across multiple trees
- ✅ **Robust to noise and outliers** in customer data
- ✅ **Provides feature importance scores**, helping identify which factors (e.g., contract type, tenure) most influence churn
- ✅ **Good balance of accuracy and interpretability** for business use cases like churn analysis

---

## 🚀 Future Improvements

- ☁️ Deploy the app on **Streamlit Cloud** for public access
- 🤖 Add and compare additional models (Logistic Regression, XGBoost, Gradient Boosting)
- 📊 Add exploratory data analysis (EDA) dashboard for churn trends
- 🧠 Implement model explainability using SHAP or LIME
- 🗄️ Connect to a live database for real-time customer data instead of manual input
- 🌐 Add multi-language support for wider accessibility
- 📱 Improve mobile responsiveness of the UI

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute this project with proper attribution.

```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software, subject to including the above copyright notice in all copies.
```

---

### ⭐ If you found this project helpful, consider giving it a star on GitHub!
