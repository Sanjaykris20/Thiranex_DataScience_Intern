import pandas as pd
import numpy as np
import os

os.makedirs("C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis", exist_ok=True)

np.random.seed(10)
n_students = 500

# Continuous variables
study_hours = np.random.uniform(2.0, 25.0, n_students) # hours per week
attendance_rate = np.random.uniform(60.0, 100.0, n_students) # percentage
sleep_hours = np.random.uniform(4.0, 9.5, n_students) # hours per night

# Extra-curricular participation (0 or 1)
extracurricular = np.random.choice([0, 1], n_students, p=[0.4, 0.6])

# Final grade logic with some random noise
# Grade is influenced positively by study hours, attendance, sleep, and extracurriculars
grade_raw = (
    1.2 * study_hours 
    + 0.5 * attendance_rate 
    + 1.8 * sleep_hours 
    + 2.5 * extracurricular 
    + np.random.normal(15, 6, n_students)
)
# Scale grade to standard 0-100 range
final_grades = np.clip(grade_raw, 0, 100)

df = pd.DataFrame({
    'StudentID': [f"STU_{3000 + i}" for i in range(n_students)],
    'Study_Hours_Per_Week': np.round(study_hours, 1),
    'Attendance_Rate': np.round(attendance_rate, 1),
    'Sleep_Hours_Per_Night': np.round(sleep_hours, 1),
    'Extracurricular_Activities': extracurricular,
    'Final_Grade': np.round(final_grades, 1)
})

df.to_csv("C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis/student_performance.csv", index=False)
print("Student Performance dataset generated successfully for EDA!")
