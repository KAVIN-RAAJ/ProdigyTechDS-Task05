import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'ID': ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],
    'Severity': [3, 2, 2, 2, 3],
    'Start_Time': ['2016-02-08 00:37:08', '2016-02-08 05:56:20', '2016-02-08 06:15:39', '2016-02-08 06:51:45', '2016-02-08 07:53:43'],
    'End_Time': ['2016-02-08 06:37:08', '2016-02-08 11:56:20', '2016-02-08 12:15:39', '2016-02-08 12:51:45', '2016-02-08 13:53:43'],
    'Start_Lat': [40.108910, 39.865420, 39.102660, 41.062130, 39.172393],
    'Start_Lng': [-83.092860, -84.062800, -84.524680, -81.537840, -84.492792],
    'End_Lat': [40.112060, 39.865010, 39.102090, 41.062170, 39.170476],
    'End_Lng': [-83.031870, -84.048730, -84.523960, -81.535470, -84.501798],
    'Distance(mi)': [3.230, 0.747, 0.055, 0.123, 0.500],
    'Description': ['Between Sawmill Rd/Exit 20 and OH-315/Olentang...', 'At OH-4/OH-235/Exit 41 - Accident.', 
                    'At I-71/US-50/Exit 1 - Accident.', 'At Dart Ave/Exit 21 - Accident.', 
                    'At Mitchell Ave/Exit 6 - Accident.'],
    # Add more columns as needed
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Sample Data:")
print(df)

# Analysis and visualization
plt.figure(figsize=(10, 6))
sns.countplot(x="Severity", data=df)
plt.title("Distribution of Accident Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Accidents")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x="Start_Lng", y="Start_Lat", hue="Severity", data=df)
plt.title("Accident Hotspots")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
