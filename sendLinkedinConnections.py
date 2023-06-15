import os
import time
import pandas as pd
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
    login_form = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'username')))

    # Enter your LinkedIn credentials
    username_input = driver.find_element(By.ID, 'username')
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys(password)

    # Submit the login form
    password_input.send_keys(Keys.ENTER)


def connectWithSecondConnection(driver, url, note, name):
    if driver.current_url != url:
        driver.get(url)

    profile_page_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='artdeco-button__text'][normalize-space()='Connect'])[2]")))
    connect_button = driver.find_element(By.XPATH, "(//span[@class='artdeco-button__text'][normalize-space()='Connect'])[2]")
    connect_button.click()

    print("found connect button for second connection")

    connection_modal_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Add a note'])[1]")))
    add_note_button = driver.find_element(By.XPATH, "(//span[normalize-space()='Add a note'])[1]")
    time.sleep(2)
    add_note_button.click()

    print("clicked addnote button for second connection")

    time.sleep(7)


    connection_text_area_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='custom-message'])[1]")))
    connection_text_area = driver.find_element(By.XPATH, "(//textarea[@id='custom-message'])[1]")
    connection_text_area.send_keys(connection_note)

    print("typed text in text area box for second connection")

    time.sleep(7)


    send_note_button_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Send'])[1]")))
    send_note_button = driver.find_element(By.XPATH, "(//span[normalize-space()='Send'])[1]")
    send_note_button.click()
    print("second connection: added name: ", name)
    return True

def connectWithThirdConnection(driver, url, note, name):
    if driver.current_url != url:
        driver.get(url)

    profile_page_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(text(),'More')])[2]")))
    more_button = driver.find_element(By.XPATH, "(//span[contains(text(),'More')])[2]")
    more_button.click()

    try:
        connect_button_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='display-flex t-normal flex-1'][normalize-space()='Connect'])[2]")))
        connect_button = driver.find_element(By.XPATH, "(//span[@class='display-flex t-normal flex-1'][normalize-space()='Connect'])[2]")
        connect_button.click()
        print("Found the connect that is in the more menu.")
    except Exception as e:
        print("Not a third connection + error message:", e)
        return False


    connection_modal_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Add a note'])[1]")))
    add_note_button = driver.find_element(By.XPATH, "(//span[normalize-space()='Add a note'])[1]")
    time.sleep(2)
    add_note_button.click()

    time.sleep(7)

    connection_text_area_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//textarea[@id='custom-message'])[1]")))
    connection_text_area = driver.find_element(By.XPATH, "(//textarea[@id='custom-message'])[1]")
    connection_text_area.send_keys(connection_note)

    time.sleep(7)

    send_note_button_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[normalize-space()='Send'])[1]")))
    send_note_button = driver.find_element(By.XPATH, "(//span[normalize-space()='Send'])[1]")
    send_note_button.click()
    print("added name: ", name)
    return True

def alreadyConnectedOrconnectionPending(driver, url, note, name):
    if driver.current_url != url:
        driver.get(url)

    try:
        loading_pending_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='artdeco-button__text'][normalize-space()='Pending'])[2]")))
        return True
    except Exception as e:
        try:
            print("connection is not pending")
            profile_page_loads = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(text(),'More')])[2]")))
            print("more button is loading")
            more_button = driver.find_element(By.XPATH, "(//span[contains(text(),'More')])[2]")
            more_button.click()
            print("clicked more button")
            loading_drop_down = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//span[@class='display-flex t-normal flex-1'][normalize-space()='Remove Connection'])[2]")))
            print("found the remove connection button")
            return True
        except Exception as e:
            print("alreadyConnectedOrPending Failed", e)
            return False
    return False


if __name__ == '__main__':
    # Set the path to your Chrome driver executable
    chrome_driver_path = '/path/to/chromedriver'

    # Set your LinkedIn credentials
    username = input("What is your linkedin username? ") #os.environ['link'] # use fake account
    password = input("What is your linkedin password? ") #os.environ['use trap account'] # use fake account
    df = pd.read_csv(input("Enter the name of the CSV file you'd like to use:"))

    # Set the options for the Chrome browser
    chrome_options = Options()
    chrome_options.add_argument("--new-tab")

    # Set additional options for macOS
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=WebRTC")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    login(driver, username, password)
    time.sleep(20)


    for index, row in df.iterrows():
        print(row['First Name'], row['LinkedIn'])
        name = row['First Name']
        connection_note = f"Hello {name}! \nI built a tool to decrease the time engineering teams spend creating and updating automated tests by 50%. Does your team face any challenges with creating automated test cases? If yes, would you be interested in chatting about these problems over a 15-minute phone call?"

        driver.get(row['LinkedIn'])
        # Initialize the Chrome driver with the specified options
        if not alreadyConnectedOrconnectionPending(
            driver,
            row['LinkedIn'],
            connection_note,
            name
        ):
            print("I am not connected with this person or have a pending request")
            if connectWithThirdConnection(
                    driver,
                    row['LinkedIn'],
                    connection_note,
                    name
                ):
                    pass
            else:
                connectWithSecondConnection(driver, row['LinkedIn'], connection_note, name)
        else:
            print("I am connected with this person or have a pending requests")
        # Keep the window open for three minutes
        time.sleep(7)

    # Close the browser window
    driver.quit()
