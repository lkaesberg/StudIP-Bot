from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from credentials import username, password
from lorem_text import lorem
from time import sleep


options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


print("Loading StudIP...")
driver.get("https://studip.uni-goettingen.de/")
print("Login")
driver.find_element(By.CSS_SELECTOR, "#loginname").send_keys(username)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
driver.find_element(By.CSS_SELECTOR, ".accept").click()
print("Finished")
driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div/table[1]/tbody/tr[7]/td[5]/a[1]").click()
while True:
	print("Send Message")
	driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div/div[1]/div/div[3]/textarea[2]").send_keys(lorem.sentence())
	driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div/div[1]/div/div[3]/a/img").click()
	sleep(600)

