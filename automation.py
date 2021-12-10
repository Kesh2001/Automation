# This wont really work cause this url is not secure
from selenium import webdriver

chrome_browser=webdriver.Chrome('./chromedriver')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title # if false errorss out the program
show_meassage_button=chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source
chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOL')
show_message_button.click()
output_message=chrome_browser.find_element_by_id('display')
assert 'I AM EXTRA COOL' in output_message.text

user_button2=chrome_browser.find_element_by_css_selector('#get-input>.btn')
print(user_button2)

chrome_browser.close()
# or chrome_browser.quit()  # to close the program with it
