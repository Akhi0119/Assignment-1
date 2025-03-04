#Finding the null values
null_counts = data.isnull().sum()
print(null_counts)
#Calculating the Average Score
data['average score'] = (data['math score'] + data['writing score'] + data['reading score'])/3
data.head()
data.columns
#Average Score
data['average score'] = np.round(data['average score'], 2)
data
#Saving the data into Cleaned data folder
data.to_csv('cleanedstudentperformance_data.csv',index=False)
