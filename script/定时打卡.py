#! E:/Anaconda/python.exe

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
import pandas as pd

# 读取用户和表单信息
table = pd.read_table('C:/Users/ASUS/Desktop/表格信息.txt',header = None, sep = "|")
info = table[1]
print (info)
waitTime=100 # 如果网络状况差，需要设置更长的等待时间上限，确保网页加载

# 设置后台运行，隐藏浏览器
option = webdriver.ChromeOptions() 
option.add_argument('headless')
browser = webdriver.Chrome(chrome_options = option)


# 登入信息平台
browser.get('https://thos.tsinghua.edu.cn/fp/view?m=fp')
try: 
    browser.find_element_by_id('i_user').send_keys(info[0])
    browser.find_element_by_id('i_pass').send_keys(info[1])
    browser.find_element_by_class_name('btn-block').click()

    WebDriverWait(browser, waitTime).until (
        EC.presence_of_element_located((By.ID,"formHome_serve_content"))
    )
    browser.find_element_by_xpath('//span[@title="学生健康及出行情况报告"]').click()


    WebDriverWait(browser, waitTime).until (
        EC.presence_of_element_located((By.ID, 'formIframe'))
    )
    browser.switch_to.frame('formIframe')
    WebDriverWait(browser, waitTime).until (
        EC.presence_of_element_located((By.ID, 'GN'))
    )
    

    # 设置表单内容，这里至少需要模拟填写所在省市的部分内容
    browser.find_element_by_xpath('//*[@id="GN"]/div[2]/div[2]/button').click()
    browser.find_element_by_xpath('//*[@id="GN"]/div[2]/div[2]/div/ul/li[3]/a/span').click()
    browser.find_element_by_xpath('//*[@id="GN"]/div[2]/div[3]/button').click()
    browser.find_element_by_xpath('//*[@id="GN"]/div[2]/div[3]/div/ul/li[3]/a/span').click()

    # 提交表单
    browser.switch_to.default_content()
    browser.find_element_by_class_name('btn-block').click()
    

finally:
    # 退出浏览器
    browser.quit()
    print ('Success!')


