
import pandas as pd
import csv
import json

file = open("data/styles.csv")

csvreader = csv.DictReader(file)

rows = []
i = 0
for row in csvreader:
    i = i + 1
    rows.append(row)
    if (i == 1000):
        break

file.close()

dictionary = {
    "data": rows,
}
 
# Writing to sample.json
with open("products.json", "w") as outfile:
    json.dump(dictionary, outfile)
