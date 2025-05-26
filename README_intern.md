# 🧼 Titanic Data Cleaning Task

## 📌 About the Task

As part of my internship assignment, I was asked to clean and preprocess the Titanic dataset. This task helped me understand how to prepare data before applying machine learning algorithms.

## ⏳ Time Window

The task was completed on the same day within the allowed time slot (10:00 AM – 10:00 PM).

## 🧠 What I Learned

- How to inspect and understand a dataset.
- Fixing missing values using median/mode.
- Encoding categorical values like 'Sex' and 'Embarked'.
- Scaling numerical data using StandardScaler.
- Detecting and removing outliers using boxplots and IQR.

## 🛠 Tools and Libraries Used

- Python
- Pandas
- NumPy
- Matplotlib and Seaborn (for visualization)
- Scikit-learn

## 📁 Dataset Info

I used the Titanic dataset from Kaggle (by Yasserh). I downloaded the `titanic.csv` file from:
https://www.kaggle.com/datasets/yasserh/titanic-dataset

## 🔧 What I Did

1. Loaded the dataset and checked for null values.
2. Filled missing values:
   - 'Age' with median
   - 'Embarked' with mode
3. Dropped columns like 'Cabin', 'Name', and 'Ticket' as they didn’t seem useful.
4. Converted categorical columns to numeric using one-hot encoding.
5. Standardized numerical columns like 'Age' and 'Fare'.
6. Visualized outliers using boxplots and removed them using IQR method.

## 📸 Screenshots

I’ve added screenshots (optional) for reference if needed.


