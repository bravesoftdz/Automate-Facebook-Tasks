
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
try:
	browser.get('http://facebook.com')

	email = browser.find_element_by_id('email')
	password = browser.find_element_by_id('pass')

	email.send_keys('')
	password.send_keys('')
	login = browser.find_element_by_xpath("//input[@value='Entrar']")
	login.click()

	browser.get('https://www.facebook.com/saved')
	saved = browser.find_elements_by_id('saveContentFragment')
	print(saved)
	for e in saved:
		print(e.text)

finally:
	browser.close()

