#!/usr/bin/python
# coding:utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()


class qqEmail:
    def __init__(self):
        pass

    # 启动浏览器
    def openBroswer(self):
        driver.get("https://mail.qq.com/")
        driver.maximize_window()
        time.sleep(3)

    # 输入账号密码登录
    def login(self):
        # 进入登录iframe
        driver.switch_to.frame(driver.find_element_by_id("login_frame"))
        # 输入账号
        driver.find_element_by_id("u").send_keys("357112130@qq.com")
        time.sleep(1)
        # 输入密码
        driver.find_element_by_id("p").send_keys("aptx_48691")
        time.sleep(1)
        # 点击登录按钮
        driver.find_element_by_id("login_button").click()
        # 跳出登录iframe
        driver.switch_to.default_content()
        time.sleep(3)

    # 输入收件人信息内容
    def send(self):
        # 点击写信按钮
        write_btn = driver.find_element_by_xpath(
            "//div[@id='resize']/div[@id='leftPanel']/div[@id='navBarDiv']/ul/li[@id='composebtn_td']/a")
        write_btn.click()
        time.sleep(2)
        # 进入写信iframe
        write_frame = driver.find_element_by_xpath(
            "//div[@id='resize']/div[@id='mainFrameContainer']/iframe[@id='mainFrame']")
        driver.switch_to.frame(write_frame)
        time.sleep(1)
        # 输入对方账号
        object_input = driver.find_element_by_xpath(
            "//body/form[2]/div[2]/div[3]/div[@id='addrsDiv' and "
            "@class='js_addr_div']/table[2]/tbody/tr/td[2]/div/div[@class='addr_text']/input")
        object_input.send_keys("2214571423@qq.com")
        time.sleep(1)
        # 输入主题
        theme_input = driver.find_element_by_xpath(
            "//body/form[2]/div[2]/div[3]/table[3]/tbody/tr[2]/td[2]/div/div/div/input")
        theme_input.send_keys("520")
        time.sleep(1)
        # 进入正文iframe
        content_frame = driver.find_element_by_xpath(
            "//div[@id='QMEditorArea']/table/tbody/tr[2]/td/iframe")
        driver.switch_to.frame(content_frame)
        time.sleep(1)
        # 输入正文内容
        driver.find_element_by_xpath("//body").send_keys(u"我爱你")
        # 返回到父iframe-正文iframe
        driver.switch_to.parent_frame()
        time.sleep(1)
        # 点击发送按钮
        driver.find_element_by_xpath("//body/form[2]/div[1]/div/a[1]").click()
        time.sleep(3)

    # 关闭浏览器
    def closeBroswer(self):
        driver.quit()

    # 运行def
    def run(self):
        self.openBroswer()
        self.login()
        self.send()
        self.closeBroswer()


if __name__ == '__main__':
    _this = qqEmail()
    _this.run()
