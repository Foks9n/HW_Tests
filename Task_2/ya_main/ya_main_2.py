import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

login = '' #Введите свой логин
password = ''  #Введите свой пароль

def login_yandex_from_chrome(login, password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    driver.get('https://passport.yandex.ru/auth/')

    login_input = driver.find_element(By.ID, 'passp-field-login')
    login_input.send_keys(login)
    login_input.send_keys(Keys.ENTER)
    WebDriverWait(driver, 1)

    password_input = driver.find_element(By.ID, 'passp-field-passwd')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    success_Auth = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, 'Yandex Pay')))

    return True

if __name__ == '__main__':
    login_yandex_from_chrome(login, password)