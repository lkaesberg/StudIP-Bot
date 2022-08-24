from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from lorem_text import lorem
from time import sleep

from credentials import message_time
from tools.utils import login


def main():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver")

    login(driver)
    driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div/table[1]/tbody/tr[7]/td[5]/a[1]").click()
    while True:
        print("Send Message")
        driver.find_element(By.XPATH,
                            "/html/body/div/div[5]/div[2]/div[2]/div/div[1]/div/div[3]/textarea[2]").send_keys(
            lorem.sentence())
        driver.find_element(By.XPATH, "/html/body/div/div[5]/div[2]/div[2]/div/div[1]/div/div[3]/a/img").click()
        sleep(message_time)


if __name__ == '__main__':
    main()
