# Titanic Exploratory Data Analysis (EDA) Assignment

This repository contains the complete step-by-step Python implementation for the Titanic Dataset EDA and Data Cleaning assignment, structured from **Task 1 to Task 29**.

## Project Structure

The project is broken down into modular Python scripts corresponding to each task:

- **Data Loading & Inspection:**
  - `task_01_import_libraries.py` - Imports Pandas, NumPy, Matplotlib, Seaborn.
  - `task_02_load_dataset.py` - Loads the CSV dataset into a Pandas DataFrame.
  - `task_03_display_first_rows.py` - Displays head rows and identifies target/feature types.
  - `task_04_sample_rows.py` - Views random sample rows.
  - `task_05_data_info.py` - Checks dataset shape and column info.
  - `task_06_check_duplicates.py` - Checks for duplicate records.
  - `task_07_check_missing.py` - Identifies missing/null values.
  - `task_08_summary_statistics.py` - Generates statistical summaries.

- **Categorical & Distribution Analysis:**
  - `task_09_class_counts.py` - Passenger class value counts.
  - `task_10_unique_values.py` - Unique value counts for text columns.

- **Visualizations (Matplotlib & Seaborn):**
  - `task_11_visualize_survived.py` - Target variable countplot.
  - `task_12_survival_by_gender.py` - Survival rate by gender.
  - `task_13_survival_by_class.py` - Survival rate by passenger class.
  - `task_14_age_distribution.py` - Passenger age histogram.
  - `task_15_age_vs_survival.py` - Age vs Survival boxplot.
  - `task_16_fare_distribution.py` - Ticket fare distribution.
  - `task_17_fare_vs_survival.py` - Fare vs Survival boxplot.
  - `task_18_embarked_distribution.py` - Embarkation port counts.
  - `task_19_survival_by_embarked.py` - Survival by embarkation port.
  - `task_20_age_by_class.py` - Age distribution across classes.

- **Correlation & Aggregation:**
  - `task_21_correlation_matrix.py` - Computes numerical correlation.
  - `task_22_correlation_heatmap.py` - Generates correlation heatmap.
  - `task_23_groupby_gender.py` - Grouping by gender.
  - `task_24_groupby_class.py` - Grouping by passenger class.

- **Data Cleaning & Feature Engineering:**
  - `task_25_fill_missing_age.py` - Imputing missing ages with mean.
  - `task_26_drop_columns.py` - Dropping irrelevant columns (Cabin, Ticket).
  - `task_27_family_size.py` - Creating `FamilySize` feature.
  - `task_28_encode_gender.py` - Encoding categorical gender data.
  - `task_29_save_cleaned_data.py` - Exporting cleaned dataset to CSV.

## Requirements
- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Author
Ammar Hassan
BCS-F23-M45