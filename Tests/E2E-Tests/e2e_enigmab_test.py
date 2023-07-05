from time import sleep
import os
from selenium.webdriver.common.action_chains import ActionChains  # Simulate physical keyboard inputs
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select  # For drop-down menu
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Setup for test simulation with Selenium
options = webdriver.FirefoxOptions()

if "CI" in os.environ.keys():
    driver = webdriver.Remote(
        command_executor='http://selenium2:4444',
        options=options
    )
else:
    driver = webdriver.Remote(command_executor='http://localhost:4444', options=options)

driver.maximize_window()
sleep(5)


def test_select_version_enigma_b():
    """Clicks Enigma B button, returns assertion that version is Enigma MB"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)
    
    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    sleep(0.5)

    # Assert that version "Enigma B" has been selected
    assert driver.find_element(By.XPATH, "/html/body/div[1]/span/h1").text == "Enigma B"


def test_reset():
    """Clicks reset button, returns assertion that enigma machine has been reset"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Using reflector ukw-a (only one in version B) and rotors I, II, II 
    # No selection necessary because this is the default

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionE").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionH").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionL").click()

    # Clicking on letter on the virtual keyboard
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()

    sleep(0.5)

    # Assert that previous ciphertext has been deleted
    assert driver.find_element(By.XPATH, "//*[@id='ciphertext']/p[1]").text == ""
    
    # Assert that reflector has been reset to ukw-a
    assert driver.find_element(By.XPATH, '//*[@id="reflector"]').text == "ukw-a"
    
    # Assert that rotors have been reset to position 1, 2 and 3
    assert driver.find_element(By.XPATH, '//*[@id="rotor1Select"]/option[1]').text == "I"
    assert driver.find_element(By.XPATH, '//*[@id="rotor2Select"]/option[2]').text == "II"
    assert driver.find_element(By.XPATH, '//*[@id="rotor3Select"]/option[3]').text == "III"

    # Assert that starting position has been reset to position A, A, A
    assert driver.find_element(By.XPATH, '//*[@id="rotor1InitialPositionOptionA"]').text == "A"
    assert driver.find_element(By.XPATH, '//*[@id="rotor2InitialPositionOptionA"]').text == "A"
    assert driver.find_element(By.XPATH, '//*[@id="rotor3InitialPositionOptionA"]').text == "A"


def test_input():
    """Clicks on virtual keyboard keys, returns assertion that ciphertext appears and is correct"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Using default values of rotor I, II, II, reflector ukw-a, starting positions A, A, A
    # Using mouse input to click a letter on the virtual keyboard and send it to the machine
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()

    sleep(0.5)

    # Checking for correct ciphertext according to encryption rules
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "VYEV"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_physical_input():
    """Sends physical key input, returns assertion that ciphertext appears and is correct"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Using default values of rotor I, II, II, reflector ukw-a, starting positions A, A, A
    # Setting up physical keyboard simulation and sending keys to machine
    actions = ActionChains(driver)
    actions.send_keys("T")
    actions.perform()
    actions.send_keys("A")
    actions.perform()
    actions.send_keys("F")
    actions.perform()

    sleep(0.5)

    # Checking for correct ciphertext according to encryption rules
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "VÅJ"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_select_starting_positions():
    """Selects starting positions in enigma, returns assertion that ciphertext output is correct based on
    selected starting positions"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionH").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionE").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionN").click()

    # Sending input with virtual keyboard with defaults: reflector ukw-a, rotors I, II, III
    for _ in range(4):
        driver.find_element(By.ID, "virtualKeyboardT").click()

    # Checking for correct ciphertext according to encryption rules with different reflector
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "LÅMR"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_history_output():
    """Clicks virtual keyboard key multiple times, returns assertion
    that 140 key-cipher pairs have been outputted"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Using reflector ukw-a (only one in version B) and rotors I, II, II 
    # No selection necessary because this is the default

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionA").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionA").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionA").click()

    # Repeat input 140 times through virtual keyboard
    for _ in range(140):
        driver.find_element(By.ID, "virtualKeyboardG").click()

    # Checking that there is at least 140 key-cipher character pairs by checking the earliest line of output
    # (The earliest line with 140 inputted characters would be the 28th line)
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/\
                                div/div[2]/p[29]").text == "UUMXP"

    # No activation of reset button in order to check if data /
    # ciphertext output has been loaded into next test-session


def test_saved_state():
    """Takes previous test session data,
    returns assertion that history is 
    the same as in previous session"""

    # Assumption: test_saved_state only
    # happens AFTER a previously used
    # session, given that nothing was reset

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Checking that there data (here cipher-text output) from last session is still present
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/\
                                        div/div[2]/p[29]").text == "UUMXP"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_lamp_panel():
    """Sends input with virtual and physical keyboard, 
    returns assertion that lamp panel turns on and off"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Using reflector ukw-a (only one in version B) and rotors I, II, II 
    # No selection necassary because this is the default

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionH").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionF").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionH").click()

    # Testing with mouse input / virtual keyboard
    driver.find_element(By.ID, "virtualKeyboardT").click()

    # Assert that lamp is on in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_V").get_attribute("style") == \
           "background-color: yellow;"

    # Waiting for lamp to turn off
    sleep(3)

    # Assert that lamp is off in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_V").get_attribute("style") == \
           "background-color: white;"

    # Testing with physical keyboard input
    actions = ActionChains(driver)
    actions.send_keys("T")
    actions.perform()

    # Assert that lamp is on in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_I").get_attribute("style") == \
           "background-color: yellow;"

    # Waiting for lamp to turn off
    sleep(3)

    # Assert that lamp is off in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_I").get_attribute("style") == \
           "background-color: white;"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_for_invalid_input():
    """Sends invalid input to enigma, returns assertion that alert for invalid input appears"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma B
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[1]/a").click()

    # Simulating physical keyboard and sending physical keyboard input to machine
    actions = ActionChains(driver)
    actions.send_keys(Keys.ALT).perform()

    # Waits for alert to appear, then switches to given alert
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    invalid_input_alert = driver.switch_to.alert

    # Asserts that the correct type of alert is present
    assert invalid_input_alert.text == "Ungültige Eingabe"
    invalid_input_alert.accept()

    # Simulating physical keyboard and sending physical keyboard input to machine
    actions.send_keys(Keys.ESCAPE).perform()

    # Waits for alert to appear, then switches to given alert
    WebDriverWait(driver, 3).until(EC.alert_is_present())
    invalid_input_alert_2 = driver.switch_to.alert

    # Asserts that the correct type of alert is present
    assert invalid_input_alert_2.text == "Ungültige Eingabe"
    invalid_input_alert_2.accept()

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()

    driver.quit()