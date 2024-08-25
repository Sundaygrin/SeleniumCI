from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class TestSuccessfulLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://enum.africa/login")

    def test_successful_login(self):
        driver = self.driver
        driver.find_element(By.ID, "talentLogInEmail").send_keys("9a54dbd64f@mailmaxy.one")
        driver.find_element(By.ID, "TalentLoginPassword").send_keys("Sunday@222")

        login_button = driver.find_element(By.ID, "login-button")
        driver.execute_script("arguments[0].click();", login_button)

    def tearDown(self):
        self.driver.quit()


class TestFailedLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://enum.africa/login")

    def test_failed_login(self):
        driver = self.driver
        driver.find_element(By.ID, "talentLogInEmail").send_keys("9a54d3dffddf@mailmaxy.one")
        driver.find_element(By.ID, "TalentLoginPassword").send_keys("dewdfds@!333")

        login_button = driver.find_element(By.ID, "login-button")
        driver.execute_script("arguments[0].click();", login_button)

        # Uncomment the following lines if you want to validate the error message
        # wait = WebDriverWait(driver, 10)
        # error_message_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login_alert_error")))
        #
        # error_message = error_message_element.text
        # self.assertEqual(error_message, "Invalid User Credentials")

    def tearDown(self):
        self.driver.quit()


class TestDisplayErrorMessage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://enum.africa/login")

    def test_invalid_login_details(self):
        driver = self.driver

        # Enter email and password
        driver.find_element(By.ID, "talentLogInEmail").send_keys("Admin@gmail.com")
        driver.find_element(By.ID, "TalentLoginPassword").send_keys("Sunday@222")

        # Click the login button
        login_button = driver.find_element(By.ID, "login-button")
        driver.execute_script("arguments[0].click();", login_button)

        # Wait for the error message to be visible and verify its presence
        wait = WebDriverWait(driver, 10)
        error_message_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tw-mb-5")))

        # Verify that the error message contains the text "Invalid User Credentials"
        self.assertIn("Invalid User Credentials", error_message_element.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
