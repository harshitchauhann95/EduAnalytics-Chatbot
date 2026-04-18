### 🎓 EduAnalytics-Chatbot

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://harshitchauhann95-eduanalytics-chatbot-app-btc5ur.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

EduAnalytics-Chatbot is a Machine Learning-powered web application designed to predict student academic performance. By analyzing internal assessment scores and lifestyle factors, the tool provides early warnings for students who might be at risk, allowing for timely academic intervention.

🔗 **Live Demo:** [EduAnalytics Web Predictor](https://harshitchauhann95-eduanalytics-chatbot-app-btc5ur.streamlit.app/)

---

## 🚀 Key Features

- **Performance Prediction:** Uses regression models to predict final grades based on mid-term performance.
- **Interactive Dashboard:** A clean, user-friendly interface built with Streamlit.
- **Contextual Insights:** Specifically tailored for the Indian education system (Sessional/Mid-term inputs).
- **Risk Assessment:** Categorizes students into "PASSING" or "AT-RISK" groups.
- **Lifestyle Analysis:** Factors in attendance, study time, and social habits to provide a holistic view.

## 🛠️ Technical Stack

- **Language:** Python
- **Machine Learning:** Scikit-learn (Linear Regression / Random Forest)
- **Data Handling:** Pandas, NumPy
- **Web Framework:** Streamlit
- **Model Serialization:** Pickle

## 📊 Dataset Information

The model is trained on student performance data (inspired by the UCI Student Performance Dataset), which includes:
- **Academic Data:** Mid-term grades (Sessional 1 & 2), past backlogs.
- **Behavioral Data:** Study time, attendance, outings with friends, and health status.

## 📂 Project Structure

```text
EduAnalytics-Chatbot/
├── models/
│   ├── student_model.pkl    # Pre-trained ML model
│   └── model_columns.pkl    # Feature list for alignment
├── app.py                   # Streamlit web application
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```
## ⚙️ Installation & Setup

**Clone the repository:**
```bash
git clone [https://github.com/harshitchauhann95/EduAnalytics-Chatbot.git](https://github.com/harshitchauhann95/EduAnalytics-Chatbot.git)
cd EduAnalytics-Chatbot
```
## ⚙️ Installation & Setup

**Create a virtual environment (Optional but recommended):**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```
**Install dependencies:**
```bash
pip install -r requirements.txt
```
**Run the application:**
```bash
streamlit run app.py
```
## 📝 Usage

1. **Open the sidebar** in the web app.
2. **Enter the Sessional/Mid-term marks** (0-20 scale).
3. **Adjust the Attendance Shortage and Study Time** sliders.
4. **View the Predicted Final Grade and Status** on the main dashboard.

## 🤝 Contributing

Contributions are welcome! If you have suggestions for improving the model accuracy or UI enhancements:

* **Fork** the Project.
* **Create your Feature Branch** (`git checkout -b feature/NewFeature`).
* **Commit your Changes** (`git commit -m 'Add some NewFeature'`).
* **Push to the Branch** (`git push origin feature/NewFeature`).
* **Open a Pull Request**.

---
**Developed by Harshit Chauhan** *BTech Computer Science Engineering Student*
