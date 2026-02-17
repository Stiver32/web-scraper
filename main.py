from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\camer\\Downloads\\chromedriver.exe")

def get_driver():
    
    # set options for the Chrome driver
    options = webdriver.ChromeOptions() # Add any desired options/flags here
    options.add_argument("disable-infobars") # option to disable infobars
    options.add_argument("start-maximized") # option to start maximized
    options.add_argument("disable-dev-shm-usage") # option to disable /dev/shm usage
    options.add_argument("no-sandbox") # option to disable sandboxing. disabling gives more privileges to the browser
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # option to exclude the "enable-automation" switch
    options.add_argument("disable-blink-features=AutomationControlled") # option to disable the "AutomationControlled" feature
    
    
    driver = webdriver.Chrome(service=service)
    driver.get("http://automated.pythonanywhere.com") # connect driver to a webpage
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())