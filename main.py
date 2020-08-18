from testcases import testcase1
from util import util
from selenium import webdriver
if __name__ == '__main__':

    # testcase1.test2()
    # print(util.gen_random_str())
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/jpress/user/register')
    driver.maximize_window()

    util.get_code(driver, 'captchaimg')
