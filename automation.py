from selenium import webdriver

chrome_browser = webdriver.Chrome('./driver/chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/')

assert 'Selenium Easy' in chrome_browser.title # Fail in case is false

chrome_browser.close()