from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd

# NASA Exoplanet URL
START_URL="https://science.nasa.gov/exoplanets/exoplanet-catalog/"

# Webdriver
browser=webdriver.Edge("msedgedriver.exe")
browser.get(START_URL)

time.sleep(10)


planet_data=[]
# Define Exoplanet Data Scrapping Method
def scrape():

    for i in range(0,10):
        print(f"Scrapping page {i+1}")

     
        
        # BeautifulSoup Object     
        soup=BeautifulSoup(browser.page_source,"html.parser")
       

        # Loop to find element using XPATH
        for ul_tag in soup.find_all("ul",attrs={"class":"exoplanet"}):
            li_tags=ul_tag.find_all("li")

            temp_list=[]
            for index, li_tag in enumerate(li_tag):

                if index==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:    
                        temp_list.append("")    
            planet_data.append(temp_list) 


    print(planet_data[1])                   



       
                   

        # Find all elements on the page and click to move to the next page
       

# Calling Method  
scrape()  

# Define Header


# Define pandas DataFrame  

# Convert to CSV
