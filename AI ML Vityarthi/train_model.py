import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score


def train_model(file_path):
    # Load data
    df = pd.read_excel(file_path)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Rename columns
    df = df.rename(columns={
        'Name': 'name',
        'Name ': 'name',
        '1. Attendance (%)': 'attendance',
        '2. Study Hours per Day': 'study_hours',
        '3. Previous Exam Score': 'previous_score',
        '4.Assignment Completion (%)': 'assignments',
        '5. Sleep Hours per Day': 'sleep',
        '5. Sleep Hours per Day\n': 'sleep',
        '6. Screen Time (hours/day)': 'screen_time',
        '6. Screen Time (hours/day) ': 'screen_time',
        '7. Study Consistency (days/week)': 'consistency',
        '8. Stress Level': 'stress',
        '9. Final Exam Score (out of 100)': 'final_score'
    })

    # Drop unnecessary columns
    if 'Timestamp' in df.columns:
        df = df.drop('Timestamp', axis=1)

    if 'name' in df.columns:
        df = df.drop('name', axis=1)

    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))

    # Features & target
    X = df.drop('final_score', axis=1)
    y = df['final_score']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # ---------------- MODELS ---------------- #

    # Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_score = r2_score(y_test, lr_model.predict(X_test))

    # Random Forest
    rf_model = RandomForestRegressor(random_state=42)
    rf_model.fit(X_train, y_train)
    rf_score = r2_score(y_test, rf_model.predict(X_test))

    # ---------------- RESULTS ---------------- #

    print("\n📊 Model Performance:")
    print("Linear Regression R2:", round(lr_score, 3))
    print("Random Forest R2:", round(rf_score, 3))

    # ---------------- MODEL SELECTION ---------------- #

    if rf_score > lr_score:
        print("\n✅ Best Model: Random Forest 🌳")

        # Feature Importance
        importances = rf_model.feature_importances_
        features = X.columns

        print("\n📌 Feature Importance:")
        for f, imp in zip(features, importances):
            print(f"{f}: {round(imp, 3)}")

        # Save model
        joblib.dump(rf_model, "model.pkl")

        return rf_model

    else:
        print("\n✅ Best Model: Linear Regression 📈")

        # Save model
        joblib.dump(lr_model, "model.pkl")

        return lr_model


# ---------------- RUN FILE ---------------- #

if __name__ == "__main__":
    train_model("data.xlsx")