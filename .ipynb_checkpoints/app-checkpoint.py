import streamlit as st
import pandas as pd
import pickle

# --- PAGE CONFIG ---
st.set_page_config(page_title="EduAnalytics Bot", layout="centered")

# --- LOAD THE EXPORTED MODEL ---
@st.cache_resource
def load_assets():
    with open('student_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('model_columns.pkl', 'rb') as f:
        cols = pickle.load(f)
    return model, cols

model, model_columns = load_assets()

# --- WEB INTERFACE ---
st.title("🎓 EduAnalytics Web Predictor")
st.write("Enter your details below to see your predicted final grade.")

# Create two columns for a cleaner layout
col1, col2 = st.columns(2)

with col1:
    g1 = st.number_input("Grade 1 (0-20)", 0, 20, 10)
    g2 = st.number_input("Grade 2 (0-20)", 0, 20, 10)
    absences = st.number_input("Absences", 0, 100, 0)

with col2:
    failures = st.selectbox("Past Failures", [0, 1, 2, 3])
    studytime = st.slider("Weekly Study (1: <2h, 4: >10h)", 1, 4, 2)
    goout = st.slider("Friends Outing (1: Low, 5: High)", 1, 5, 3)

# --- PREDICTION LOGIC ---
if st.button("Calculate Prediction"):
    # Create a DataFrame with 0s for all features
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    
    # Fill in the user inputs
    input_df.at[0, 'G1'] = g1
    input_df.at[0, 'G2'] = g2
    input_df.at[0, 'absences'] = absences
    input_df.at[0, 'failures'] = failures
    input_df.at[0, 'studytime'] = studytime
    input_df.at[0, 'goout'] = goout
    
    prediction = model.predict(input_df)[0]
    
    st.divider()
    st.header(f"Predicted Grade: {prediction:.2f}/20")
    
    if prediction >= 10:
        st.success("Result: PASSING")
    else:
        st.error("Result: AT-RISK")