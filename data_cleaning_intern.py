import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load the dataset
df = pd.read_csv('titanic.csv')

# Check the first few rows
print(df.head())

# Check for missing values and data types
print(df.info())
print("Missing values:\n", df.isnull().sum())

# Fill missing values
df['Age'].fillna(df['Age'].median(), inplace=True)  # Using median for Age
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)  # Using mode for Embarked

# Drop the 'Cabin' column as it has too many missing values
df.drop('Cabin', axis=1, inplace=True)

# Drop columns that are not useful
df.drop(['Name', 'Ticket'], axis=1, inplace=True)

# Convert categorical columns to numerical using one-hot encoding
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# Standardize the numerical columns
scaler = StandardScaler()
num_cols = ['Age', 'Fare']
df[num_cols] = scaler.fit_transform(df[num_cols])

# Visualize outliers using boxplots
sns.boxplot(x=df['Age'])
plt.title("Boxplot of Age")
plt.show()

sns.boxplot(x=df['Fare'])
plt.title("Boxplot of Fare")
plt.show()

# Remove outliers using IQR method
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]

# Final check of cleaned data
print(df.info())
print(df.head())
