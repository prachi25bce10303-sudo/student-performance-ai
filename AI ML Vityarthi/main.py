from train_model import train_model
from suggestion_engine import give_suggestions, generate_study_plan, get_grade, get_result
import pandas as pd

# Step 1: Train model
model = train_model("data.xlsx")

print("\n--- Enter Student Details ---")

# 👤 Name
name = input("Student Name: ")

# Input
attendance = float(input("Attendance (%): "))
study_hours = float(input("Study hours per day: "))
previous_score = float(input("Previous exam score: "))
assignments = float(input("Assignment completion (%): "))
sleep = float(input("Sleep hours per day: "))
screen_time = float(input("Screen time (hours/day): "))
consistency = float(input("Study consistency (days/week): "))
stress = float(input("Stress level (1-10): "))

# Store data
student = {
    "attendance": attendance,
    "study_hours": study_hours,
    "previous_score": previous_score,
    "assignments": assignments,
    "sleep": sleep,
    "screen_time": screen_time,
    "consistency": consistency,
    "stress": stress
}

# Convert to DataFrame
input_df = pd.DataFrame([student])

# Predict
predicted_score = model.predict(input_df)[0]

# Get extras
grade = get_grade(predicted_score)
result = get_result(predicted_score)
suggestions = give_suggestions(student, predicted_score)
plan = generate_study_plan(predicted_score)

# 🔥 FINAL OUTPUT
print("\n==============================")
print(f"🎓 Student: {name}")
print("==============================")

print(f"📊 Predicted Score: {round(predicted_score, 2)}")
print(f"🏆 Grade: {grade}")
print(f"✅ Result: {result}")

print("\n📌 Suggestions:")
for s in suggestions:
    print("•", s)

print("\n📅 Study Plan:")
for p in plan:
    print("•", p)

print("\n==============================")