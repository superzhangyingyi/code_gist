## custom_plugins 浏览器自定义插件
1. 是通过自定义浏览器插件实现的，无需安装三方库和额外驱动,打开浏览器开发者模式，传入整个文件夹即可
2. edge和chrome均已支持

## each5s_append_file 每5秒往文件追加字符

# create_vm_job 创建虚拟化作业示例
1. 接口/ds/dbackup/:路由最后有/
2. 该接口使用`'Content-Type': 'application/x-www-form-urlencoded',`注意提交参数格式

# test_Experience
1.作业的前置条件执行的时候，该作业处于running状态
2.执行前置脚本时，执行python脚本文件也会阻塞进程，即使忽略执行结果，仍然阻塞，作业只有进度条不会执行
