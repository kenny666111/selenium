#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://taojinbi.taobao.com')
login_btn = browser.find_element_by_link_text("登录查看金币明细")
print "move mouse to login button"
action = webdriver.ActionChains(browser)
action.move_to_element(login_btn)
action.click(login_btn)
action.perform()
print "after click login btn"
browser.implicitly_wait(8) # seconds
# switch to frame finally works when using css selector
browser.switch_to_frame(browser.find_element(By.CSS_SELECTOR, "iframe[class='mnl-ifr']"))
new_action = webdriver.ActionChains(browser)
username = browser.find_element_by_id("TPL_username_1")
password = browser.find_element_by_css_selector("#TPL_password_1")
new_action.move_to_element(username)
print "click username box"
new_action.click(username)
new_action.perform()
username.send_keys("xxx")
new_action.move_to_element(password)
print "click password box"
new_action.click(password)
new_action.perform()
password.send_keys("xxx")
submit_btn = browser.find_element_by_css_selector("#J_SubmitStatic")
new_action.move_to_element(submit_btn)
print "click submit btn"
new_action.click(submit_btn)
new_action.perform()
browser.implicitly_wait(5) # seconds
browser.switch_to_default_content()
get_today_btn = browser.find_element_by_class_name("J_GoTodayBtn")
new_action_2 = webdriver.ActionChains(browser)
new_action_2.move_to_element(get_today_btn)
new_action_2.click(get_today_btn)
new_action_2.perform()
