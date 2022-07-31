import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    # Test Case Login Positive
    def test_a_success_login(self):

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

        current_url = driver.current_url
        self.assertIn(
            current_url, 'https://opensource-demo.orangehrmlive.com/index.php/dashboard')

    # Test Case Login Negative
    def test_b_failed_login_with_wrong_pass(self):

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, "Invalid credentials")

    # Test Case Login Negative
    def test_c_failed_login_with_empty_data(self):

        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(3)
        driver.find_element(By.ID, "txtUsername").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, "txtPassword").send_keys("")
        time.sleep(1)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(1)

        response_message = driver.find_element(By.ID, "spanMessage").text
        self.assertEqual(response_message, "Username cannot be empty")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
