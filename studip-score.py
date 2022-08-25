import pathlib
import time

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from lorem_text import lorem
from time import sleep

from credentials import users, log_time
from tools.utils import login, get_score


def main():
    pathlib.Path("./logs").mkdir(exist_ok=True)
    options = FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options, executable_path="./geckodriver")
    # driver = webdriver.Firefox(options=options)

    login(driver)
    while True:
        curr_time = int(time.time())
        for user in users:
            score = get_score(driver, user)
            if score:
                log_file = open(f"logs/{user}.log", "a")
                log_file.write(f"{score} {curr_time}\n")
                log_file.flush()
                log_file.close()
                print(f"{user}: Got score")
            else:
                print(f"{user}: Score not public")
        sleep(log_time)


if __name__ == '__main__':
    main()
