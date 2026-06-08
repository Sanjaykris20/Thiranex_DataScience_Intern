import json
import os

def create_notebook(py_file_path, ipynb_file_path):
    with open(py_file_path, 'r') as f:
        code = f.read()
    
    # Split code into lines for Jupyter source list
    lines = [line + '\n' for line in code.split('\n')]
    # Remove trailing newline from the last element
    if lines and lines[-1] == '\n':
        lines[-1] = ''

    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# Internship Project Code: {os.path.basename(ipynb_file_path)}\n",
                    "This notebook was generated dynamically to present clean, readable, and reproducible data science pipelines."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": lines
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 2
    }

    with open(ipynb_file_path, 'w') as f:
        json.dump(notebook, f, indent=1)
    print(f"Created notebook: {ipynb_file_path}")

# Paths
create_notebook(
    "C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/data_cleaning.py",
    "C:/Users/HP/Downloads/intern 4th sem/01_Data_Cleaning_and_Visualization/data_cleaning.ipynb"
)

create_notebook(
    "C:/Users/HP/Downloads/intern 4th sem/02_Predictive_Modeling/modeling.py",
    "C:/Users/HP/Downloads/intern 4th sem/02_Predictive_Modeling/modeling.ipynb"
)

create_notebook(
    "C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis/eda.py",
    "C:/Users/HP/Downloads/intern 4th sem/03_Exploratory_Data_Analysis/eda_analysis.ipynb"
)

create_notebook(
    "C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project/stock_analytics.py",
    "C:/Users/HP/Downloads/intern 4th sem/04_Real_World_Finance_Project/stock_analytics.ipynb"
)
