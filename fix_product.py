import json
from selenium import webdriver 
from selenium.webdriver.common.by import By

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

f = open('products.json')

data = json.load(f)
f.close()

# Iterating through the json
# list

def fix_products():
    count = 0    
    for i in data['data']:
        if (len(i['imgUrls']) < 3):
            count+=1
            while (1):
                try:
                    i['imgUrls'] = searchImages(
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
            
            dictionary = {
                "data": data['data'],
            }
                    
            # Writing to sample.json
            with open("products.json", "w") as outfile:
                json.dump(dictionary, outfile)

            print("Fixed ", i['id'], count)

def checkError():
    count = 0     
    for i in data['data']:
        if (len(i['imgUrls']) < 3):
            count+=1
            # print(i['id'])
    print('Count: ',count)       

# Closing file

checkError()
# fix_products()

driver.quit()