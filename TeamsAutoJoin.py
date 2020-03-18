# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:23:29 2020

@author: C21David.Thacker
"""

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import time
import sys


def login(driver):
	driver.get("https://teams.microsoft.com/_#/school//?ctx=teamsGrid")
	time.sleep(4)
	while(True):
		print("\nInsert Username\n")
		email_input = driver.find_element_by_name('loginfmt')
		signin_button = driver.find_element_by_id('idSIButton9')
		"""
		Insert username for user below in the quotes
		"""
		email_input.send_keys("")
		signin_button.click()
		time.sleep(3)
		print("\nInsert Password\n")
		password_input = driver.find_element_by_xpath("//input[@type='password']")
		"""
		Insert password for user below in the quotes
		"""
		password_input.send_keys("")
		time.sleep(1)
		signin_button = driver.find_element_by_id('idSIButton9')
		signin_button.click()
		time.sleep(5)
		print("\nBypassing Checkbox\n")
		newButton = driver.find_element_by_id('idSIButton9')
		newButton = driver.find_element_by_id('idSIButton9')
		newButton.click()
		try:
			WebDriverWait(driver, 5).until(expected_conditions.invisibility_of_element((By.CSS_SELECTOR, ".zb-progress-circular.orange.med.message-present.ember-view")))
		except:
			driver.quit()
			print("Timed out while authenticating login, aborting...")
			exit()
		if(driver.find_elements_by_xpath("//button[@disabled='']") or driver.find_elements_by_xpath("//div[contains(text(), 'Invalid email or password')]")):
			print("--Invalid email or password--\n")
			email_input.clear()
			password_input.clear()
		else:
			print("\nLogin Successful\n")
			break


print("\nHeadless Firefox browswer initiated.\n")
options = Options()
#browser = input("Choose the web browser you have installed:\n") #todo: give options for different installed browsers
driver = webdriver.Firefox(options = options)
login(driver)
print("Waiting for connection to Teams\n")
for remaining in range(10, 0, -1):
	sys.stdout.write("\r")
	sys.stdout.write("{:2d} seconds remaining.".format(remaining))
	sys.stdout.flush()
	time.sleep(1)
print("\nNavigating to Class Website\n")
driver.get("https://teams.microsoft.com/_#/school/conversations/General?threadId=19:6bcff50be57a4de59f0d29ce06258c49@thread.tacv2&ctx=channel")

time.sleep(100)
driver.quit()
print("Headless Firefox browser closed")
