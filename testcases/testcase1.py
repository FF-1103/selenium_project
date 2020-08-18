from selenium import webdriver
from time import sleep
import pyautogui


def test1():
    print('test1')


def test2():
    driver = webdriver.Chrome()
    driver.get('http://www.jpress.io/user/register')
    driver.maximize_window()
    sleep(2)
    elem = driver.find_element_by_id('agree')
    print(elem.rect)
    rect = elem.rect
    pyautogui.click(rect['x'] + 10, rect['y'] + 130)
    sleep(5)
