#Calculate BMI from Weight and Height
data['bmi'] = (703 * (data['weight']))/(data['height'] ** 2)
data['bmi'] = data['bmi'].round(2)

# Calculating grip strength in Lbs
data['grip_strength_lbs'] = data['grip strength'] * 2.20462  # Conversion factor from Kgs to Lbs
data['grip_strength_lbs'] = data['grip_strength_lbs'].round(2)

# Calculating frailty index with grip_strength_lbs
data['frailty_index'] = (data['height'] / data['weight']) * data['age'] + (data['grip_strength_lbs'] / data['weight']) * data['age']
data['frailty_index'] = data['frailty_index'].round(2)
print(data)

#1. Age Vs Frailty Index
import seaborn as sns
import matplotlib.pyplot as plt
print(data.columns)

# Create age groups for better visualization
data['age_group'] = pd.cut(data['age'], bins=[30, 40, 50, 60, 70, 80, 90], labels=['30-40', '40-50', '50-60', '60-70', '70-80', '80-90'])

# Compute mean frailty index per age group and frailty status with observed=False to suppress warning
avg_frailty_index = data.groupby(['age_group', 'frality'], observed=False)['frailty_index'].mean().reset_index()

# Define a color palette with requested colors
color_mapping = {"Y": "#00008B", "N": "#87CEEB"}  # Dark Blue for 'Y', Sky Blue for 'N'

# Bar plot
plt.figure(figsize=(8, 6))
sns.barplot(x='age_group', y='frailty_index', hue='frality', data=avg_frailty_index, palette=color_mapping)

# Titles and labels
plt.title('Average Frailty Index by Age Group and Frailty Status')
plt.xlabel('Age Group')
plt.ylabel('Average Frailty Index')

# Show grid for better readability
plt.grid(axis='y')

# Custom legend to explicitly mention colors
handles = [
    plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color_mapping['Y'], label="Frail (Y) - Dark Blue"),
    plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color_mapping['N'], label="Non-Frail (N) - Sky Blue")
]
plt.legend(handles=handles, title="Frailty Status")
# Save the image
plt.savefig('/content/frailty_index_by_age_group.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()


#2. Body Mass Index (BMI) Vs Frailty Status
# Define a dictionary mapping 'frality' values to colors
color_mapping = {'Y': '#ff9999', 'N': '#66b3ff'}  # Example colors for 'Y' and 'N'

# Swarm plot of BMI by Frailty Status with color differentiation by 'frality'
plt.figure(figsize=(8, 6))
sns.swarmplot(x='frality', y='bmi', data=data, hue='frality', palette=color_mapping)

# Set titles and labels
plt.title('BMI by Frailty Status')
plt.xlabel('Frailty Status')
plt.ylabel('BMI')

# Display grid
plt.grid(True)

# Add a custom legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color_mapping['Y'], label='Frailty: Y'),
           plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color_mapping['N'], label='Frailty: N')]

plt.legend(handles=handles, title="Frailty Status")
# Save the image
plt.savefig('/content/bmi_by_frailty_status.png', dpi=300, bbox_inches='tight')
# Show plot
plt.show()

#3. Average grip strength by Frailty Status

# Define new custom color palette
color_mapping = {"Y": "#8B0000", "N": "#1E90FF"}  # Dark Red for 'Y', Dodger Blue for 'N'

# Violin plot of grip strength by Frailty Status
plt.figure(figsize=(6, 4))
sns.violinplot(x='frality', y='grip strength', data=data, hue='frality', palette=color_mapping, dodge=False)

# Adding title and labels
plt.title('Grip Strength Distribution by Frailty Status')
plt.xlabel('Frailty Status')
plt.ylabel('Grip Strength')

# Add a custom legend to indicate colors
handles = [
    plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color_mapping['Y'], label="Frailty: Y (Dark Red)"),
    plt.Line2D([0], [0], marker='o', color='w', markersize=10, markerfacecolor=color_mapping['N'], label="Frailty: N (Dodger Blue)")
]
plt.legend(handles=handles, title="Frailty Status")
# Save the image
plt.savefig('/content/grip_strength_by_frailty_status.png', dpi=300, bbox_inches='tight')
# Show the plot
plt.show()


