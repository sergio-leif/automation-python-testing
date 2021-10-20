from selenium import webdriver

chrome_browser = webdriver.Chrome('./driver/chromedriver')

chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

assert 'Selenium Easy' in chrome_browser.title # Fail in case is false

# <button type="button" onclick="showInput();" class="btn btn-default">Show Message</button>

show_message_button = chrome_browser.find_element_by_class_name('btn-default') # Find specific class
print(show_message_button.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

# <input type="text" class="form-control" placeholder="Please enter your Message" id="user-message">
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am suuuuuper cool')

show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'I am suuuuuper cool' in output_message.text

chrome_browser.quit()