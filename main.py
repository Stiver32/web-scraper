from selenium import webdriver # import the webdriver module from the selenium package, which provides a way to automate web browsers. This allows us to control a web browser (like Chrome) programmatically, enabling us to interact with web pages, fill out forms, click buttons, and extract information from websites.

from selenium.webdriver.chrome.service import Service # import the Service class from the selenium.webdriver.chrome.service module, which is used to manage the ChromeDriver service. This allows us to specify the path to the ChromeDriver executable and control its lifecycle (starting and stopping the service) when using Selenium to automate browser interactions.

from selenium.webdriver.common.keys import Keys # import the Keys class from the selenium.webdriver.common.keys module, which provides a set of constants representing keyboard keys (like ENTER, TAB, etc.) that can be used to simulate keyboard input in web automation tasks.

import time # import the time module, which will be used to introduce a delay (using time.sleep) to allow the web page to load before attempting to find and interact with elements on the page.

from datetime import datetime as dt # import the datetime class from the datetime module and alias it as dt. This will be used to generate timestamps for the filenames when saving the temperature data.



service = Service("C:\\Users\\camer\\Downloads\\chromedriver.exe")

def get_driver(): # function get_driver will set up and return a Chrome WebDriver instance.
    
    # set options for the Chrome driver
    options = webdriver.ChromeOptions() # Add any desired options/flags here
    options.add_argument("disable-infobars") # option to disable infobars
    options.add_argument("start-maximized") # option to start maximized
    options.add_argument("disable-dev-shm-usage") # option to disable /dev/shm usage
    options.add_argument("no-sandbox") # option to disable sandboxing. disabling gives more privileges to the browser
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) # option to exclude the "enable-automation" switch
    options.add_argument("disable-blink-features=AutomationControlled") # option to disable the "AutomationControlled" feature
    
    #
    driver = webdriver.Chrome(service=service) # create a new instance of the Chrome WebDriver using the specified service and options. 
    driver.get("http://automated.pythonanywhere.com") # connect driver to a webpage
    return driver



def clean_text(text):
    # extract only temp from text
    output = float(text.split(": ")[1]) # split the text by ": " and take the second part, then convert it to a float... this assumes the text is in the format "Temperature: 20.5"
    return output

def write_file(text):
    # create a filename based on the current date and time, formatted as "YYYY-MM-DD.HH-MM-SS.txt"
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt" 
    
    with open(filename, "w") as f: # open the file in write mode
        f.write(text)

def main():
    driver = get_driver()
    loop_num = 5 # number of iterations to run the loop
    
    while loop_num > 0: # loop until the specified number of iterations has been reached
        time.sleep(5) # wait for 5 seconds before each iteration 
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]") # find the element containing the temperature information using its XPath.
        text = str(clean_text(element.text)) # get text content of the element, clean it w/ the clean_text function to extract the temp value, convert it to a string
        write_file(text) # write the cleaned text (temperature value) to a file using the write_file function
        loop_num -= 1 # decrement the loop counter




print(main())