import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\miriam\Downloads\India_lpg_dataset.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(data.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(data.tail())

# Display the shape of the dataset
print("\nShape of Dataset:")
print(data.shape)

# Display column names
print("\nColumn Names:")
print(data.columns)

# Display dataset information
print("\nDataset Information:")
data.info()

# Display data types
print("\nData Types:")
print(data.dtypes)

# Display statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Display statistical summary including text columns
print("\nComplete Summary:")
print(data.describe(include='all'))

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(data.isnull().sum().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(data.duplicated().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Verify duplicates removed
print("\nDuplicate Rows After Removal:")
print(data.duplicated().sum())

# Number of unique values in each column
print("\nUnique Values:")
print(data.nunique())

# Display 5 random rows
print("\nRandom Sample:")
print(data.sample(5))