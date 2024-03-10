from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from Library import ConfigReader
from Pages import Login


def Launchbrowser():
    global driver
    # driver = webdriver.Chrome(executable_path="C:\\Users\\Punem Kishor Babu\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")

    if ((ConfigReader.readConfigData('Details', 'Browser')) == 'Chrome'):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif ((ConfigReader.readConfigData('Details', 'Browser')) == 'FireFox'):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(ConfigReader.readConfigData('Details', 'Application_Url'))
    driver.maximize_window()
    title = driver.title
    print(title)
    driver.implicitly_wait(20)
    login = Login.Login(driver)
    login.Login_Username('test1@trukker.com')
    login.Login_password('trukker@123')
    login.Login_Button()
    title = driver.title
    print(title)
    return driver


def closeBrowser():
    driver.close()
