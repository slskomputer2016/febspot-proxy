import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Membuka browser layar penuh
# options.add_argument("--headless")      # Aktifkan ini jika ingin berjalan di latar belakang

# Inisialisasi driver otomatis dengan webdriver_manager
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
service = Service() 
driver = webdriver.Chrome(service=service)


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
        driver.get("https://www.sslunblocker.com/")
        wait = WebDriverWait(driver,1)
        #email_field = wait.until(EC.presence_of_element_located((By.NAME, "get")))
        email_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "url-input")))

        email_field.send_keys(link)
        time.sleep(2)
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        time.sleep(3)
        btn_play = driver.find_element(By.CLASS_NAME, "fs-player")
        btn_play.click()
        #button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CLASS_NAME, "fs-player")))
        #button.click()
        time.sleep(19)
        print("Bot end !!!")
        print("")
        # btn2 = wait.until(EC.presence_of_element_located((By.ID, "server-options")))
        # btn2.click()
        time.sleep(1)

    except Exception as e:
        print(f"Terjadi kesalahan saat login: {e}")
    #finally:
        #time.sleep(10)
        #driver.quit()
