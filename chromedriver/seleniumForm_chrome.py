from selenium import webdriver
import time
from vk_auth_data import vk_phone_num, vk_password


options = webdriver.ChromeOptions()

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0")

driver = webdriver.Chrome(executable_path=r"D:\Dev\PypySelenium\chromedriver\chromedriver.exe",
                          options=options)

try:
    driver.get('https://vk.com/')
    time.sleep(2)

    email_input = driver.find_element_by_id('index_email')
    email_input.clear()
    email_input.send_keys(vk_phone_num)
    time.sleep(2)

    password_input = driver.find_element_by_id('index_pass')
    password_input.clear()
    password_input.send_keys(vk_password)
    time.sleep(3)

    login_button = driver.find_element_by_id('index_login_button').click()
    time.sleep(2)

    news_link = driver.find_element_by_id('l_nwsf').click()
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()