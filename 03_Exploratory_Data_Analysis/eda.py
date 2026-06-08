import pandas as pd
import numpy as np
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# Load data
df = pd.read_csv("C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis/student_performance.csv")

# 1. Descriptive stats
desc_stats = df.describe().to_dict()

# 2. Correlation Matrix
corr_matrix = df.drop(columns=['StudentID']).corr().to_dict()

# 3. Aggregations / Insights
# Average grade by extracurricular activities
extracurricular_avg = df.groupby('Extracurricular_Activities')['Final_Grade'].mean().to_dict()

# Average grade by study hours bins
df['Study_Hours_Bin'] = pd.cut(df['Study_Hours_Per_Week'], bins=[0, 8, 16, float('inf')], labels=['Low (<8h)', 'Medium (8-16h)', 'High (>16h)'])
study_bin_avg = df.groupby('Study_Hours_Bin', observed=False)['Final_Grade'].mean().to_dict()

# Convert key types to string for JSON compatibility
study_bin_avg = {str(k): float(v) for k, v in study_bin_avg.items()}
extracurricular_avg = {str(k): float(v) for k, v in extracurricular_avg.items()}

# Prepare individual scatter plot data for UI (sampling 150 points for visualization speed)
scatter_points = df[['Study_Hours_Per_Week', 'Attendance_Rate', 'Final_Grade']].sample(n=150, random_state=42).to_dict(orient='records')

# Plots directory
plots_dir = "C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis/plots"
os.makedirs(plots_dir, exist_ok=True)

# Save Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df.drop(columns=['StudentID', 'Study_Hours_Bin']).corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap - Student Performance factors')
plt.tight_layout()
plt.savefig(f"{plots_dir}/correlation_heatmap.png")
plt.close()

# Save scatter plot
plt.figure()
sns.scatterplot(x='Study_Hours_Per_Week', y='Final_Grade', hue='Extracurricular_Activities', data=df, palette='Set1')
plt.title('Study Hours vs Final Grade')
plt.xlabel('Study Hours / Week')
plt.ylabel('Final Grade (0-100)')
plt.tight_layout()
plt.savefig(f"{plots_dir}/study_vs_grade.png")
plt.close()

# Export data to JS for web reporting
eda_export = {
    "descriptive_statistics": desc_stats,
    "correlations": corr_matrix,
    "study_hours_impact": study_bin_avg,
    "extracurricular_impact": extracurricular_avg,
    "scatter_data": scatter_points,
    "overall_averages": {
        "avg_grade": float(df['Final_Grade'].mean()),
        "avg_attendance": float(df['Attendance_Rate'].mean()),
        "avg_study_hours": float(df['Study_Hours_Per_Week'].mean()),
        "avg_sleep": float(df['Sleep_Hours_Per_Night'].mean())
    }
}

with open("C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis/eda_data.js", "w") as f:
    f.write(f"const edaResults = {json.dumps(eda_export)};\n")

print("EDA analysis completed. eda_data.js and plots exported successfully!")
