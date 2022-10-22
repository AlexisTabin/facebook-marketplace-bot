from time import sleep
from selenium.webdriver.common.by import By

def login(driver):
    usr='alexis29611@gmail.com'
    pwd='HEHEHSHEEH'

    username_box = driver.find_element(By.ID, 'email')
    print(username_box)
    username_box.send_keys(usr)
    print ("Email Id entered")
    sleep(1)
    
    password_box = driver.find_element(By.ID, 'pass')
    password_box.send_keys(pwd)
    print ("Password entered")
    sleep(5)

    login_box = driver.find_element(By.NAME, 'login')
    login_box.click()
    
    print ("Login")