from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    ...

    # Отправляем заполненную форму
    input_first_element = browser.find_element(By.CSS_SELECTOR, ".first[required]")
    input_first_element.send_keys("Ivan")
    input_last_element = browser.find_element(By.CSS_SELECTOR, ".second[required]")
    input_last_element.send_keys("Ivanov")
    input_email_element = browser.find_element(By.CSS_SELECTOR, ".third[required]")
    input_email_element.send_keys("Ivanov@mail.ru")
    button_element = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_element.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()