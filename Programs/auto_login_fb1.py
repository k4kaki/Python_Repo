from selenium import webdriver
import time
def gmail_login():
    browser=webdriver.Firefox()
    browser.get('https://www.gmail.com')
    time.sleep(5)
    #user credentials 
    login=browser.find_element_by_css_selector('#identifierLink')
    login.click()
    user=browser.find_element_by_css_selector('#identifierId')
    user.send_keys('140eight')
    user_next=browser.find_element_by_css_selector('#identifierNext')
    user_next.click()
    passwd=browser.find_element_by_css_selector('#password')
    passwd.send_keys('Libp@1408')
    login_end=browser.find_element_by_css_selector('#passwordNext')
    login_end.click()
gmail_login()
