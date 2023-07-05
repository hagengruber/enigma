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
        command_executor='http://selenium3:4444',
        options=options
    )
else:
    driver = webdriver.Remote(command_executor='http://localhost:4444', options=options)

driver.maximize_window()
sleep(5)


def test_select_version_enigma_m3():
    """Clicks Enigma M3 button, returns assertion that version is Enigma M3"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    sleep(0.5)

    # Assert that version "Enigma M3" has been selected
    assert driver.find_element(By.XPATH, "/html/body/div[1]/span/h1").text == "Enigma M3"


def test_reset():
    """Clicks reset button, returns assertion that enigma machine has been reset"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-c")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[1]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[5]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionE").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionH").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionL").click()

    # Selecting plugboard pair
    driver.find_element(By.ID, "checkboxT").click()
    driver.find_element(By.ID, "checkboxF").click()

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
    
    # Assert that reflector has been reset to ukw-b
    assert driver.find_element(By.XPATH, '//*[@id="reflector"]/option[1]').text == "ukw-b"
    
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

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Using default values of rotor I, II, II, reflector ukw-b, starting positions A, A, A
    # Using mouse input to click a letter on the virtual keyboard and send it to the machine
    driver.find_element(By.ID, "virtualKeyboardC").click()
    driver.find_element(By.ID, "virtualKeyboardM").click()
    driver.find_element(By.ID, "virtualKeyboardV").click()

    sleep(0.5)

    # Checking for correct ciphertext according to encryption rules
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "PDC"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_physical_input():
    """Sends physical key input, returns assertion that ciphertext appears and is correct"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Using default values of rotor I, II, II, reflector ukw-b, starting positions A, A, A
    # Setting up physical keyboard simulation and sending keys to machine
    actions = ActionChains(driver)
    actions.send_keys("T")
    actions.perform()
    actions.send_keys("A")
    actions.perform()
    actions.send_keys("W")
    actions.perform()

    sleep(0.5)

    # Checking for correct ciphertext according to encryption rules
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "ZTH"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_input_with_selected_rotors():
    """Selects rotors in enigma, returns assertion that ciphertext output is correct based on selected rotors"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                    /td[2]/select/option[6]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                    /td[3]/select/option[7]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                    /td[4]/select/option[8]").click()

    # Sending input with virtual keyboard with defaults: reflector ukw-b, starting positions A, A, A
    for _ in range(4):
        driver.find_element(By.ID, "virtualKeyboardT").click()

    # Checking for correct ciphertext according to encryption rules with different rotors
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "GNZH"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_select_reflector():
    """Selects reflector in enigma, returns assertion that ciphertext output is correct based on selected
    reflector"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-c")

    # Sending input with virtual keyboard with defaults: rotors I, II, III, starting positions A, A, A
    for _ in range(4):
        driver.find_element(By.ID, "virtualKeyboardT").click()

    # Checking for correct ciphertext according to encryption rules with different reflector
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "AGAH"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_select_starting_positions():
    """Selects starting positions in enigma, returns assertion that ciphertext output is correct based on
    selected starting positions"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionZ").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionE").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionN").click()

    # Sending input with virtual keyboard with defaults: reflector ukw-b, rotors I, II, III
    for _ in range(4):
        driver.find_element(By.ID, "virtualKeyboardT").click()

    # Checking for correct ciphertext according to encryption rules with different reflector
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "HEEA"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_history_output():
    """Clicks virtual keyboard key multiple times, returns assertion
    that 140 key-cipher pairs have been outputted"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[1]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[2]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[3]").click()

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
                                    div/div[2]/p[29]").text == "YXMBA"

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

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Checking that there data (here cipher-text output) from last session is still present
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/\
                                        div/div[2]/p[29]").text == "YXMBA"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_lamp_panel():
    """Sends input with virtual and physical keyboard, 
    returns assertion that lamp panel turns on and off"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[5]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[1]").click()

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
    assert driver.find_element(By.ID, "lampPanel_H").get_attribute("style") == \
           "background-color: yellow;"

    # Waiting for lamp to turn off
    sleep(3)

    # Assert that lamp is off in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_H").get_attribute("style") == \
           "background-color: white;"

    # Testing with physical keyboard input
    actions = ActionChains(driver)
    actions.send_keys("T")
    actions.perform()

    # Assert that lamp is on in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_V").get_attribute("style") == \
           "background-color: yellow;"

    # Waiting for lamp to turn off
    sleep(3)

    # Assert that lamp is off in corresponding lamp panel
    assert driver.find_element(By.ID, "lampPanel_V").get_attribute("style") == \
           "background-color: white;"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_plugboard_pair_selection():
    """Selects plugboard pair, returns assertion that plugboard pair has been selected"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[5]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[2]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionC").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionI").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionL").click()

    # Selecting plugboard pair
    driver.find_element(By.ID, "checkboxA").click()
    driver.find_element(By.ID, "checkboxB").click()

    # Assert that plugboard pair is selected
    assert driver.find_element(By.ID, "checkboxA").get_attribute("style") == \
           "background-color: black;"
    assert driver.find_element(By.ID, "checkboxB").get_attribute("style") == \
           "background-color: black;"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_input_with_plugboard():
    """Selects plugboard pair and sends input, 
    returns assertion that ciphertext appears and is correct"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[5]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[2]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionC").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionI").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionL").click()

    # Selecting plugboard pair
    driver.find_element(By.ID, "checkboxT").click()
    driver.find_element(By.ID, "checkboxF").click()

    # Clicking on letter in plugboard pair on the virtual keyboard
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()

    sleep(0.5)

    # Checking for correct ciphertext according to encryption rules
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]\
                               /div/div[2]/p[1]").text == "CSYN"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()

    sleep(0.5)


