import os
import string
import time
import random
from copyreg import pickle

from PIL import Image
from lib.ShowapiRequest import ShowapiRequest


# 获取验证码图片
def get_code(driver, id):
    # 获取当前时间
    t = time.time()
    '''
    os.path.dirname(__file__) 获得当前文件所在文件夹的路径D:/PythonWorkSpace/my_selenium_project/util
    os.path.dirname(os.path.dirname(__file__)) 获得当前文件所在文件夹上一层文件夹的路径D:/PythonWorkSpace/my_selenium_project
    path = os.path.dirname(os.path.dirname(__file__)) + '/screenshots' 获得获得当前文件所在文件夹上一层文件夹的路径后拼接路径
    /screenshots 最终path路径为D:/PythonWorkSpace/my_selenium_project/screenshots
    '''
    path = os.path.dirname(os.path.dirname(__file__)) + '\\screenshots'
    # 图片路径和名称 D:/PythonWorkSpace/my_selenium_project/screenshots  当前时间.png
    picture_name1 = path + '\\' + str(t) + '.png'
    # 截图保存
    driver.save_screenshot(picture_name1)
    # 根据传入ID获取到该ID的元素位置
    ce = driver.find_element_by_id(id)
    # 获取距离左边坐标值
    left = ce.location['x']
    # 获取距离顶部坐标值
    top = ce.location['y']
    # 右边距离 = 元素的宽度 + 左边距离
    right = ce.size['width'] + left
    # 高度距离 = 元素高度 + 距顶距离
    height = ce.size['height'] + top
    # 打开保存的截图
    im = Image.open(picture_name1)
    # 根据座标切割图片
    img = im.crop((left, top, right, height))
    # 图片路径和名称 D:/PythonWorkSpace/my_selenium_project/screenshots  当前时间.png
    picture_name2 = path + '\\' + str(t) + '.png'
    # 保存图片
    img.save(picture_name2)
    # 调用第三方API自动识别图片内信息
    r = ShowapiRequest("http://route.showapi.com/184-4", "332647", "b65f40472bd142c0ba3e18f5df149b91")
    r.addFilePara("image", picture_name2)
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    res = r.post()
    code = res.json()['showapi_res_body']['Result']
    print(code)
    return code


# 生成随机字符串
def gen_random_str():
    rand_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    return rand_str


# 保存cookie
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        cookies = driver.get_cookies()
        print(cookies)
        pickle.dump(cookies, filehandler)


# 加载cookie
def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
