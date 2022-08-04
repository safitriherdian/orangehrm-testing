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
     
    # Test Case Time Negative
    def test_a_search_empty_data(self): 

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click()
        time.sleep(1)
        driver.find_element(By.ID,"employee").click() 
        time.sleep(1)
        driver.find_element(By.ID,"btnView").click() 
        time.sleep(1)

        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertIn('Required', response_message)
    
    def tearDown(self): 
        self.driver.close() 


if __name__ == "__main__": 
    unittest.main()   