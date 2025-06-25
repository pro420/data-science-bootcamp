# https://api.nobelprize.org/v1/prize.json


import json
import numpy as np


with open("prize.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# print(data)
# print(type(data))

years = [prize["year"] for prize in data["prizes"]]

# print(years)

years_array = np.array(years)

unique_years, counts = np.unique(years_array, return_counts=True)

print("\n" + "-" * 32)
print(f"{'Year':<10} | {'Prizes Count':<15}")
for year, count in zip(unique_years, counts):
    print(f"{year:<10} | {count:<15}")
print("-" * 32)

# fix the logic of prize count per year
#  Total years present : 
#  Total prizes awarded : 
#  Total Laurates Honoured : 
#  Total unique categories : 

