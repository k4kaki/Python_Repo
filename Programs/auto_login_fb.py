from selenium import webdriver
import time
def fb_login():
    browser=webdriver.Firefox()
    browser.get('https://www.facebook.com')
    time.sleep(10)
    #user credentials 
    user=browser.find_element_by_css_selector('#email')
    user.send_keys('8688992211')
    passwd=browser.find_element_by_css_selector('#pass')
    passwd.send_keys('Libf#491092')
    login=browser.find_element_by_css_selector('#u_0_8')
    login.click()
fb_login()
