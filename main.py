# -*- coding: utf-8 -*-
# 开发人员   ：Fanzhishuo
# 开发时间   ：2020-08-19  16:24
# 文件名称   ：test_user_login.PY
# 开发工具   ：PyCharm
from util import util
from selenium import webdriver
from testcases.basic.test_user_register import TestUserRegister
from testcases.basic.test_user_login import TestUserLogin
from testcases.basic.test_admin_logiin import TestAdminLogin
from testcases.basic.test_category import TestCategory
from testcases.basic.test_article import TestArticle
if __name__ == '__main__':
    # case01 = TestUserRegister()
    # case01.test_register_code_error()
    # case01.test_register_ok()
    # case02 = TestUserLogin()
    # case02.test_user_login_username_error()
    # case02.test_user_login_ok()
    login = TestAdminLogin()
    print(login)
    # case03.test_admin_login_username_error()
    login.test_admin_login_ok()
    # case04 = TestCategory(login)
    # case04.test_add_category_error()
    # case04.test_add_category_ok()
    case05 = TestArticle(login)
    case05.test_add_ok()
