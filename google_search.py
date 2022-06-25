from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome(service=Service('C:\\Program Files (x86)\\chromedriver.exe'))

driver.get("https://google.com")
try:
	search = driver.find_element(By.NAME,'q')
	search.send_keys("test")
	search.send_keys(Keys.ENTER)

	main = WebDriverWait(driver, 5).until(
		EC.visibility_of_element_located((By.ID, 'main'))
		)

	results = main.find_elements(By.CLASS_NAME, "yuRUbf")

	for result in results:
		selection = result.find_element(By.TAG_NAME,'a')
		link = selection.get_attribute("href")
		print(link)

	driver.quit()
except Exception as e:
	print(e)
	driver.quit()