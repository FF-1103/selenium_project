# -*- coding: utf-8 -*-
# 开发人员   ：Fanzhishuo
# 开发时间   ：2020-08-19  16:24
# 文件名称   ：test_user_login.PY
# 开发工具   ：PyCharm
from util import util
from selenium import webdriver
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
if __name__ == '__main__':
    # case01 = TestUserRegister()
    # case01.test_register_code_error()
    # case01.test_register_ok()
    case02 = TestUserLogin()
    # case02.test_user_login_username_error()
    case02.test_user_login_ok()
