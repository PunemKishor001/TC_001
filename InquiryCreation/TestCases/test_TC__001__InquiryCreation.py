import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Base import BaseUrl
from Library import ConfigReader
from Pages import CreateInquiry

def test_CreateInquiry():
    driver = BaseUrl.Launchbrowser()
    time.sleep(10)
    #driver.save_screenshot("./ScreenShot/errorfullpage.jpg")
    #CreateInquiry.InquiryCreation(driver)
    #CreateInquiry.ClickInquiry()
    driver.find_element(By.XPATH, (ConfigReader.fetchInquiryCreation('InquiryCreation', 'CreateInquiry'))).send_keys(
        Keys.ENTER)
    Create_Inquiry = driver.find_element(By.LINK_TEXT, "Create Inquiry")
    driver.execute_script("arguments[0].click();", Create_Inquiry)
    time.sleep(5)
    driver.find_element(By.XPATH,
                            (ConfigReader.fetchInquiryCreation('InquiryCreation', 'ShipperNameTextfield'))).send_keys(
            "Deepak_Shipper_UAE01-OE1")
    time.sleep(10)
    driver.find_element(By.XPATH,
                            (ConfigReader.fetchInquiryCreation('InquiryCreation', 'ShipperNameTextfield'))).send_keys(
            Keys.ARROW_DOWN)
    driver.find_element(By.XPATH,
                            (ConfigReader.fetchInquiryCreation('InquiryCreation', 'ShipperNameTextfield'))).send_keys(
            Keys.ENTER)

