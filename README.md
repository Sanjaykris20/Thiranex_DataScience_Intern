# Data Science & Analytics Internship Portfolio

Welcome to my **Data Science & Analytics Internship Project Portfolio**. This repository contains a structured, end-to-end suite of four data science projects demonstrating data cleaning, predictive modeling, exploratory data analysis (EDA), and financial forecasting. 

Every module contains full data generation scripts, automated data cleaning/modeling pipelines, Jupyter notebooks, static visual reports, and **premium interactive HTML dashboards** powered by Chart.js.

---

## 📂 Repository Structure

```text
├── 01_Data_Cleaning_and_Visualization/
│   ├── generate_raw_data.py          # Script generating raw, dirty sales data
│   ├── data_cleaning.py              # Cleaning pipeline & dashboard compiler
│   ├── raw_sales_data.csv            # Raw dataset (duplicates, missing, outliers)
│   ├── clean_sales_data.csv          # Cleaned dataset ready for ingestion
│   ├── dashboard_data.js             # Data payload for the HTML UI
│   ├── dashboard.html                # Interactive glassmorphic audit dashboard
│   ├── data_cleaning.ipynb           # Generated Jupyter Notebook
│   └── plots/                        # Static matplotlib/seaborn plots
│
├── 02_Predictive_Modeling/
│   ├── generate_churn_data.py        # Generates customer retention profile
│   ├── modeling.py                   # Model training and metric evaluations
│   ├── customer_churn_data.csv       # Customer churn data
│   ├── model_data.js                 # Exported model weights and ROC values
│   ├── churn_predictor.html          # Interactive live ML risk calculator
│   └── modeling.ipynb                # Generated Jupyter Notebook
│
├── 03_Exploratory_Data_Analysis/
│   ├── generate_eda_data.py          # Generates student behavior profiles
│   ├── eda.py                        # Computes descriptive statistics & correlations
│   ├── student_performance.csv       # Academic performance dataset
│   ├── eda_data.js                   # Statistical payload
│   ├── eda_report.html               # Interactive heatmap and metrics dashboard
│   └── eda_analysis.ipynb            # Generated Jupyter Notebook
│
├── 04_Real_World_Finance_Project/
│   ├── generate_stock_data.py        # Simulates daily stock prices
│   ├── stock_analytics.py            # Computes SMA trends, Sharpe, and regressions
│   ├── stock_prices.csv              # Asset performance historical data
│   ├── finance_data.js               # Historical and trend forecast payload
│   ├── finance_app.html              # Portfolio Simulator & Trend Forecaster
│   └── stock_analytics.ipynb         # Generated Jupyter Notebook
│
├── convert_all.py                    # Root script compiling .py scripts to .ipynb
└── .gitignore                        # Standard files/folders exclusions
```

---

## 🛠️ Project Walkthroughs

### 1. Data Cleaning & Visualization Project (Quest 1)
* **Goal**: Take a raw, dirty, and outlier-heavy transaction dataset and build a clean pipeline.
* **Pipeline Highlights**:
  * Imputed missing values using category-specific medians and placeholders.
  * Standardized values (corrected typos in product categories).
  * Removed duplicates and resolved positive/negative extreme outliers.
  * Imputed missing ages using rounded mean values.
* **Web UI ([dashboard.html](01_Data_Cleaning_and_Visualization/dashboard.html))**: Includes a detailed **Data Quality Audit Log** tracking issues resolved, along with interactive breakdown charts of category revenue, transaction counts, and payment modes.

### 2. Customer Churn Prediction Using Machine Learning (Quest 2)
* **Goal**: Build a predictive model to evaluate and flag high-risk telecom customers.
* **Pipeline Highlights**:
  * Trained and cross-evaluated **Logistic Regression** and **Random Forest Classifiers**.
  * Handled data splits using stratified splits (80/20 train/test).
  * Calculated model statistics: Accuracy, Precision, Recall, F1-Score, Confusion Matrix, and ROC/AUC.
* **Web UI ([churn_predictor.html](02_Predictive_Modeling/churn_predictor.html))**: Features a **Live ML Risk Calculator** widget. It runs the trained logistic regression coefficients locally in the browser to compute and display churn risk probabilities instantly as users slide attributes.

### 3. Student Engagement Exploratory Data Analysis (Quest 3)
* **Goal**: Analyze the correlation of behavioral patterns (study hours, sleep, attendance, extracurriculars) on student performance.
* **Pipeline Highlights**:
  * Calculated comprehensive descriptive statistics.
  * Extracted correlation matrices for key factors.
  * Binned continuous study hours to study impact intensity groups.
* **Web UI ([eda_report.html](03_Exploratory_Data_Analysis/eda_report.html))**: Renders an interactive, hover-responsive correlation strength heatmap grid, sleep/attendance statistics, and study-impact distributions.

### 4. Real-world Financial Portfolio Trend Forecaster (Quest 4)
* **Goal**: Analyze multi-stock pricing data to forecast future values and manage risk.
* **Pipeline Highlights**:
  * Calculated annualized volatility, Sharpe ratios, and returns for three assets (TechCorp, EcoEnergy, MedHealth).
  * Generated 20-day and 50-day Simple Moving Averages (SMAs).
  * Applied scikit-learn `LinearRegression` to output a 10-day price trend projection.
* **Web UI ([finance_app.html](04_Real_World_Finance_Project/finance_app.html))**: Includes an **Investment Simulator Game** where you can trade shares, track cash reserves, calculate net gains, and monitor asset health indicators dynamically.

---

## 💻 Tech Stack & Libraries

* **Backend / Analytics**: Python 3.13+, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn.
* **Frontend / Visualization**: HTML5, CSS3 (Custom Glassmorphic themes & gradients), JavaScript (ES6+), Chart.js.
* **Notebooks**: Jupyter Notebook.

---

## 🚀 How to Run Locally

### 1. Install Dependencies
Ensure you have Python installed, then install the required libraries:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

### 2. Generate and Process Data
Execute the following commands from the root directory to generate the datasets and process the analytics:
```bash
# Generate mock datasets
python 01_Data_Cleaning_and_Visualization/generate_raw_data.py
python 02_Predictive_Modeling/generate_churn_data.py
python 03_Exploratory_Data_Analysis/generate_eda_data.py
python 04_Real_World_Finance_Project/generate_stock_data.py

# Run pipelines and generate payloads
python 01_Data_Cleaning_and_Visualization/data_cleaning.py
python 02_Predictive_Modeling/modeling.py
python 03_Exploratory_Data_Analysis/eda.py
python 04_Real_World_Finance_Project/stock_analytics.py
```

### 3. Compile Notebooks
To compile the raw Python pipelines into ready-to-run Jupyter Notebooks:
```bash
python convert_all.py
```

### 4. Run Interactive Dashboards
Open the respective `.html` dashboard files in any web browser to view the interactive widgets and results:
* `01_Data_Cleaning_and_Visualization/dashboard.html`
* `02_Predictive_Modeling/churn_predictor.html`
* `03_Exploratory_Data_Analysis/eda_report.html`
* `04_Real_World_Finance_Project/finance_app.html`
