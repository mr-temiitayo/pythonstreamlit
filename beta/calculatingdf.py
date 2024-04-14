import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Maths': [75, 80, 85, 90],
    'Science': [70, 75, 80, 85],
    'English': [80, 85, 90, 95]
}

df = pd.DataFrame(data)

# Calculate total score for each student along axis 0
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)

print(df)
