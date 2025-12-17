import pandas as pd

# Load the dataframe
df = pd.read_csv('life_expectancy.csv')

# Inspect the dataframe
print(df.head())
print(df.info())

# Save to JSON
json_filename = 'life_expectancy.json'
df.to_json(json_filename, orient='records', indent=4)

print(f"File saved as {json_filename}")