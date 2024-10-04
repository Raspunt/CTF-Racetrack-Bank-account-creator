import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

from generator import *

host = "http://enter_your_ip"

login_page = f"{host}/login.html"
logout_page = f"{host}/api/logout"
create_page = f"{host}/create.html"
giving_page = f"{host}/giving.html"

main_user = "box"

def login_in_site(driver, username, password):
    driver.get(login_page)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "uname"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd"))
    )

    username_field.clear()
    password_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

def create_user(driver, username, password):
    driver.get(create_page)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "uname"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd"))
    )
    password2_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "passwd2"))
    )

    username_field.clear()
    password_field.clear()
    password2_field.clear()

    username_field.send_keys(username)
    password_field.send_keys(password)
    password2_field.send_keys(password)

    password_field.send_keys(Keys.RETURN)

def giving_money(driver):
    driver.get(giving_page)

    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "uname"))
    )
    number_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "amnt"))
    )

    username_field.clear()
    number_field.clear()

    username_field.send_keys(main_user)
    number_field.send_keys(1)

    number_field.send_keys(Keys.RETURN)

def logout_account(driver):
    driver.get(logout_page)

    WebDriverWait(driver, 10).until(
        EC.url_to_be(login_page)
    )





def giving_loop(driver, thread_number):
    fail_attempt = 0
    success_attempt = 0

    while True:
        user = gen_unic_username()
        password = gen_unic_password()

        try:
            create_user(driver, user, password)
            login_in_site(driver, user, password)
            giving_money(driver)
            logout_account(driver)

            success_attempt += 1
            print(f"Thread {thread_number}, Attempt {success_attempt} succeeded")

        except Exception as e:
            fail_attempt += 1
            print(f"Thread {thread_number}, Attempt {fail_attempt} failed")
            continue


def start_browser(thread_number):
    firefox_options = Options()
    firefox_options.headless = True 

    driver = webdriver.Firefox(options=firefox_options)

    create_user(driver, main_user, "qaqsqdqe")
    giving_loop(driver, thread_number)



if __name__ == "__main__":
    num_threads = 10

    for i in range(1,num_threads):
        browser_thread = threading.Thread(target=start_browser, args=(i,))
        browser_thread.start()
    
