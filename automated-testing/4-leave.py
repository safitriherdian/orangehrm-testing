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
     
    # Test Case Leave Negative
    def test_a_search_data_not_found(self):

        driver = self.driver
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.ID,"txtUsername").send_keys(username)
        time.sleep(1)
        driver.find_element(By.ID,"txtPassword").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(1)

        driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/a/b").click()
        time.sleep(1)
        driver.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys("zzz") 
        time.sleep(1)
        driver.find_element(By.ID,"btnSearch").click() 
        time.sleep(1)
        
        response_message = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[3]/table/tbody").text
        self.assertIn('No Records', response_message)

    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()   