import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs('output_images', exist_ok=True)

df = pd.read_csv('healthcare_analytics_patient_flow_data.csv')
age_data = df['Patient Age'].dropna()

bins = [0, 18, 35, 50, 70, 100]
labels = ['0-18', '19-35', '36-50', '51-70', '71+']
age_groups = pd.cut(age_data, bins=bins, labels=labels).value_counts().sort_index()

plt.figure(figsize=(8, 6))
age_groups.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Patient Age Groups - Bar Chart')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.savefig('output_images/bar_chart.png')
plt.close()

plt.figure(figsize=(8, 6))
plt.plot(age_data.values, color='green')
plt.title('Patient Ages (Unsorted) - Line Chart')
plt.xlabel('Patient Index')
plt.ylabel('Age')
plt.savefig('output_images/line_chart.png')
plt.close()

plt.figure(figsize=(8, 6))
age_groups.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Patient Age Distribution - Pie Chart')
plt.ylabel('')
plt.savefig('output_images/pie_chart.png')
plt.close()

plt.figure(figsize=(8, 6))
plt.step(range(len(age_data)), age_data.values, where='mid', color='purple')
plt.title('Patient Ages (Unsorted) - Stair Chart')
plt.xlabel('Patient Index')
plt.ylabel('Age')
plt.savefig('output_images/stair_chart.png')
plt.close()

plt.figure(figsize=(8, 6))
plt.hist(age_data, bins=20, color='orange', edgecolor='black')
plt.title('Patient Age - Histogram')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('output_images/histogram.png')
plt.close()

print("Charts created successfully in output_images folder.")