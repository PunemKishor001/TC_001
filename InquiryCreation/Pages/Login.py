from selenium.webdriver.common.by import By

from Library import ConfigReader


class Login:
    def __init__(self,obj):
        global driver
        driver = obj
    def Login_Username(self,Username):
        driver.find_element(By.XPATH, (ConfigReader.fetchLoginLocators('LoginCredentials', 'Username'))).send_keys(
            "test1@trukker.com")

    def Login_password(self,Password):
        driver.find_element(By.XPATH, (ConfigReader.fetchLoginLocators('LoginCredentials', 'Password'))).send_keys(
            "trukker@123")

    def Login_Button(self):
        driver.find_element(By.XPATH, (ConfigReader.fetchLoginLocators('LoginCredentials', 'Button'))).click()