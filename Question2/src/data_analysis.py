#1. Pie Plot of Race or Ethnicity
# Define a custom color palette
own_palette = ["#ae0581", "#2067bf", "#602e36", "#794680", "#658b63"]

# Count occurrences of each race/ethnicity category
race_counts = data['race/ethnicity'].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(race_counts, labels=race_counts.index, autopct='%1.1f%%', colors=own_palette, startangle=140, wedgeprops={'edgecolor': 'black'})

# Title
plt.title('Distribution of Race/Ethnicity')
# Save the image in Google Colab
plt.savefig('/content/race_ethnicity_distribution.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()

#2.Hist Plot of Gender Distribution
# Get unique gender values to ensure correct mapping
unique_genders = data['gender'].unique()

# Define a color palette dynamically based on dataset values
own_palette1 = {unique_genders[0]: "#ff7f50", unique_genders[1]: "#1177ad"}  # Coral for one, Dark Blue for the other

# Create a bar plot with hue assigned correctly
plt.figure(figsize=(6, 5))
ax = sns.countplot(x='gender', data=data, hue='gender', palette=own_palette1)

# Add count labels on top of the bars
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}',
                 (p.get_x() + p.get_width() / 2., p.get_height()),
                 ha='center', va='bottom', fontsize=12, fontweight='bold', xytext=(0, 5),
                 textcoords='offset points')

# Titles and labels
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')

# Save the image
plt.savefig('/content/gender_distribution.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()

plt.figure(figsize=(15, 5))

# 3.Swarm plot: Average score vs Reading score
plt.subplot(1, 3, 1)
sns.swarmplot(data=data, x="gender", y="reading score", hue="gender", palette=["#008080", "#800080"], size=3, dodge=True)
plt.xlabel("Gender")
plt.ylabel("Reading Score")
plt.title("Reading Score Distribution by Gender")

# Swarm plot: Average score vs Math score
plt.subplot(1, 3, 2)
sns.swarmplot(data=data, x="gender", y="math score", hue="gender", palette=["#008080", "#800080"], size=3, dodge=True)
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.title("Math Score Distribution by Gender")

# Swarm plot: Average score vs Writing score
plt.subplot(1, 3, 3)
sns.swarmplot(data=data, x="gender", y="writing score", hue="gender", palette=["#008080", "#800080"], size=3, dodge=True)
plt.xlabel("Gender")
plt.ylabel("Writing Score")
plt.title("Writing Score Distribution by Gender")

# Save the image
plt.savefig('/content/swarm_plot_scores_by_gender.png', dpi=300, bbox_inches='tight')

# Adjust layout for better spacing
plt.tight_layout()
plt.show()

#4.Box plot of Gender vs Average Score
plt.figure(figsize=(8, 6))

# Box plot: Distribution of Average Scores by Gender
sns.boxplot(x='gender', y='average score', data=data, hue='gender', palette=['#006400', '#FF1493'])

# Titles and labels
plt.title('Distribution of Average Scores by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Score')

# Save the image
plt.savefig('/content/gender_vs_avg_score.png', dpi=300, bbox_inches='tight')

# Show plot
plt.show()

#5.Bar Plot of Parental level of education VS Average Score

# Define a mix of light and dark colors
color_palette = ["#87CEFA", "#483D8B", "#A2D9CE", "#76448A", "#F7C6C7", "#154360"]

plt.figure(figsize=(10, 6))

# Bar plot: Parental Level of Education vs. Average Score
sns.barplot(data=data, x='parental level of education', y='average score', hue='parental level of education', palette=color_palette, legend=False)

# Titles and labels
plt.title('Parental Level of Education vs. Average Score')
plt.xlabel('Parental Level of Education')
plt.ylabel('Average Score')

# Rotate x-axis labels for readability
plt.xticks(rotation=45, ha='right')

plt.savefig('/content/parental_education_vs_avg_score.png', dpi=300, bbox_inches='tight')
# Show plot
plt.show()
