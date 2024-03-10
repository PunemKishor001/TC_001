import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base import BaseUrl
from Library import ConfigReader

def test_ViewShipper():
    driver = BaseUrl.Launchbrowser()
    time.sleep(10)
    # driver.save_screenshot("./ScreenShot/errorfullpage.jpg")
    driver.find_element(By.XPATH,(ConfigReader.fetchViewShipper('ViewShipper','ViewShipper'))).send_keys(Keys.ENTER)
    View_Shippers = driver.find_element(By.LINK_TEXT, "View Shippers")
    driver.execute_script("arguments[0].click();", View_Shippers)