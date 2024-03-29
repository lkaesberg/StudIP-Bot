from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from lorem_text import lorem
from time import sleep

from credentials import message_time
from tools.utils import login


def main():
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver")

    login(driver)
    driver.get("https://studip.uni-goettingen.de/dispatch.php/course/messenger/course?cid=3bef620d24272d395a5f0dde1e9799c1")
    sleep(10)
    while True:
        print("Send Message")
        words = 4
        driver.find_element(By.XPATH,
                            "/html/body/main/div/div/div[1]/div[1]/div/div[3]/textarea").send_keys(lorem.words(words))
        driver.find_element(By.XPATH, "/html/body/main/div/div/div[1]/div[1]/div/div[3]/textarea").send_keys(Keys.RETURN)
        sleep(message_time)


if __name__ == '__main__':
    main()
