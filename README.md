[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge.svg)](https://harshitchauhann95-eduanalytics-chatbot-app-btc5ur.streamlit.app/)
[![GitHub stars](https://img.shields.io/github/stars/harshitchauhann95/EduAnalytics-Chatbot?style=social)](https://github.com/harshitchauhann95/EduAnalytics-Chatbot/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/harshitchauhann95/EduAnalytics-Chatbot?style=social)](https://github.com/harshitchauhann95/EduAnalytics-Chatbot/network/members)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub repo size](https://img.shields.io/github/repo-size/harshitchauhann95/EduAnalytics-Chatbot)](https://github.com/harshitchauhann95/EduAnalytics-Chatbot)
[![GitHub last commit](https://img.shields.io/github/last-commit/harshitchauhann95/EduAnalytics-Chatbot)](https://github.com/harshitchauhann95/EduAnalytics-Chatbot)

### 🎓 EduAnalytics-Chatbot

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
## 📸 Interface Preview
<img width="1440" height="789" alt="Screenshot 2026-04-19 at 3 43 45 AM" src="https://github.com/user-attachments/assets/cb7d1957-b405-46a5-93b1-4dc97fff262f" />


---
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
