from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option('detach', True)
driver = webdriver.Edge(options=edge_options)
 
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")
upgrades_id = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment"]
 
main_timer = time.time() + 60*5
timeout = time.time() + 5
add_time_factor = 0.2
 
while time.time() < main_timer:
    cookie.click()
    if time.time() > timeout:
        print(f"\nTimeout!\n\n")
 
        for n in range(-1, -6, -1):
            try:
                element2 = driver.find_element(By.ID, upgrades_id[n])
                element2.click()
                print(f"Try block passed with: {element2.text}\n")
                add_time_factor += 0.1 + abs(n*0.03)
            except NoSuchElementException:
                print(f"{NoSuchElementException} :: index {n}")
            finally:
                continue
 
        timeout = time.time() + 5 + add_time_factor
 
cookies_cps = driver.find_element(By.ID, 'cps').text
print(f"\n***\nCookies CPS: {cookies_cps}\n\n***")
 
driver.quit()
