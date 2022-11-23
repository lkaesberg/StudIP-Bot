import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import re

from selenium.webdriver.support.wait import WebDriverWait

from credentials import username, password


def login(driver):
    print("Loading StudIP...")
    driver.get("https://studip.uni-goettingen.de/")
    print("Login")
    driver.find_element(By.CSS_SELECTOR, "#loginname").send_keys(username)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, ".accept").click()
    print("Finished")


def get_score(driver: WebDriver, username):
    driver.get(f"https://studip.uni-goettingen.de/dispatch.php/profile?username={username}")
    try:
        score = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[5]/div[2]/div[1]/section/div[2]/div[2]/div[2]/div[2]/a/div[1]"))).text
        score = int(score.split(" ")[1].replace(".", ""))
        return score

    except:
        return None
