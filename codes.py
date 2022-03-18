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

orders_url = f"https://portal.momento.com.tr/{COMPANY}/orders"

driver.get(orders_url)
time.sleep(2)
order_ids = driver.execute_script("""
    var elements = document.querySelectorAll('tr[class="fc1"]')
    var order_ids=[]
    for (var i=0; i<elements.length; i++)
    {
        if (elements[i].innerText.includes("Trendyol"))
        {
            order_ids.push(elements[i].getAttribute("data-id"))
        }
    }
    return order_ids
""")

with open("codes.txt", "w") as f:
    for order_id in order_ids:
        order_url = f"https://portal.momento.com.tr/{COMPANY}/orderdetails/{order_id}"
        driver.get(order_url)
        time.sleep(0.5)
        order = driver.find_element_by_css_selector('div[class*="fc3 bold"]')
        code = order.text.split(':')[1].strip()
        print(code, file=f)
        print(code)