#!/usr/bin/python
# -*- coding: utf-8 -*-
# in the end, the CAPTCHA showed up 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox()
browser.get('https://taojinbi.taobao.com')
login_btn = browser.find_element_by_link_text("登录查看金币明细")
login_btn.click()
print "after click login btn"
browser.implicitly_wait(8) # seconds
print "trying to find form"
# switch to frame finally works when using css selector
browser.switch_to_frame(browser.find_element(By.CSS_SELECTOR, "iframe[class='mnl-ifr']"))
username = browser.find_element_by_id("TPL_username_1")
password = browser.find_element_by_css_selector("#TPL_password_1")
username.send_keys("xxx")
password.send_keys("xxx")
browser.find_element_by_css_selector("#J_SubmitStatic").click()
browser.implicitly_wait(5) # seconds
get_today_btn = browser.find_element_by_class_name("J_GoTodayBtn")
get_today_btn.click()
