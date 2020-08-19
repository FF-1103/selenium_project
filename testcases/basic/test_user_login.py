# -*- coding: utf-8 -*-
# 开发人员   ：Fanzhishuo
# 开发时间   ：2020-08-19  16:24 
# 文件名称   ：test_user_login.PY
# 开发工具   ：PyCharm
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from util import util


class TestUserLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/login')
        self.driver.maximize_window()

    # 测试用户登录失败，用户名错误
    def test_user_login_username_error(self):
        # 用户名为空
        username = ''
        pwd = '123456'
        expected = '账号不能为空'

        # 输入用户名
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/button').click()

        # 等待alert
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        sleep(5)
        assert alert.text == expected
        alert.accept()

    # 测试用户登录成功
    def test_user_login_ok(self):
        # 用户名为空
        username = 'admin'
        pwd = 'admin'
        expected = '用户中心'

        # 输入用户名
        self.driver.find_element_by_name('user').send_keys(username)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 点击登录
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[3]/div/button').click()

        WebDriverWait(self.driver, 5).until(EC.title_is(expected))

        assert self.driver.title == expected

