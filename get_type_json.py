
import pandas as pd
import csv
import json

file = open("data/styles.csv")

csvreader = csv.reader(file)

header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)


# Create the pandas DataFrame
df = pd.DataFrame(rows, columns=header)
df = df.head(1000)

file.close()

genders = []
masterCategorys = []
subCategorys = []

for col in df:
    if (col == "gender"):
        genders = df[col].unique()
    if (col == "masterCategory"): 
        masterCategorys = df[col].unique()
    if (col == "subCategory"):
          subCategorys = df[col].unique()

print(genders)
print(masterCategorys)
print(subCategorys)

dictionary = {
    "genders": genders.tolist(),
    "masterCategorys" : masterCategorys.tolist(),
    "subCategorys" : subCategorys.tolist(),
}
 
# Writing to sample.json
with open("type.json", "w") as outfile:
    json.dump(dictionary, outfile)
