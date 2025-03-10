import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


npy_file = r'.\OneDrive_2025-03-03\LED_data_for prediction\Dataset\Data_preprocessing_2D_CNN\Data_All\Data\SAC105\FCGB1_sac105.npy'

arr = np.load(npy_file)
df = pd.DataFrame(arr, columns=['X Location (µm)', 'Y Location (µm)', 'Z Location (µm)', 'NLCREQ (µm/µm)'])

# Calculate the length in each direction
print()
print("X Length(µm):", df['X Location (µm)'].max() - df['X Location (µm)'].min())
print("Y Length(µm):", df['Y Location (µm)'].max() - df['Y Location (µm)'].min())
print("Z Length(µm):", df['Z Location (µm)'].max() - df['Z Location (µm)'].min())
print("NLCREQ Length(µm/µm):", df['NLCREQ (µm/µm)'].max() - df['NLCREQ (µm/µm)'].min())

# Plot X and Y
# plt.figure(figsize=(8, 6))
# plt.plot(df['X Location (µm)'], df['Y Location (µm)'], 'bo', markersize=3)
# plt.xlabel('X Location (µm)')
# plt.ylabel('Y Location (µm)')
# plt.title(npy_file.split('\\')[-1])
# plt.grid(True)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.show()


# Create 3D scatter plot
fig = px.scatter_3d(df, x='X Location (µm)', y='Y Location (µm)', z='Z Location (µm)', 
                    title='3D Scatter Plot of Data Points', 
                    labels={'X Location (µm)': 'X (µm)', 'Y Location (µm)': 'Y (µm)', 'Z Location (µm)': 'Z (µm)'})

# Show the plot
fig.show()
