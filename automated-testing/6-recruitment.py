import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "https://opensource-demo.orangehrmlive.com/"
username = "Admin"
password = "admin123"

class Job(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
     
    # Test Case Recruitment Positive
    def test_a_search_candidates(self): 

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click()
        time.sleep(1)
        driver.find_element(By.ID,"candidateSearch_candidateName").send_keys("Archie Augustine") 
        time.sleep(1)
        driver.find_element(By.ID,"btnSrch").click() 
        time.sleep(3)

        validation = driver.find_element(By.ID,"resultTable").text
        self.assertIn('Archie Augustine', validation)
    
    def tearDown(self): 
        self.driver.close() 


if __name__ == "__main__": 
    unittest.main()   