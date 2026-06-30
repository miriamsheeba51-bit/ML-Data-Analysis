import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\miriam\Downloads\StatewiseTestingDetails.csv")

# Display first 5 rows
print("\nFirst 5 Rows")
print(data.head())

# Dataset information
print("\nDataset Info")
print(data.info())

# Dataset shape
print("\nShape:", data.shape)

# Missing values
print("\nMissing Values")
print(data.isnull().sum())

# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing values with 0
data = data.fillna(0)

# ---------- Death Rate ----------
# If your dataset has a 'Deaths' column
if 'Deaths' in data.columns:
    data['Death_Rate'] = (data['Deaths'] / data['Positive']) * 100
    data['Death_Rate'] = data['Death_Rate'].fillna(0)

    print("\nTop 10 States by Death Rate")
    print(data[['State', 'Death_Rate']].sort_values(by='Death_Rate', ascending=False).head(10))

# ---------- Recovery Rate ----------
# If your dataset has a 'Recovered' column
if 'Recovered' in data.columns:
    data['Recovery_Rate'] = (data['Recovered'] / data['Positive']) * 100
    data['Recovery_Rate'] = data['Recovery_Rate'].fillna(0)

    print("\nTop 10 States by Recovery Rate")
    print(data[['State', 'Recovery_Rate']].sort_values(by='Recovery_Rate', ascending=False).head(10))

# Top 10 states with highest positive cases
print("\nTop 10 States by Positive Cases")
print(data[['State', 'Positive']].sort_values(by='Positive', ascending=False).head(10))

# Average Positive Cases
print("\nAverage Positive Cases:", data['Positive'].mean())

# Maximum Positive Cases
print("Maximum Positive Cases:", data['Positive'].max())

# Minimum Positive Cases
print("Minimum Positive Cases:", data['Positive'].min())

# ---------------- VISUALIZATIONS ----------------

# Positive Cases by State
plt.figure(figsize=(12,6))
sns.barplot(x='State', y='Positive', data=data.head(15))
plt.xticks(rotation=90)
plt.title("Positive Cases by State")
plt.show()

# Total Samples by State
plt.figure(figsize=(12,6))
sns.barplot(x='State', y='TotalSamples', data=data.head(15))
plt.xticks(rotation=90)
plt.title("Total Samples Tested")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(data['Positive'], bins=20)
plt.title("Distribution of Positive Cases")
plt.xlabel("Positive Cases")
plt.ylabel("Frequency")
plt.show()

# Correlation Heatmap
numeric = data.select_dtypes(include=['number'])

plt.figure(figsize=(8,6))
sns.heatmap(numeric.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Save cleaned dataset
data.to_csv("Covid_Cleaned.csv", index=False)

print("\nProject Completed Successfully!")