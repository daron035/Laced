# from pprint import pprint
# from typing import List, Optional
# from pydantic import BaseModel
#
#
# class V(BaseModel):
#     id: int
#     UK: float
#     EU: float
#
#
# class DataFieldModel(BaseModel):
#     description: str
#     sku: str
#     year_released: int
#     colour: str
#     # variations: Optional[List[V]]
#     # variations: list[V] | None
#
#
# # class M(BaseModel):
#
#
# # class VariationsProp(DataFieldModel):
# class VariationsProp(BaseModel):
#     id: int
#     UK: float
#     EU: float
#     # price: float
#
#
# p1 = {
#     "description": "desc",
#     "sku": "ID2350",
#     "year_released": 32,
#     "colour": "red",
#     # "variations": None,
# }
#
# v1 = {
#     # "description": "desc",
#     # "sku": "ID2350",
#     # "year_released": 32,
#     # "colour": "red",
#     "id": 33,
#     "UK": 3.0,
#     "EU": 36.0,
#     # "price": {"GBP": 130, "EUR": 150},
# }
#
# prod1 = DataFieldModel(**p1)
# pprint(prod1.model_dump())
#
# # var1 = VariationsProp(**v1)
# # pprint(var1.model_dump())


# import pandas as pd
#
# # Define the data in a list
# data_list = [
#     ['id', 'UK', 'EU', {'price': ["GBP", "EUR"]}],
#     [33, 3, 36, [130, 150]],
#     [41, 4, 37, [140, 160]],
#     [52, 5, 38, [150, 180]],
# ]
#
# # Extract the columns from the first row
# columns = data[0]
#
# # Extract the rows from the remaining data
# rows = data[1:]
#
# # Create a pandas DataFrame using the extracted columns and rows
# df = pd.DataFrame(rows, columns=columns)
#
# # Display the DataFrame
# print(df)

# from pprint import pprint
# import pandas as pd
# from pandas import json_normalize
#
# # Your list of nested JSON data
data_list = [
    {
        "id": 33,
        "uk": 3,
        "eu": 36,
        "price": [
            {"gbp": 130},
            {"eur": 160},
        ],
    },
    {
        "id": 41,
        "uk": 4,
        "eu": 37,
        "price": [
            {"gbp": 140},
            {"eur": 180},
        ],
    },
]
# # Initialize an empty DataFrame
# df = pd.DataFrame()
#
# # Process each JSON object and concatenate the results
# for data in data_list:
#     df = pd.concat([df, json_normalize(data, sep="_")], ignore_index=True)
#
# # Display the DataFrame
# print(df)
#
# json_data = df.to_json(orient="records")
# # pprint(json_data)


from pprint import pprint

import pandas as pd
from pandas import json_normalize


# Column names
columns = ["id", "uk", "eu", "price"]

# Your list of nested JSON data
data_list = [
    [33, 3.3, 36, {"gbp": 130, "eur": 160}],
    [41, 4.0, 37, {"gbp": 140, "eur": 180}],
]

# Initialize an empty DataFrame
df = pd.DataFrame()

# print(df)

# Process each list and concatenate the results
for data in data_list:
    data_dict = dict(zip(columns, data))
    # df = pd.concat([df, json_normalize(data_dict, sep="_")], ignore_index=True)
    df = pd.concat([df, json_normalize(data_dict)], ignore_index=True)

json_data = df.to_json(orient="records")
json_dict = {"sizes": json_data}
# Display the DataFrame
# print(df)
# print(df.shape)
# print(df.dtypes)
# print(df[0:1])
# print(df.loc[0])
# print(df.iloc[0])

json_data = df.to_json(orient="records")
# json_data = df.to_json()
# json_data = df[0:1].to_json(orient="records")
# json_data = df.iloc[0].to_json(orient="records")
pprint(json_data)
