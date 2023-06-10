import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    # Open LinkedIn
    driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

    # Wait until the login form is visible
    login_form = WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.ID, 'username')))

    # Enter your LinkedIn credentials
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    # Submit the login form
    password_input.send_keys(Keys.ENTER)


def viewProfile(driver, url):
    driver.get(url)

def sendConnection(driver, note):
    try:
        profile_page_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='artdeco-button__text'][normalize-space()='Connect'])[2]")))
        connect_button = driver.find_element(By.XPATH, "(//span[@class='artdeco-button__text'][normalize-space()='Connect'])[2]")
        connect_button.click()
    except:
        more_button_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'More')]")))
        more_button = driver.find_element(By.XPATH, "//span[contains(text(),'More')]")
        more_button.click()
        connect_button_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='display-flex t-normal flex-1'][normalize-space()='Connect']")))
        connect_button = driver.find_element(By.XPATH, "//span[@class='display-flex t-normal flex-1'][normalize-space()='Connect']")
        connect_button.click()

    connection_modal_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Add a note'])[1]")))
    add_note_button = driver.find_element(By.XPATH, "(//span[normalize-space()='Add a note'])[1]")
    add_note_button.click()

    connection_text_area_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id=\'custom-message\']')))
    connection_text_area = driver.find_element(By.XPATH, '//textarea[@id=\'custom-message\']')
    connection_text_area.send_keys(connection_note)

    connection_text_area_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//textarea[@id=\'custom-message\']')))
    connection_text_area = driver.find_element(By.XPATH, '//textarea[@id=\'custom-message\']')
    connection_text_area.send_keys(connection_note)

    send_note_button_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Send'])[1]")))
    send_note_button = driver.find_element(By.XPATH, "(//span[normalize-space()='Send'])[1]")
    send_note_button.click()


if __name__ == '__main__':
    # Set the path to your Chrome driver executable
    chrome_driver_path = '/path/to/chromedriver'

    # Set your LinkedIn credentials
    username = os.environ['linkedinUsername']
    password = os.environ['linkedinPassword']
    print(username, password)
    connection_note = """Hello! \nI built a tool to decrease the time engineering teams spend creating and updating automated tests by 50%. Does your team face any challenges with creating automated test cases? If yes, would you be interested in chatting about these problems over a 15-minute phone call?"""

    # Set the options for the Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--new-tab")

    # Set additional options for macOS
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=WebRTC")

    profile_page_url = "https://www.linkedin.com/in/sandrasohn/"

    # Initialize the Chrome driver with the specified options
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    login(driver, username, password)
    viewProfile(driver, profile_page_url)
    sendConnection(driver, connection_note)
    # Keep the window open for three minutes
    time.sleep(180)

    # Close the browser window
    driver.quit()
