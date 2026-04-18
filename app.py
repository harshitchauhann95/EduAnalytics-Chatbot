import streamlit as st
import pandas as pd
import pickle

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="EduAnalytics Bot", 
    page_icon="🎓", 
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD ASSETS ---
@st.cache_resource
def load_assets():
    try:
        with open('models/student_model.pkl', 'rb') as f:
            model = pickle.load(f)
        with open('models/model_columns.pkl', 'rb') as f:
            cols = pickle.load(f)
        return model, cols
    except FileNotFoundError:
        st.error("Model files not found. Please check 'models/' directory.")
        return None, None

model, model_columns = load_assets()

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3413/3413535.png", width=100)
    st.title("Student Profile")
    st.info("Adjust the parameters below to update the prediction.")
    
    st.subheader("📊 Academic History")
    g1 = st.number_input("Unit Test / Mid-Term 1 (0-20)", 0, 20, 10)
    g2 = st.number_input("Unit Test / Mid-Term 2 (0-20)", 0, 20, 10)
    failures = st.selectbox("Backlogs / Previous Fails", [0, 1, 2, 3])
    
    st.subheader("🕒 Lifestyle Factors")
    absences = st.slider("Number of Days Absent", 0, 100, 0)
    studytime = st.select_slider("Weekly Study Time", 
                               options=[1, 2, 3, 4],
                               format_func=lambda x: ["<2h", "2-5h", "5-10h", ">10h"][x-1])
    goout = st.select_slider("Outing Frequency", 
                            options=[1, 2, 3, 4, 5],
                            format_func=lambda x: ["Very Low", "Low", "Neutral", "High", "Very High"][x-1])

# --- MAIN INTERFACE ---
st.title("🎓 EduAnalytics Dashboard")
st.markdown("Predict final student performance based on historical data and habits.")
st.divider()

if model is not None:
    # PREDICTION CALCULATION
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)
    input_df.at[0, 'G1'] = g1
    input_df.at[0, 'G2'] = g2
    input_df.at[0, 'absences'] = absences
    input_df.at[0, 'failures'] = failures
    input_df.at[0, 'studytime'] = studytime
    input_df.at[0, 'goout'] = goout
    
    prediction = model.predict(input_df)[0]
    prediction = max(0, min(20, prediction)) # Clamp between 0-20

    # DISPLAY RESULTS
    col_res1, col_res2, col_res3 = st.columns([1, 1, 1])
    
    with col_res1:
        st.metric(label="Predicted Final Grade", value=f"{prediction:.2f} / 20")
        
    with col_res2:
        status = "PASSING" if prediction >= 10 else "AT-RISK"
        st.metric(label="Status", value=status, delta=None if status == "PASSING" else "Action Needed", delta_color="inverse")

    with col_res3:
        avg_input = (g1 + g2) / 2
        improvement = prediction - avg_input
        st.metric(label="Projected Trend", value=f"{improvement:+.2f}", delta=f"{improvement:.2f}")

    # Visual Progress Bar
    st.write("### Performance Scale")
    progress_color = "green" if prediction >= 10 else "red"
    st.progress(prediction / 20)
    
    # Contextual Advice
    st.divider()
    with st.expander("💡 Insights & Recommendations"):
        if prediction < 10:
            st.warning("**Recommendation:** Based on current trends, the student is at risk of failing. Focus on reducing 'Outing Frequency' and increasing 'Study Time'.")
        else:
            st.success("**Recommendation:** The student is on track. To improve further, maintain current Grade 2 consistency.")
        
        st.write(f"- **Current Absences:** {absences}")
        st.write(f"- **Calculated Input Average:** {avg_input:.2f}")

else:
    st.warning("Waiting for model to load...")

# --- FOOTER ---
st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: grey;">
        <small>EduAnalytics Bot v2.0 | Data-Driven Academic Success</small>
    </div>
    """, unsafe_allow_html=True)
