# AI-Based Student Performance Predictor  

## Project Description  
This project presents an AI-based system that predicts student academic performance using machine learning techniques and provides personalized intervention suggestions to improve outcomes.  

The system uses real-world data collected through Google Forms and considers factors such as attendance, study hours, previous scores, assignment completion, sleep, screen time, study consistency, and stress level.  

Multiple machine learning models (Linear Regression and Random Forest) are trained and compared, and the best-performing model is selected based on the R² score.  

The project is deployed as an interactive web application using Streamlit, allowing users to input their details and receive real-time predictions, performance insights, and suggestions.

## Features  
- Predicts student performance (score)  
- Assigns grade and pass/fail result  
- Provides personalized suggestions  
- Generates study plan  
- Interactive web application  
- Data visualization (graphs)  

## Machine Learning Models  
- Linear Regression  
- Random Forest Regression  

The best model is selected based on performance (R² score).

## Dataset  
- Collected using Google Forms  
- Contains real student data  

### Features:
- Attendance (%)  
- Study hours per day  
- Previous exam score  
- Assignment completion (%)  
- Sleep hours  
- Screen time  
- Study consistency (days/week)  
- Stress level  

### Target:
- Final exam score (out of 100)

## Installation  
### Install required libraries:
pip install -r requirements.txt
python3 train_model.py
python3 -m streamlit run app.py

## student-performance-ai/
│
├── app.py
├── train_model.py
├── suggestion_engine.py
├── model.pkl
├── data.xlsx
├── requirements.txt
├── README.md
└── report.pdf

<img width="1461" height="784" alt="interface" src="https://github.com/user-attachments/assets/09d8b6e1-81f8-4edc-8101-6220b8c82980" />

<img width="1307" height="706" alt="Screenshot 2026-03-27 at 8 09 04 PM" src="https://github.com/user-attachments/assets/8452fdb8-1f02-45b1-989b-3160c4259f36" />

<img width="891" height="647" alt="Screenshot 2026-03-27 at 8 09 24 PM" src="https://github.com/user-attachments/assets/357992fd-d34b-4cf4-b22b-4fb02ee2c7fb" />

<img width="811" height="649" alt="Screenshot 2026-03-27 at 8 09 31 PM" src="https://github.com/user-attachments/assets/f52bb980-09bb-4b2e-98db-9a813e26c0c1" />

<img width="1033" height="668" alt="Screenshot 2026-03-27 at 8 09 38 PM" src="https://github.com/user-attachments/assets/5157c645-afc6-48c4-a2c4-e0e656374b7c" />

