from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Library import ConfigReader


class InquiryCreation:
    def __init__(self, obj):
        global driver
        driver = obj


def ClickInquiry(self,CreateInquiry):
    driver.find_element(By.XPATH, (ConfigReader.fetchInquiryCreation('InquiryCreation', 'CreateInquiry'))).send_keys(Keys.ENTER)


def SelectCreateInquiry(self,CreateInquiry):
    Create_Inquiry = driver.find_element(By.LINK_TEXT, "Create Inquiry")
    driver.execute_script("arguments[0].click();", Create_Inquiry)


def Enter_ShipperName(self, Shippername):
    driver.find_element(By.XPATH,
                        (ConfigReader.fetchInquiryCreation('InquiryCreation', 'ShipperNameTextfield'))).send_keys(
        "Deepak_Shipper_UAE01-OE1")


def DownArrow(self,Shippername):
    driver.find_element(By.XPATH,
                        (ConfigReader.fetchInquiryCreation('InquiryCreation', 'ShipperNameTextfield'))).send_keys(
        Keys.ARROW_DOWN)
    driver.find_element(By.XPATH,
                        (ConfigReader.fetchInquiryCreation('InquiryCreation', 'ShipperNameTextfield'))).send_keys(
        Keys.ENTER)