def test_plugboard_pair_deselection():
    """Selects plugboard pair and deselects it,
    returns assertion that plugboard pair does 
    not exist"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[5]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[2]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionC").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionI").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionL").click()

    # Selecting plugboard pair
    driver.find_element(By.ID, "checkboxT").click()
    driver.find_element(By.ID, "checkboxF").click()

    # Deselecting plugboard pair
    driver.find_element(By.ID, "checkboxT").click()

    # Assert that plugboard pair is not selected
    assert driver.find_element(By.ID, "checkboxT").get_attribute("style") == ""
    assert driver.find_element(By.ID, "checkboxF").get_attribute("style") == \
           "background-color: rgb(255, 255, 255);"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_plugboard_selection_deselection():
    """Selects, deselects and selects new plugboard pair and sends input,
    returns assertion that ciphertext appears and is correct"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[1]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                            /td[4]/select/option[5]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionT").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionC").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionD").click()

    #  Selecting plugboard pair
    driver.find_element(By.ID, "checkboxT").click()
    driver.find_element(By.ID, "checkboxZ").click()

    # Deselecting chosen plugboard pair
    driver.find_element(By.ID, "checkboxT").click()

    # Selecting new plugboard pair
    driver.find_element(By.ID, "checkboxT").click()
    driver.find_element(By.ID, "checkboxU").click()

    # Clicking on letters in plugboard pair on the virtual keyboard
    driver.find_element(By.ID, "virtualKeyboardT").click()
    driver.find_element(By.ID, "virtualKeyboardU").click()
    driver.find_element(By.ID, "virtualKeyboardT").click()

    sleep(0.5)

    # Checking for correct ciphertext according to encryption rules
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/p[1]").text == "DFQ"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_plugboard_pair_with_single_cord():
    """Selects pair and single cord in plugboard, returns 
    assertion that     single cord has no effect on ciphertext 
    and that ciphertext outputs correctly"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[1]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[5]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionD").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionG").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionM").click()

    # Selecting pair and single cord
    driver.find_element(By.ID, "checkboxE").click()
    driver.find_element(By.ID, "checkboxF").click()
    driver.find_element(By.ID, "checkboxG").click()

    # Clicking virtual keyboard keys selected in the plugboard
    driver.find_element(By.ID, "virtualKeyboardE").click()
    driver.find_element(By.ID, "virtualKeyboardF").click()
    driver.find_element(By.ID, "virtualKeyboardG").click()

    # Checking for correct ciphertext output
    assert driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]\
                               /p[1]").text == "QBO"

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_plugboard_limit():
    """Selects limit of 10 plugboard pairs and attempts to go over limit,
    returns assertion that limit has been reached"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Selecting reflector
    select_reflector = Select(driver.find_element(By.ID, "reflector"))
    select_reflector.select_by_value("ukw-b")

    # Selecting rotors 1, 2 and 3
    select_rotor_1 = driver.find_element(By.ID, "rotor1Select")
    select_rotor_1.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[2]/select/option[4]").click()

    sleep(1)

    select_rotor_2 = driver.find_element(By.ID, "rotor2Select")
    select_rotor_2.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[3]/select/option[1]").click()

    sleep(1)

    select_rotor_3 = driver.find_element(By.ID, "rotor3Select")
    select_rotor_3.find_element(By.XPATH, "/html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]\
                                /td[4]/select/option[5]").click()

    # Selecting starting / initial positions of rotors 1, 2 and 3
    Select(driver.find_element(By.ID, "rotor1InitialPosition"))
    driver.find_element(By.ID, "rotor1InitialPositionOptionC").click()

    Select(driver.find_element(By.ID, "rotor2InitialPosition"))
    driver.find_element(By.ID, "rotor2InitialPositionOptionI").click()

    Select(driver.find_element(By.ID, "rotor3InitialPosition"))
    driver.find_element(By.ID, "rotor3InitialPositionOptionM").click()

    # Selecting 1st Plugboard Pair
    driver.find_element(By.ID, "checkboxA").click()
    driver.find_element(By.ID, "checkboxB").click()

    # Selecting 2nd Plugboard Pair
    driver.find_element(By.ID, "checkboxC").click()
    driver.find_element(By.ID, "checkboxD").click()

    # Selecting 3rd Plugboard Pair
    driver.find_element(By.ID, "checkboxE").click()
    driver.find_element(By.ID, "checkboxF").click()

    # Selecting 4th Plugboard Pair
    driver.find_element(By.ID, "checkboxG").click()
    driver.find_element(By.ID, "checkboxH").click()

    # Selecting 5th Plugboard Pair
    driver.find_element(By.ID, "checkboxI").click()
    driver.find_element(By.ID, "checkboxJ").click()

    # Selecting 6th Plugboard Pair
    driver.find_element(By.ID, "checkboxK").click()
    driver.find_element(By.ID, "checkboxL").click()

    # Selecting 7th Plugboard Pair
    driver.find_element(By.ID, "checkboxM").click()
    driver.find_element(By.ID, "checkboxN").click()

    # Selecting 8th Plugboard Pair
    driver.find_element(By.ID, "checkboxO").click()
    driver.find_element(By.ID, "checkboxP").click()

    # Selecting 9th Plugboard Pair
    driver.find_element(By.ID, "checkboxQ").click()
    driver.find_element(By.ID, "checkboxR").click()

    # Selecting 10th Plugboard Pair
    driver.find_element(By.ID, "checkboxS").click()
    driver.find_element(By.ID, "checkboxT").click()

    # Attempt to go over set limit of 10 pairs
    driver.find_element(By.ID, "checkboxU").click()
    driver.find_element(By.ID, "checkboxV").click()

    sleep(0.5)

    # Assert that 10th and final plugboard pair is selected
    assert driver.find_element(By.ID, "checkboxS").get_attribute("style") \
           == "background-color: black;"
    assert driver.find_element(By.ID, "checkboxT").get_attribute("style") \
           == "background-color: black;"

    # Assert that attempt for 11th plugboard pair couldn't be selected / doesn't exist
    assert driver.find_element(By.ID, "checkboxU").get_attribute("style") == ""
    assert driver.find_element(By.ID, "checkboxV").get_attribute("style") == ""

    # Resetting enigma
    driver.find_element(By.XPATH, "//*[@id='button']").click()


def test_for_invalid_input():
    """Sends invalid input to enigma, returns assertion that alert for invalid input appears"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

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


def test_for_valid_amount_of_rotors():
    """Starts enigma, returns assertion that correct amount of rotors is selected"""

    driver.get("http://enigma:8080")

    driver.implicitly_wait(3)

    # Select Enigma M3
    driver.find_element(By.XPATH, "/html/body/div[1]/nav/ul/li[3]/a").click()

    # Asserts that all rotor positions are filled
    assert driver.find_element(By.XPATH, '//*[@id="rotor1Select"]/option[1]').text == "I"
    assert driver.find_element(By.XPATH, '//*[@id="rotor2Select"]/option[2]').text == "II"
    assert driver.find_element(By.XPATH, '//*[@id="rotor3Select"]/option[3]').text == "III"

    driver.quit()
