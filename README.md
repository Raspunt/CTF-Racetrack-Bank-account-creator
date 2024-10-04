This code is for a CTF challenge. Here is the URL:[ Racetrack Bank](https://tryhackme.com/r/room/racetrackbank).

This is the first stage of the CTF, which involves creating a user that provides giving gold to our dear account, "boxman"

browser.py is the slow version, but it uses Selenium. Selenium is cool!<br />
api.py uses the requests library, making it a Selenium-free version with over 100 threads!

To use this code replace for your ip, just enter:
```
pip install requests
python3 api.py
```
Or for Selenium:
```
pip install selenium
python3 browser.py
```
