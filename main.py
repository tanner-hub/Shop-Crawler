import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage')

baseDir = os.path.abspath(os.path.dirname(__file__))
sourcePath = baseDir + "/topmilus.csv"
archiveDir = baseDir + "/portal" #On server will be linked to "data/wet/archive"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

df = pd.read_csv(sourcePath)

index = 0
domain = ""
for row in df.itertuples():
    index = row[1]
    domain = str(row[2])

    print("+", str(index), " -> Pulling from ", domain)

    url = "https://www." + domain + "/"

    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, features='lxml')

        subArchiveDir = archiveDir + "/" + domain
        if not os.path.isdir(subArchiveDir):
            os.mkdir(subArchiveDir)
        with open(subArchiveDir + "/" + domain + ".html", "w") as file:
            file.write(str(soup))

        print("-", str(index), " <- Exiting from ", domain)
        
    except:
        print("Error: an error has occured durring file retreival for record ", str(index), ", domain ", domain)

driver.quit()