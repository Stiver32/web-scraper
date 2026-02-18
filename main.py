from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

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



def clean_text(text):
    # extract only temp from text
    output = float(text.split(": ")[1]) # split the text by ": " and take the second part, then convert it to a float... this assumes the text is in the format "Temperature: 20.5"
    return output



def main():
    driver = get_driver()
    time.sleep(5) # wait for the page to load before trying to find the element 
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)



print(main())