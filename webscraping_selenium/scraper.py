from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from bs4 import BeautifulSoup
import pandas as pd
import os

path="C:\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.sbipensionfunds.com/historical-nav/")  

def automated_data_entry():     # FILLS DATES USING SELENIUM

    #Enters the start date
    driver.find_element_by_name("fromdate").send_keys("15-05-2009")

    #Enters the End date
    driver.find_element_by_name("todate").send_keys(date.today().strftime("%d-%m-%Y"))

    #click Submit Button
    driver.find_element_by_name("mysubmit").click()
    
    # Keep script waiting before next page loads
    driver.implicitly_wait(5)
    scrape()

def scrape():             # THIS FUNCTIONS EXTRACTS DATA FROM SITE USING BEAUTIFUL SOUP
    
    data_storage = []
    source_code = driver.page_source
    soup = BeautifulSoup(source_code, 'lxml')

    table = soup.find("table", class_="table table-hover table-condensed table-bordered")
    table_rows = table.find_all("tr")
    
    # Following snippet adds Scraped data in a list 'Data_storage'
    for table_row in table_rows:
        cells_data = table_row.find_all("td")
        data=[cell_data.text.strip() for cell_data in cells_data]
        data_storage.append(data)
    

    # FOLLOWING SNIPPIT SAVE THE SCRAPED DATA IN A CSV FILE
    csv_data = pd.DataFrame(data_storage)
    csv_data.to_csv('scraped_data.csv', index=False)
    
        
def main():
    automated_data_entry()
    os.system('cls||clear')
    print("TASK COMPLETED !\nDATA SCRAPED SUCESSFULLY.")
    driver.quit()

if __name__ == "__main__":
    main()

# CREATED BY PRATHAM BHATNAGAR.