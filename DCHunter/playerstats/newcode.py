import pandas as pd

# Sample DataFrame with a date column
data = {'DateColumn': ['2023-09-14 08:00:00', '2023-09-14 09:00:00', '2023-09-15 10:00:00', '2023-09-16 11:00:00']}
df = pd.DataFrame(data)

# Convert the 'DateColumn' to datetime
df['DateColumn'] = pd.to_datetime(df['DateColumn'])

# Convert the Timestamp objects to string
df['DateColumn'] = df['DateColumn'].dt.strftime('%Y-%m-%d %H:%M:%S')

# Convert the DataFrame to a JSON object
json_data = df.to_json(orient='records', date_format='iso')

print(json_data)
