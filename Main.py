from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

Headless = True
EMAIL = ""
PASSWORD = ""

def sleep(seconds):
    time.sleep(seconds)

def LoadDriver():
    options = webdriver.ChromeOptions()
    if Headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get("https://assessment.peardeck.com/login")
    return driver

def CloseDriver(driver):
    driver.quit()

def ClickElement(by, query, time=0):
    element = driver.find_element(by, query)
    element.click()
    if time > 0:
        sleep(time)

def TypeInElement(by, query, text, enter=False, time=0):
    element = driver.find_element(by, query)
    element.send_keys(text)
    if enter:
        element.send_keys("\n")
    if time > 0:
        sleep(time)

driver = LoadDriver()
wait = WebDriverWait(driver, 30)

try:
    email_input = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "email")))
    pass_input  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "password")))

    email_input.send_keys(EMAIL)
    pass_input.send_keys(PASSWORD)
    pass_input.send_keys("\n")

    wait.until(EC.url_contains("assessment.peardeck.com"))
    cards = wait.until(
        EC.presence_of_all_elements_located((
        By.CSS_SELECTOR,
        ".ant-row.AssignmentCard__CardWrapper-sc-14ztw5t-0.sFUpT"
    ))) 

    print(len(cards), "assignments found.")
finally:
    driver.quit()
