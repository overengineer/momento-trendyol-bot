from selenium import webdriver
import time, os.path
from getpass import getpass

USERNAME = input("Username:")
PASSWORD = getpass("Password:")
COMPANY = "siemens"
EXE_PATH = os.path.expanduser(r"~/Downloads/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(EXE_PATH)
base_url = f"https://portal.momento.com.tr/{COMPANY}/"
driver.get(base_url)
time.sleep(0.5)

user=driver.find_element_by_id("EmailOrUserNameOrPhone")
user.send_keys(USERNAME)
passw=driver.find_element_by_id("Password")
passw.send_keys(PASSWORD)
login=driver.find_element_by_css_selector('button[type="submit"]')
time.sleep(0.5)
login.click()
time.sleep(2)

trendyol_url = f"https://portal.momento.com.tr/{COMPANY}/trendyol-hediye-kodu---anlik-kod_762"

while True:
    driver.get(trendyol_url)
    time.sleep(2)
    driver.execute_script("""
        for (var i=0; i<10; i++)
        {
            IncreasePrice()
        }
    """)
    ok=driver.find_element_by_css_selector('button[class*="swal-button--catch"]')
    ok.click()
    time.sleep(0.5)
    ok=driver.find_element_by_css_selector('button[class*="swal-button--catch"]')
    ok.click()
    time.sleep(0.5)


