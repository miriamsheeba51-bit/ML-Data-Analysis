import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\miriam\Downloads\Indian_Traffic_Violations.csv")
print("\nMost Common Violation")
print(data['Violation_Type'].value_counts().head(10))

print("\nTop 10 Locations with Highest Violations")
print(data['Location'].value_counts().head(10))

print("\nTop Vehicle Types")
print(data['Vehicle_Type'].value_counts())

print("\nDriver Gender Distribution")
print(data['Driver_Gender'].value_counts())

print("\nRegistration State Distribution")
print(data['Registration_State'].value_counts())

print("\nWeather Conditions")
print(data['Weather_Condition'].value_counts())

print("\nRoad Conditions")
print(data['Road_Condition'].value_counts())

print("\nPayment Methods")
print(data['Payment_Method'].value_counts())

print("\nBreathalyzer Results")
print(data['Breathalyzer_Result'].value_counts())

print("\nTop 10 Officers Issuing Fines")
print(data['Officer_ID'].value_counts().head(10))