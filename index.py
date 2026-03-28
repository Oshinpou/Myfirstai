import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# --- 1. AI BACKEND (The Brain) ---
# Simple data: Square Feet vs Price (in $1000s)
X = np.array([[600], [800], [1000], [1200], [1500], [2000], [2500]])
y = np.array([150, 180, 220, 250, 310, 400, 500])

model = LinearRegression()
model.fit(X, y)

# --- 2. UI/UX FRONTEND (The Face) ---
st.set_page_config(page_title="Housely AI", page_icon="🏠")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #4A90E2; color: white; }
    .prediction-box { padding: 20px; border-radius: 15px; background-color: #e3f2fd; text-align: center; border: 1px solid #90caf9; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Housely AI Predictor")
st.write("Enter the house size below to get an instant AI-powered market valuation.")

# Input Section
sqft = st.number_input("Square Footage (sq ft)", min_value=500, max_value=5000, value=1500, step=50)

# Prediction Logic
prediction = model.predict([[sqft]])[0]

# UI Result Display
st.markdown("---")
st.markdown(f"""
    <div class="prediction-box">
        <h3 style='margin:0; color: #1565c0;'>Estimated Market Value</h3>
        <h1 style='margin:0; color: #0d47a1;'>${prediction:,.2f}k</h1>
    </div>
    """, unsafe_allow_html=True)

# Add a little UX "Trust" feature
st.caption("⚠️ This prediction is based on a Linear Regression model using local historical data.")
