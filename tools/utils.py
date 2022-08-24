from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
import re

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
    score = driver.find_element(By.CSS_SELECTOR,
                                "div.minor:nth-child(2) > a:nth-child(1) > div:nth-child(1)").text
    score = int(score.split(" ")[1].replace(".", ""))
    return score
