# !/usr/bin/python
# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()


# 上机实操: 在新的TAB打开连接
# 打开：https://china-testing.github.io/
# 选择"数据分析"栏目的文章
# 按住"Ctrl+TAB"选择"python"栏目的文章
# 切换到新的标签"python"
# 关闭新的标签"python"
# 关闭浏览器
def page_switching():
    driver.get("https://china-testing.github.io/")
    time.sleep(1)
    driver.find_element_by_link_text("数据分析").click()
    time.sleep(2)
    element = driver.find_element_by_link_text("python")
    ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(
        Keys.CONTROL).perform()
    time.sleep(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.close()
    time.sleep(2)


# 上机实操: 基于坐标移动
# 打开：http://guidebook.seleniumacademy.com/Selectable.html
# 输出数字1的位置和大小
# 输出数字6的位置和大小
# 利用数字1的位置和大小移动到数字6
def position_movement():
    driver.get("http://guidebook.seleniumacademy.com/Selectable.html")
    driver.implicitly_wait(30)
    driver.maximize_window()
    one = driver.find_element_by_name('one')
    print(one.location)
    print(one.size)
    six = driver.find_element_by_name('six')
    print(six.location)
    print(six.size)
    actions = ActionChains(driver)
    actions.move_by_offset(one.size['width'] + one.location['x'],
                           one.size['height'] + one.location['y']).click().perform()
    input('Press ENTER to close the automated browser')


# position_movement()

page_switching()

driver.quit()
