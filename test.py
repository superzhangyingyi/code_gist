from selenium import webdriver
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
browser = webdriver.Chrome(options=option)
browser.get('http://www.baidu.com/')
