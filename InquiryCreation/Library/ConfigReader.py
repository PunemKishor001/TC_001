import configparser


def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigurationFiles/Config.cfg")
    return config.get(section, key)


def fetchLoginLocators(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigurationFiles/LoginCredentials.cfg")
    return config.get(section, key)

def fetchInquiryCreation(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigurationFiles/InquiryCreation.cfg")
    return config.get(section, key)

def fetchViewShipper(section, key):
    config = configparser.ConfigParser()
    config.read("../ConfigurationFiles/ViewShipper.cfg")
    return config.get(section, key)

#print(readConfigData('Details', 'Username'))
