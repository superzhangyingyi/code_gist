## custom_plugins 浏览器自定义插件
1. 是通过自定义浏览器插件实现的，无需安装三方库和额外驱动,打开浏览器开发者模式，传入整个文件夹即可
2. edge和chrome均已支持

## each5s_append_file 每5秒往文件追加字符

## create_vm_job 创建虚拟化作业示例
1. 接口/ds/dbackup/:路由最后有/
2. 该接口使用`'Content-Type': 'application/x-www-form-urlencoded',`在requests请求中需要data 参数发送数据
    - data参数：
        - 发送的数据仍使用对象类型传入，由request库自动处理并转译后再发送数据
        - 响应头默认置为application/x-www-form-urlencoded
    - json参数：
        - 响应头默认置为application/json
3. 存在python脚本和bash脚本两种写法，均成功
    - bash脚本中，只有虚拟化作业名称是转译过的，否则乱码

## webhook_receive
1. 为webhook的接收平台测试，在迪备中配置URL地址为 http://IP:443/webhook
2. 均可以简单显示由迪备发出的post请求的body和请求头
    1. main.js
        - 需要node.js环境运行
        - 有转换成企业微信机器人消息推送功能，将迪备请求转换后发送到机器人webhook
            - 将迪备的请求头和body重新打包成{'head':迪备请求头, 'body':迪备body}
            - (功能尚未认证)
    2. fl.py
        - 需要安装`pip3 install flask` (迪备环境不自带)



# test_Experience
1.作业的前置条件执行的时候，该作业处于running状态
2.执行前置脚本时，执行python脚本文件也会阻塞进程，即使忽略执行结果，仍然阻塞，作业只有进度条不会执行
