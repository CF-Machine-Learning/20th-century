import pandas as pd

# Example dataframe
data = {
    'Country': ['USA', 'Canada', 'Germany', 'France', 'Italy'],
}

df = pd.DataFrame(data)

# Create a flag column using a lambda function
df['Flag'] = df['Country'].apply(lambda x: True if x in ['USA', 'Canada'] else False)

# Print the updated dataframe
print(df)
