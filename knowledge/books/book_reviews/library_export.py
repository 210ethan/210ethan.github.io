#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 19:45:46 2020

@author: EthanMorse
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

import sys
sys.path.append("/Users/EthanMorse/Documents/personal/Python")
from goodreads_info import em, pw

# open Chrome webdriver
driver = webdriver.Chrome(executable_path="/Users/EthanMorse/opt/anaconda3/lib/python3.7/site-packages/chromedriver")

# go to Goodreads sign in page
driver.get("https://www.goodreads.com/user/sign_in")

user_email = driver.find_element_by_id("user_email")
user_pw = driver.find_element_by_id("user_password")
login_button = driver.find_element_by_name("next")

# enter login info, log in
user_email.send_keys(em)
user_pw.send_keys(pw)
login_button.send_keys(Keys.RETURN)

# navigate to webpage, wait until fully open
driver.get("https://www.goodreads.com/review/import")


# find export button 
export_button = driver.find_element_by_class_name("gr-form--compact__submitButton")

# press enter on export button
export_button.send_keys(Keys.RETURN)

# wait for library to be exported
time.sleep(60)

# go to link
driver.get("https://www.goodreads.com/review_porter/export/75258150/goodreads_export.csv")


time.sleep(60)

# close Chrome webdriver
driver.close()