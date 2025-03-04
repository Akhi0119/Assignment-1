null_counts = data.isnull().sum()
print(null_counts)
data.to_csv('cleaned_data.csv',index=False)
