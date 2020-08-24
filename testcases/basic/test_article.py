# -*- coding: utf-8 -*-
# 开发人员   ：Fanzhishuo
# 开发时间   ：2020-08-19  16:24 
# 文件名称   ：test_user_login.PY
# 开发工具   ：PyCharm
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from selenium.webdriver.common.by import By


class TestArticle(object):
    def __init__(self, login):
        self.login = login

    # 测试添加文章
    def test_add_ok(self):
        title = '我的文章'
        content = '我的文章内容'
        expected = '文章保存成功'

        # 点击文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击写文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        sleep(1)
        # 输入文章标题
        self.login.driver.find_element_by_xpath('//*[@id="article-title"]').send_keys(title)
        sleep(1)
        # 获得iframe
        frame1 = self.login.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')
        # 切换到iframe
        self.login.driver.switch_to.frame(frame1)
        sleep(1)
        # 输入文章内容
        self.login.driver.find_element_by_xpath('/html/body').send_keys(content)
        # 退出当前iframe
        self.login.driver.switch_to.default_content()
        # 点击发布
        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected
