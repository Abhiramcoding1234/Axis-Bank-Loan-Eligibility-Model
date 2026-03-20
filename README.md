# Axis Bank - Loan Eligibility Prediction Portal 🏦

An end-to-end Machine Learning web application built with **Streamlit** and **Scikit-Learn**. 

## 🚀 Live Features
- **ML Backend**: Logistic Regression model with 83% accuracy.
- **Branded UI**: Official Axis Bank crimson theme with custom CSS and multi-tab navigation.
- **Business Logic Layer**: 7+ hard-rejection rules (CIBIL, Income, FOIR etc.) for safer lending decisions.
- **Reporting**: Automated `.txt` eligibility report generation with unique reference numbers.

## 📂 Project Files
- `app.py`: Main Streamlit application.
- `train_model.py`: Script to train the model and generate pkl files.
- `model.pkl`, `scaler.pkl`, `encoders.pkl`: Trained ML artifacts.
- `loan_train.csv`: Training dataset.
- `.streamlit/config.toml`: Custom theme configuration.

## 🛠️ Local Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```

---
*Disclaimer: This is a preliminary assessment tool for educational/demonstration purposes.*
