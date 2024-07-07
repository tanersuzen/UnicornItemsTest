import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestErrorMessage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_login_error_message(self):
        driver = self.driver
        driver.get("http://unicornitems.com/my-account/")
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME, "username")))
        login_input = driver.find_element(By.NAME, "username")
        password_input = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.NAME, "login")
        login_input.send_keys("123")
        password_input.send_keys("123")
        login_button.click()
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "woocommerce-error")))
        assert ": Incorrect username or password." in driver.page_source

    def tearDown(self) ->None:
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
