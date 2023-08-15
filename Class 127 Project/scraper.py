from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.m.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(START_URL)

scraped_data=[]

def scrape():
    #Soup BS4
    soup = BeautifulSoup(browser.page_source, "html.parser")
    # Finding Class/Table/Row

    bright_star_table=soup.find("table",attrs={"class","wikitiable"})

    table_body=soup.find("tbody")

    table_rows=soup.find("tr")

    # Finding Data in the Columns
    for rows in table_rows: 
        table_colms=soup.find_all("td")

        temp_list=[]

        #Modifing Data  
        for col_data in table_colms:

            # Displaying only text using .text
            data=col_data.text

            #Removing Space using .strip()
            lst=data.strip()

            temp_list.append(data)

            scraped_data.append(temp_list)

scrape()

stars_data=[]    
for i in range(0,len(scraped_data)):
    name=scraped_data[i][1]
    dist=scraped_data[i][3]
    mass=scraped_data[i][5]
    r=scraped_data[i][6]
    lum=scraped_data[i][7]

    required_data=[name,dist,mass,r,lum]
    stars_data.append(required_data)


headers=["Name","Distance","Mass","Radius","Luminosity"]

star_df_1=pd.DataFrame(stars_data)

star_df_1.to_csv("Star Data.csv",index=True,index_label="id")
 
print(stars_data)

