from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url="https://www.baidu.com/"
driver=webdriver.PhantomJS()
dcap=dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"]=(" Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0")

driver=webdriver.PhantomJS(desired_capabilities=dcap)
driver.implicitly_wait(20)

driver.get(url=url)