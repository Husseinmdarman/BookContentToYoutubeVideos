from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class scrapebook():
    
    def __init__(self, isbn) -> None:
        """
        SETUP the init method of the class

        parameter: ISBN number of the book

        example: 9781838559984
        """
        self.url = f"https://www.perlego.com/search?query={isbn}"
        
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,1)
        
    def loadwebpage(self):
        """
        uses the url of the webpage that had been setup in the init method and 
        clicks till it reaches the table of content
        """
        self.driver.get(self.url)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid*='Cookies']"))).click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test-locator*='new-book']"))).click()

        self.driver.find_element(By.XPATH, "(//*[contains(text(),'Table of contents')])[1]").click()
        pass

    def soupingthecontent(self):
        """
        Once reached we get the page source and find all the texts 
        under the table of content and returns the  striped list back to
        """
        soup = BeautifulSoup(self.driver.page_source,"html.parser")

        results = soup.find_all(attrs={'class': ['sc-b81fc1ca-2','kydYov']}, text=True)

        table_of_content = []
        for x in results:
            table_of_content.append(x.text)
        return table_of_content 


