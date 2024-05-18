import pandas as pd
from pandas import json_normalize

# Updated Column names
columns = ["id", "uk", "eu", ["gbp", "eur"]]

# Your list of nested JSON data
data_list = [
    [33, 3.3, 36, [130, 160]],
    [41, 4.0, 37, [140, 180]],
]

# Initialize an empty DataFrame
df = pd.DataFrame(data_list, columns=columns)

# Flatten the nested lists using json_normalize
for col in columns:
    if isinstance(col, list):
        df = pd.concat(
            [df, json_normalize(df[col].apply(lambda x: dict(zip(col, x))))], axis=1
        )
        df = df.drop(columns=[col])

# Convert DataFrame to JSON string
json_data = df.to_json(orient="records")
print(json_data)
