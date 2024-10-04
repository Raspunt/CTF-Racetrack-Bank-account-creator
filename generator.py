import random

def gen_unic_password(length=8) -> str:
    password_wordlist = "qwertyuiopasdfghjklzxcvbnm"
    password_string = "".join(random.choice(password_wordlist) for _ in range(length))
    return password_string

def gen_unic_username(length=8) -> str:
    username_wordlist = "abcdefghijklmnopqrstuvwxyz0123456789"
    username_string = "".join(random.choice(username_wordlist) for _ in range(length))
    return username_string