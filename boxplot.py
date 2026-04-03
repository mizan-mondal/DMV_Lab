import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('healthcare_analytics_patient_flow_data.csv')
patient_waittime = df['Patient Waittime'].dropna()
plt.boxplot(patient_waittime)
plt.xlabel('time(mins)')
plt.title('Box Plot of Waited time')
plt.show()