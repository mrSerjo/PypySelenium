from selenium import webdriver
import time
import random
from fake_useragent import UserAgent


user_agent_list = [
    'hello_world',
    'Chrome/18.0.1025.133 Mobile Safari/535.19',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19B74'
    ' [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/15.1;FBSS/3;FBID/phone;FBLC/fr_FR;FBOP/5]',
]

useragent = UserAgent()

url = "https://vk.com/"

options = webdriver.ChromeOptions()

# Для примера случайный выбор из списка user_agent_list
#options.add_argument(f"user-agent={random.choice(user_agent_list)}")

#Для примера user-agent из библиотеки fake-useragent
options.add_argument(f'user-agent={useragent.random}')

driver = webdriver.Chrome(executable_path=r"D:\Dev\PypySelenium\chromedriver\chromedriver.exe",
                          options=options)

try:
    driver.get(url="https://www.whatsmyua.info/")
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()