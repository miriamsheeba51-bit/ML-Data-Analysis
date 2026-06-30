import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ===============================
# Load Dataset
# ===============================

data = pd.read_csv(r"C:\Users\miriam\Downloads\india_cancer_patients_2022_2025.csv")

# ===============================
# Basic Information
# ===============================

print("========== CANCER DATA ANALYSIS ==========\n")

print("First 5 Records")
print(data.head())

print("\nLast 5 Records")
print(data.tail())

print("\nDataset Shape")
print(data.shape)

print("\nColumn Names")
print(data.columns)

print("\nDataset Information")
data.info()

print("\nStatistical Summary")
print(data.describe(include='all'))

print("\nMissing Values")
print(data.isnull().sum())

print("\nDuplicate Rows")
print(data.duplicated().sum())

# Remove duplicates
data = data.drop_duplicates()

# ===============================
# Patient Analysis
# ===============================

print("\nTotal Patients:", len(data))

print("\nPatient Status")
print(data['Status'].value_counts())

alive = data[data['Status']=="Alive"]
dead = data[data['Status']=="Deceased"]

print("\nPatients Alive:", len(alive))
print("Patients Deceased:", len(dead))

print("\nSurvival Rate:",
      round((len(alive)/len(data))*100,2), "%")

print("Mortality Rate:",
      round((len(dead)/len(data))*100,2), "%")

# ===============================
# Age Analysis
# ===============================

print("\nAverage Age:", round(data['Age'].mean(),2))
print("Youngest Patient:", data['Age'].min())
print("Oldest Patient:", data['Age'].max())

# ===============================
# Cancer Analysis
# ===============================

print("\nCancer Types")
print(data['Cancer_Type'].value_counts())

print("\nCancer Stage Distribution")
print(data['Stage'].value_counts())

print("\nTreatment Types")
print(data['Treatment_Type'].value_counts())

# ===============================
# Survival Analysis
# ===============================

print("\nAverage Survival Months:",
      round(data['Survival_Months'].mean(),2))

print("Maximum Survival:",
      data['Survival_Months'].max())

print("Minimum Survival:",
      data['Survival_Months'].min())

print("\nAverage Survival by Cancer Type")
print(data.groupby('Cancer_Type')['Survival_Months'].mean())

print("\nAverage Survival by Stage")
print(data.groupby('Stage')['Survival_Months'].mean())

print("\nAverage Survival by Treatment")
print(data.groupby('Treatment_Type')['Survival_Months'].mean())

# ===============================
# Gender Analysis
# ===============================

print("\nGender Distribution")
print(data['Gender'].value_counts())

# ===============================
# State Analysis
# ===============================

print("\nState-wise Patients")
print(data['State'].value_counts())

print("\nTop 10 Cities")
print(data['City'].value_counts().head(10))

print("\nTop 10 Hospitals")
print(data['Hospital_Name'].value_counts().head(10))

# ===============================
# Cross Analysis
# ===============================

print("\nCancer Type vs Status")
print(data.groupby('Cancer_Type')['Status'].value_counts())

print("\nTreatment Type vs Status")
print(data.groupby('Treatment_Type')['Status'].value_counts())

print("\nStage vs Status")
print(data.groupby('Stage')['Status'].value_counts())

# ===============================
# Visualizations
# ===============================

# Cancer Type
plt.figure(figsize=(10,5))
sns.countplot(x='Cancer_Type', data=data)
plt.xticks(rotation=45)
plt.title("Cancer Type Distribution")
plt.show()

# Stage
plt.figure(figsize=(8,5))
sns.countplot(x='Stage', data=data)
plt.title("Cancer Stage Distribution")
plt.show()

# Treatment Type
plt.figure(figsize=(8,5))
sns.countplot(x='Treatment_Type', data=data)
plt.title("Treatment Type")
plt.show()

# Gender
plt.figure(figsize=(6,5))
sns.countplot(x='Gender', data=data)
plt.title("Gender Distribution")
plt.show()

# Patient Status
plt.figure(figsize=(6,6))
data['Status'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.ylabel("")
plt.title("Patient Status")
plt.show()

# Age Distribution
plt.figure(figsize=(8,5))
plt.hist(data['Age'], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Patients")
plt.show()

# Survival Months
plt.figure(figsize=(8,5))
plt.hist(data['Survival_Months'], bins=20)
plt.title("Survival Months")
plt.xlabel("Months")
plt.ylabel("Patients")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,5))
numeric = data.select_dtypes(include=['int64','float64'])
sns.heatmap(numeric.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Save Cleaned Dataset
data.to_csv("Cancer_Cleaned.csv", index=False)

print("\n========== ANALYSIS COMPLETED SUCCESSFULLY ==========")
