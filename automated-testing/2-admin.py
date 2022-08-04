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
     
    # Test Case Admin Positive
    def test_a_input_and_reset(self):
        
        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)
        
        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click()
        time.sleep(1)
        select = select(driver.find_element(By.ID,'searchSystemUser_userType'))
        select.select_by_visible_text('Admin')
        time.sleep(1)
        select = select(driver.find_element(By.ID,'searchSystemUser_status'))
        select.select_by_visible_text('Enabled')
        time.sleep(1)
        
        driver.find_element(By.ID,"searchSystemUser_userName").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID,"searchSystemUser_employeeName_empName").send_keys("Saf")
        time.sleep(1)
        driver.find_element(By.ID,"resetBtn").click()
        time.sleep(3)

        validation = driver.find_element(By.ID,"searchSystemUser_userName").get_attribute("value")
        self.assertIn('', validation)

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()   