## 安装
1. 安装selenium库 `pip install selenium`
2. 确定浏览器版本
3. 下载对应驱动 
    - chrome： `http://chromedriver.storage.googleapis.com/index.html`
    - edge： `https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/`
    - 只要版本号开头的数字相同就可以了
4. 解压拷贝到python安装目录下
    - edge 报错则需要将文件重命名为 MicrosoftWebDriver.exe

## 测试
```
from selenium import webdriver

driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.get('https://www.baidu.com')
```

## v1.1
1. overview是通过延迟来等待预览界面加载完成再截图的，延迟时间为传入overview_screenshot的参数