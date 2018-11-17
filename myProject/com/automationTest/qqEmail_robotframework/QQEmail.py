#!/usr/bin/python
# -*- coding: UTF-8 -*-
from robot.api import TestSuite
from robot.api import ResultWriter
import sys

if sys.getdefaultencoding() != 'UTF-8':
    reload(sys)
    sys.setdefaultencoding('UTF-8')


# 发送邮件测试
class SendMailTest:
    def __init__(self, name, librarys=["Selenium2Library"]):
        # 创建测试套件
        self.suite = TestSuite(name)
        # 导入Selenium2Library
        for lib in librarys:
            self.suite.resource.imports.library(lib)

    # 定义变量
    def create_variables(self):
        variables = {
            "${qqemail}": "https://mail.qq.com/",
            "${browser}": "Chrome",
            "${login_frame}": "id=login_frame",
            "${name_input}": "id=u",
            "${password_input}": "id=p",
            "${login_btn}": "id=login_button",
            "${write_btn}": "xpath=//div[@id='resize']/div[@id='leftPanel']/"
                            "div[@id='navBarDiv']/ul/li[@id='composebtn_td']/a",
            "${write_frame}": "xpath=//div[@id='resize']/div[@id='mainFrameContainer']/"
                              "iframe[@id='mainFrame']",
            "${object_input}": "xpath=//body/form[2]/div[2]/div[3]/div[@id='addrsDiv' "
                               "and @class='js_addr_div']/table[2]/tbody/tr/td[2]/div/div[@class='addr_text']/input",
            "${theme_input}": "xpath=//body/form[2]/div[2]/div[3]/table[3]/tbody/tr[2]/"
                              "td[2]/div/div/div/input",
            "${content_frame}": "xpath=//div[@id='QMEditorArea']/table/tbody/tr[2]/td/iframe",
            "${content_input}": "xpath=//body",
            "${send_btn}": "xpath=//body/form[2]/div[1]/div/a[1]"

        }
        for k, v in variables.items():
            self.suite.resource.variables.create(k, v)

    # 测试用例:启动浏览器
    def open_browsers(self):
        test_01 = self.suite.tests.create("Start_up-Borwser")
        test_01.keywords.create("Open Browser", args=["${qqemail}", "${browser}"])
        test_01.keywords.create("Maximize Browser Window")

    # 测试用例:QQ邮箱登录、发件测试
    def search_word(self):
        test_02 = self.suite.tests.create("QQEmail-Login-Test")
        test_02.keywords.create("Select Frame", args=["${login_frame}"])
        test_02.keywords.create("Input Text", args=["${name_input}", "357112130@qq.com"])
        test_02.keywords.create("Input Text", args=["${password_input}", "aptx_48691"])
        test_02.keywords.create("Click Button", args=["${login_btn}"])
        test_02.keywords.create("Unselect Frame")
        test_02.keywords.create("Sleep", args=["3s"])
        test_02 = self.suite.tests.create("QQEmail-SendEmail-Test")
        test_02.keywords.create("Click Element", args=["${write_btn}"])
        test_02.keywords.create("Sleep", args=["2s"])
        test_02.keywords.create("Select Frame", args=["${write_frame}"])
        test_02.keywords.create("Input Text", args=["${object_input}", "2214571423@qq.com"])
        test_02.keywords.create("Input Text", args=["${theme_input}", "520"])
        test_02.keywords.create("Select Frame", args=["${content_frame}"])
        test_02.keywords.create("Input Text", args=["${content_input}", "I Love You"])
        test_02.keywords.create("Unselect Frame")
        test_02.keywords.create("Select Frame", args=["${write_frame}"])
        test_02.keywords.create("Click Element", args=["${send_btn}"])
        test_02.keywords.create("Sleep", args=["5s"])

    # 测试用例:断言验证发送邮件结果
    # def assert_title(self):
    #     test_03 = self.suite.tests.create("断言验证发送邮件结果")
    #     test_03.keywords.create("Title Should Be", args=["您的邮件已发送"])

    # 测试用例:关闭浏览器
    def close_browsers(self):
        test_04 = self.suite.tests.create("Close-Browser")
        test_04.keywords.create("Close All Browsers")

    # 运行
    def run(self):
        self.create_variables()
        self.open_browsers()
        self.search_word()
        #self.assert_title()
        self.close_browsers()

        # 运行套件
        result = self.suite.run(critical="SendEamil", output="output.xml")

        # 生成日志、报告文件
        ResultWriter(result).write_results(
            report="report.html", log="log.html")


if __name__ == "__main__":
    print("用Python写Robot Framework测试")
    suite = SendMailTest("SendEmail-TestSuite")
    suite.run()
