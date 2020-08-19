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


class TestUserRegister(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:8080/jpress/user/register')
        self.driver.maximize_window()

    # 测试登录验证码错误
    def test_register_code_error(self):
        username = 'test001'
        email = 'test001@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = '666'
        expected = '验证码不正确'
        # 输入用户名
        self.driver.find_element_by_name('username').send_keys(username)
        # 输入email
        self.driver.find_element_by_name('email').send_keys(email)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 输入验证码
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册按键
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/button').click()
        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python 的断言
        assert alert.text == expected
        alert.accept()

        sleep(5)

    # 测试成功
    def test_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        captcha = ''
        expected = '注册成功，点击确定进行登录。'
        # 输入用户名
        self.driver.find_element_by_name('username').send_keys(username)
        # 输入email
        self.driver.find_element_by_name('email').send_keys(email)
        # 输入密码
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')
        # 输入验证码
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册按键
        self.driver.find_element_by_xpath('/html/body/div/div/div/form/div[6]/div/button').click()
        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python 的断言
        assert alert.text == expected
        alert.accept()

        sleep(5)