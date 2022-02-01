from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


driver = webdriver.Firefox(executable_path="./drivers/geckodriver")

driver.get("https://jerseysportszone.com/vote-now-for-jszs-week-4-game-balls/")

try:
    for i in range(5):
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "PDI_answer50648026"))
                )
        element.click()

        sleep(0.25)

        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "pd-vote-button11031741"))
                )
        element.click()

        print(f"I voted for Lia {i} times!")

        sleep(0.25)

        driver.refresh()

except:
    driver.quit()

# sleep(5)

driver.quit()
