from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ScholarScraper():
    
    def __init__(self, search_term: str) -> None:
        """
        Searches the term provided on google scholar which will be used
        to find pdfs related to that search term

        Input: search_term(str)
        """
        
        # replaces the spaces between characters with a plus sign which is needed when sending
        # scholar keyword search terms
        search_words = search_term.replace(" ", "+")
        

        self.url = f"https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={search_words}&btnG="
        
        #setting up drivers
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver,10)
    
    def open_webpage(self):
        """
        Opens the webpage

        Input: none
        Return: none
        """
        
        self.driver.get(self.url)

    def get_pdf_files(self) -> list:
        """
        Returns the pdf files that were found on the first search page of google

        Input: none
        Return: data (list)
        
        """

        # looks for all elements with that particular class due to pdf links have this similar class name
        container_pdf = self.wait.until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME,'gs_or_ggsm')))
        
        data = list()

        #iterate through the container pdf
        for elem in container_pdf:
           #there will be the whole elem being return but we need to drill down to where the href is kept
           href_object = elem.find_element(By.TAG_NAME, 'a')
           # now get the attribute of the href
           data.append(href_object.get_attribute('href'))
        
        return data