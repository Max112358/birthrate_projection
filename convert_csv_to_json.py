import pandas as pd

# Load the dataframe
df = pd.read_csv('population_distribution.csv')

# Inspect the dataframe
print(df.head())
print(df.info())

# Save to JSON
json_filename = 'population_distribution.json'
df.to_json(json_filename, orient='records', indent=4)

print(f"File saved as {json_filename}")