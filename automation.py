from selenium import webdriver

chrome_browser = webdriver.Chrome('./driver/chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.title # Fail in case is false

# <button type="button" onclick="showInput();" class="btn btn-default">Show Message</button>

button = chrome_browser.find_element_by_class_name('btn-default') # Find specific class

print(button.get_attribute('innerHTML'))
chrome_browser.close()