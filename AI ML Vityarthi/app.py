import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

from suggestion_engine import give_suggestions, generate_study_plan, get_grade, get_result

# Load trained model
model = joblib.load("model.pkl")

# Page config
st.set_page_config(page_title="Student Performance Predictor", layout="centered")

# Title
st.title("🎓 AI-Based Student Performance Predictor")
st.write("Enter student details to predict performance and get personalized suggestions")

# ---------------- INPUT SECTION ---------------- #

st.subheader("📥 Enter Student Details")

attendance = st.slider("Attendance (%)", 0, 100, 75)
study_hours = st.slider("Study Hours per Day", 0.0, 10.0, 2.0)
previous_score = st.slider("Previous Score", 0, 100, 60)
assignments = st.slider("Assignment Completion (%)", 0, 100, 70)
sleep = st.slider("Sleep Hours per Day", 0.0, 12.0, 7.0)
screen_time = st.slider("Screen Time (hours/day)", 0.0, 12.0, 4.0)
consistency = st.slider("Study Consistency (days/week)", 0, 7, 4)
stress = st.slider("Stress Level (1-10)", 1, 10, 5)

# ---------------- PREDICTION ---------------- #

if st.button("🔍 Predict Performance"):

    # Store input
    data = {
        "attendance": attendance,
        "study_hours": study_hours,
        "previous_score": previous_score,
        "assignments": assignments,
        "sleep": sleep,
        "screen_time": screen_time,
        "consistency": consistency,
        "stress": stress
    }

    df = pd.DataFrame([data])

    # Prediction
    predicted_score = model.predict(df)[0]

    # Extra outputs
    grade = get_grade(predicted_score)
    result = get_result(predicted_score)
    suggestions = give_suggestions(data, predicted_score)
    study_plan = generate_study_plan(predicted_score)

    # Risk level
    if predicted_score < 50:
        risk = "High Risk 🔴"
    elif predicted_score < 70:
        risk = "Moderate Risk 🟡"
    else:
        risk = "Low Risk 🟢"

    # ---------------- OUTPUT ---------------- #

    st.subheader("📊 Prediction Result")

    st.write(f"**Predicted Score:** {round(predicted_score, 2)}")
    st.write(f"**Grade:** {grade}")
    st.write(f"**Result:** {result}")
    st.write(f"**Risk Level:** {risk}")

    st.subheader("📌 Suggestions")
    for s in suggestions:
        st.write("•", s)

    st.subheader("📅 Study Plan")
    for p in study_plan:
        st.write("•", p)

# ---------------- DATA ANALYSIS ---------------- #

st.subheader("📊 Data Insights")

if st.checkbox("Show Data Analysis"):

    df_data = pd.read_excel("data.xlsx")

    # Clean columns (same as your training)
    df_data.columns = df_data.columns.str.strip()

    df_data = df_data.rename(columns={
        '1. Attendance (%)': 'attendance',
        '2. Study Hours per Day': 'study_hours',
        '3. Previous Exam Score': 'previous_score',
        '4.Assignment Completion (%)': 'assignments',
        '5. Sleep Hours per Day': 'sleep',
        '6. Screen Time (hours/day)': 'screen_time',
        '7. Study Consistency (days/week)': 'consistency',
        '8. Stress Level': 'stress',
        '9. Final Exam Score (out of 100)': 'final_score'
    })

    # Graph 1: Study Hours vs Score
    st.write("### Study Hours vs Score")
    fig1, ax1 = plt.subplots()
    ax1.scatter(df_data["study_hours"], df_data["final_score"])
    ax1.set_xlabel("Study Hours")
    ax1.set_ylabel("Final Score")
    st.pyplot(fig1)

    # Graph 2: Attendance vs Score
    st.write("### Attendance vs Score")
    fig2, ax2 = plt.subplots()
    ax2.scatter(df_data["attendance"], df_data["final_score"])
    ax2.set_xlabel("Attendance")
    ax2.set_ylabel("Final Score")
    st.pyplot(fig2)

    # Graph 3: Stress vs Score
    st.write("### Stress vs Score")
    fig3, ax3 = plt.subplots()
    ax3.scatter(df_data["stress"], df_data["final_score"])
    ax3.set_xlabel("Stress Level")
    ax3.set_ylabel("Final Score")
    st.pyplot(fig3)