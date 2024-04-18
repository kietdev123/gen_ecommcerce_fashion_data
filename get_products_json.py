from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv
import json

driver = webdriver.Chrome() 

def searchImages(searchKey):
    #  "Men Footwear Sandal summer"
    driver.get("https://www.google.com/search?q=" + searchKey )

    aResults = driver.find_elements(By.XPATH,"//div[@class='crJ18e']//div//a")
    # time.sleep(1)
    # click to shopping tag
    aResults[1].click()

    imgResults = driver.find_elements(By.XPATH,"//div[@class='ArOc1c']//img")

    i = 0
    strs = []
    for img in imgResults:
        str = img.get_attribute('src')
        strs.append(str)
        # print(str)
        i += 1
        if (i == 3): break; 
    return strs


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

count = 0
for i in rows:
    while (1):
       try:
         i["imgUrls"] = searchImages(
            i["gender"] + " " +
            i["masterCategory"] +  " " +
            i["subCategory"] + " " +
            i["articleType"] +  " " +
            i["baseColour"] + " " +
            i["season"] +  " " +
            i["usage"] +  " " 
            )
         break
       except:
        print("An exception occurred")
  
    count +=1
    print("Crawled images for product ",count)
    
    dictionary = {
        "data": rows,
    }
    
    # Writing to sample.json
    with open("products.json", "w") as outfile:
        json.dump(dictionary, outfile)

driver.quit()
print("Done")