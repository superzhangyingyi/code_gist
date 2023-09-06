from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_webdriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized') #浏览器最大化
    options.add_experimental_option("detach", True) #不自动关闭浏览器
    browser=webdriver.Chrome(options=options)
    browser.get('http://192.168.3.118')
    login(browser, 'zyy', '22222222')

# 登录
def login(browser, userName, passWord):
    #显式等待 dom元素加载完成
    login_DOM_userName=WebDriverWait(browser,10,0.5).until(EC.presence_of_element_located((By.ID, "txt_username")))
    login_DOM_password=WebDriverWait(browser,10,0.5).until(EC.presence_of_element_located((By.ID, "txt_password")))
    login_DOM_userName.send_keys(userName)
    login_DOM_password.send_keys(passWord)
    # 24h自动登录
    login_DOM_rember_btn=WebDriverWait(browser,10,0.5).until(EC.presence_of_element_located((By.ID, "cb_remember_me")))
    login_DOM_rember_btn.click()
    login_DOM_login_btn=WebDriverWait(browser,10,0.5).until(EC.presence_of_element_located((By.TAG_NAME, "button")))
    login_DOM_login_btn.click()
    overview_short(browser)
    
def overview_short(browser):
    login_DOM_close_pop_btn=WebDriverWait(browser,10,0.5).until(EC.presence_of_element_located((By.CLASS_NAME, "close")))
    login_DOM_close_pop_btn.click()
    

if __name__ == '__main__':
    run_webdriver()