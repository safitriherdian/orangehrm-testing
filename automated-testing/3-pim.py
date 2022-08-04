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
     
    # Test Case PIM Positive
    def test_a_search_employee(self): 

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        driver.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        driver.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Aaliyah Haq")  
        time.sleep(1)
        driver.find_element(By.ID,"searchBtn").click()
   

        response_data = driver.find_element(By.ID,"resultTable").text
        self.assertIn('Aaliyah',response_data)   

    
    def tearDown(self): 
        self.driver.close() 


if __name__ == "__main__": 
    unittest.main()   