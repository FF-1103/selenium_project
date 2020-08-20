# -*- coding: utf-8 -*-
# 开发人员   ：Fanzhishuo
# 开发时间   ：2020-08-19  16:24
# 文件名称   ：test_user_login.PY
# 开发工具   ：PyCharm
from selenium import webdriver
from util import util
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAdminLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/admin/login')
        self.driver.maximize_window()

    def test_admin_login_username_error(self):
        username = ''
        pwd = 'admin'
        expected = '账号不能为空'

        self.driver.find_element_by_xpath('//*[@id="form"]/div[1]/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="form"]/div[2]/input').send_keys(pwd)
        captcha = util.get_code(self.driver, 'captchaImg')
        self.driver.find_element_by_xpath('//*[@id="form"]/div[3]/input').send_keys(captcha)
        self.driver.find_element_by_xpath('//*[@id="form"]/div[4]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        sleep(3)
        print(alert.text)
        assert alert.text == expected
        alert.accept()


