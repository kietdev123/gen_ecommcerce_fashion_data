import json
from selenium import webdriver 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 

def searchImages(searchKey, index):
    #  "Men Footwear Sandal summer"
    driver.get("https://www.google.com/search?q=" + searchKey )

    aResults = driver.find_elements(By.XPATH,"//div[@class='crJ18e']//div//a")
    # time.sleep(1)
    # click to shopping tag
    aResults[index].click()

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

f = open('type.json')

data = json.load(f)
f.close()

# Iterating through the json
# list

dictionary = data
def main():
    count = 0    
    for i,gender in enumerate(data['genders']):
        imgUrls = []
        value = gender + "Urls"
        if value in data: continue
        for j,masterCategory  in enumerate(data['masterCategorys']):
            # print(i, gender, j, masterCategory)
            
            index = 0
            while (1):
                try:
                        imgUrls.append(searchImages(
                                gender+ " " +
                                masterCategory
                                , index)[0])
                   
                        break
                except:
                        print("An exception occurred")
                        index+=1
                        if (index == 3): index =0
         # Writing to sample.json
        dictionary[gender + "Urls"] = imgUrls
        
        with open("type.json", "w") as outfile:
            json.dump(dictionary, outfile)

        # print("Fixed ", i,j, count)        
              
                        
           
                

main()


driver.quit()