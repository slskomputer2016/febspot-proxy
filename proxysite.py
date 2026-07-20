import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")
service = Service() 
driver = webdriver.Chrome(service=service, options=options)


def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            item = [line.strip() for line in file if line.strip()]
        if not item:
            print("No item found in the file.")
            return []
        return item
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


links = load_file('./files/link-febspot.txt')
for link in links:
    #os.system('cls')
    try:
        driver.get("https://www.proxysite.com/")
        wait = WebDriverWait(driver,10)
        email_field = wait.until(EC.presence_of_element_located((By.NAME, "d")))
        email_field.send_keys(link)
        time.sleep(2)
        select_element = driver.find_element(By.ID, 'serverSelect')
        select = Select(select_element)
        select.select_by_index(0)
        #assert count_element.is_selected()
        time.sleep(1)

        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(5)
        btn_play = driver.find_element(By.CLASS_NAME, "fs-player")
        btn_play.click()
        time.sleep(22)
        print("")
        print("")
        print("")
        print("")


    except Exception as e:
        print(f"Terjadi kesalahan saat login: {e}")
    #finally:
        #time.sleep(10)
        #driver.quit()
print("---------------------------------------------------------")  
print("--- Proxysite End ---------------")  
print("---------------------------------------------------------") 