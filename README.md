# DataClean-Task1
For internship Task1 
# Internship Task 1: Data Cleaning – Summary

## Task Objective:
The goal of this task was to perform initial data cleaning and preprocessing on the Medical Appointment No-Show dataset to prepare it for analysis.

## Steps Followed:

1. **Load the Dataset:**
   - Loaded the dataset using `pandas` and verified its shape and structure.

2. **Check for Missing Values:**
   - Checked for missing values across all columns. 
   - Found no missing values, which was good.

3. **Remove Duplicates:**
   - Checked for and removed duplicate entries.
   - The dataset didn’t contain any duplicates.

4. **Standardize Column Values:**
   - Cleaned up the "no-show" column by stripping whitespace and converting text to uppercase for consistency.

5. **Convert Date Columns:**
   - Converted the `scheduledday` and `appointmentday` columns into proper `datetime` formats to enable time-based analysis.

6. **Check Data Types:**
   - Checked that each column had the correct data type for proper analysis.

## Final Output:
- Saved the cleaned dataset as `medical_appointments_cleaned.csv`, ready for further exploration or modeling.
